import numpy.testing as npt
from pyHalo.Cosmology.lensing_mass_function import LensingMassFunction, massFunction
from pyHalo.Cosmology.cosmology import Cosmology
from pyHalo.Rendering.MassFunctions.mass_function_base import GeneralPowerLaw
from pyHalo.Rendering.MassFunctions.delta_function import ScaleFree
import pytest
from scipy.integrate import quad
import numpy as np

class TestLensingMassFunction(object):

    def setup(self):

        cosmo = Cosmology()
        mlow = 10**6
        mhigh = 10**10
        zlens = 0.5
        zsource = 1.5
        cone_opening_angle = 6.
        m_pivot = 10**8
        mass_function_model = 'sheth99'
        use_lookup_table = True
        geometry_type = 'DOUBLE_CONE'
        self.lmf_lookup_ShethTormen = LensingMassFunction(cosmo, zlens, zsource, mlow, mhigh, cone_opening_angle, m_pivot,
                                       mass_function_model, use_lookup_table, geometry_type)

        use_lookup_table = False
        self.lmf_no_lookup_ShethTormen = LensingMassFunction(cosmo, zlens, zsource, mlow, mhigh, cone_opening_angle, m_pivot,
                                              mass_function_model, use_lookup_table, geometry_type)

        self._m = np.logspace(6., 10, 50)

        self.cosmo = cosmo
        self.cone_opening_angle = cone_opening_angle

    def test_lookup(self):

        dndm_1 = self.lmf_lookup_ShethTormen.dN_dMdV_comoving(self._m, 0.5)
        dndm_2 = self.lmf_no_lookup_ShethTormen.dN_dMdV_comoving(self._m, 0.5)
        npt.assert_almost_equal(dndm_1, dndm_2)

    def test_normalization(self):

        z = 0.5
        plaw_index = self.lmf_lookup_ShethTormen.plaw_index_z(z)
        rho_dv = self.lmf_lookup_ShethTormen.norm_at_z_density(z, plaw_index, 10**8)
        dz = 0.01
        rho = self.lmf_no_lookup_ShethTormen.norm_at_z(z, plaw_index, dz, 10**8)

        radius_arcsec = self.cone_opening_angle * 0.5
        A = self.lmf_lookup_ShethTormen.geometry.angle_to_comoving_area(radius_arcsec, z)
        dr = self.cosmo.D_C_transverse(z + dz) - self.cosmo.D_C_transverse(z)
        dv = A * dr
        rho_2 = dv * rho_dv
        npt.assert_almost_equal(rho_2/rho, 1.0, 2)

    def test_power_law_index(self):

        plaw_index = self.lmf_lookup_ShethTormen.plaw_index_z(0.5)
        npt.assert_almost_equal(plaw_index, -1.91)
        plaw_index = self.lmf_no_lookup_ShethTormen.plaw_index_z(0.5)
        npt.assert_almost_equal(np.round(plaw_index, 2), -1.91)

    def test_two_halo_boost(self):

        z = 0.5
        m_halo = 10 ** 13
        def _integrand(x):
            return self.lmf_no_lookup_ShethTormen.twohaloterm(x, m_halo, z)

        dz = 0.01
        dr = self.cosmo.D_C_transverse(z + dz) - self.cosmo.D_C_transverse(z)
        integral_over_two_halo_term = quad(_integrand, 0.5, dr)[0]
        length = dr - 0.5
        average_value = integral_over_two_halo_term / length

        # factor of two for symmetry in front/behind lens
        boost_factor = 1 + 2 * average_value
        boost_factor_no_lookup = self.lmf_no_lookup_ShethTormen.two_halo_boost(m_halo, z, 0.5, dr)
        boost_factor_lookup = self.lmf_lookup_ShethTormen.two_halo_boost(m_halo, z, 0.5, dr)
        npt.assert_almost_equal(boost_factor, boost_factor_no_lookup)
        npt.assert_almost_equal(boost_factor, boost_factor_lookup)

    def test_component_density(self):

        f = 1.
        rho = self.lmf_no_lookup_ShethTormen.component_density(f)
        rho_dm = self.cosmo.astropy.Odm(0.) * self.cosmo.astropy.critical_density(0.).value
        rho_dm *= self.cosmo.density_to_MsunperMpc
        npt.assert_almost_equal(rho, rho_dm, 4)

    def test_mass_function_fit(self):

        m = np.logspace(6, 10, 50)
        m_pivot = 10 ** 8

        z = 0.2
        norm_mpivot_8, index = self.lmf_no_lookup_ShethTormen._mass_function_params(m, z)
        norm_theory = self.lmf_no_lookup_ShethTormen.norm_at_z_density(z, index, 10**8)
        norm = norm_mpivot_8 / (m_pivot**index)
        npt.assert_almost_equal(norm/norm_theory, 1., 3)

        z = 1.2
        norm_mpivot_8, index = self.lmf_no_lookup_ShethTormen._mass_function_params(m, z)
        norm_theory = self.lmf_no_lookup_ShethTormen.norm_at_z_density(z, index, 10 ** 8)
        norm = norm_mpivot_8 / (m_pivot ** index)
        npt.assert_almost_equal(norm / norm_theory, 1., 3)

    def test_mass_fraction_in_halos(self):

        z = 0.5
        mlow = 10 ** 6
        mhigh = 10 ** 9
        frac1 = self.lmf_no_lookup_ShethTormen.mass_fraction_in_halos(z, mlow, mhigh, mlow_global=10**-4)
        frac2 = self.lmf_no_lookup_ShethTormen.mass_fraction_in_halos(z, 10**-4, mhigh, mlow_global=10**-4)
        frac3 = self.lmf_no_lookup_ShethTormen.mass_fraction_in_halos(z, 0.99999 * mhigh, mhigh)
        npt.assert_almost_equal(frac2, 1)
        npt.assert_almost_equal(frac1, 0.43799, 3)
        npt.assert_almost_equal(frac3, 0., 3)

    def test_norm(self):

        h = self.cosmo.h

        z = 0.5
        mass_function = self.lmf_no_lookup_ShethTormen.dN_dMdV_comoving

        m = np.logspace(6, 10, 10)

        # units Mpc ^ -3 M ^ -1
        mfunc = mass_function(m, z)

        # to units (Mpc/h) ^ =3 M ^ -1
        mfunc *= h ** -3

        # to units (Mpc/h) ^ -3 (M/h) ^ -1
        mfunc *= h ** -1
        coefs = np.polyfit(np.log10(m), np.log10(mfunc), 1)
        # coefs = (-1.907, 8.732)

        m_h = m * h
        # units (Mpc/h) ^ -3 ln(M/h)^-1
        dndlogm = massFunction(m_h, z, q_out='dndlnM', model='sheth99')
        # units (Mpc/h) ^ -3 M ^ -1
        dndm = dndlogm / m
        # units (Mpc/h) ^ -3 (M/h) ^ -1
        dndm *= h ** -1
        coefs_theory = np.polyfit(np.log10(m), np.log10(dndm), 1)
        # coefs_theory = (-1.907, 8.732)

        npt.assert_almost_equal(coefs_theory, coefs)

    def test_samples(self):

        h = self.cosmo.h
        z = 0.5

        volume_element = 100000.
        nbins = 15
        m = np.logspace(6, 8.7, nbins)
        m_h = m * h
        dndlnmdv = massFunction(m_h, z, q_out='dndlnM', model='sheth99')
        dndm_theory = dndlnmdv * h ** 3 / m
        coefs_theory = np.polyfit(np.log10(m), np.log10(dndm_theory), 1)

        norm_theory = coefs_theory[1]
        plaw_index_theory = coefs_theory[0]

        norm = volume_element * self.lmf_no_lookup_ShethTormen.norm_at_z_density(z, plaw_index_theory, 10**8)

        model = ScaleFree()
        kwargs_model = {}
        mfunc = GeneralPowerLaw(6, 8.7, plaw_index_theory, False, norm, model, kwargs_model)
        mdraw = mfunc.draw()
        dndm_model = []

        mstep = 0.08
        msteps = 10**np.arange(6, 8.7+mstep, mstep)
        for i in range(0, len(msteps)-1):
            cond1 = mdraw >= msteps[i]
            cond2 = mdraw < msteps[i+1]
            n = np.sum(np.logical_and(cond1, cond2))
            delta_m = msteps[i+1] - msteps[i]
            new = n / delta_m
            dndm_model.append(new)

        coefs_model = np.polyfit(np.log10(msteps[0:-1]), np.log10(dndm_model), 1)
        norm_model = coefs_model[1]
        npt.assert_almost_equal(10**(norm_model - norm_theory) / volume_element, 1, 1)

if __name__ == '__main__':
       pytest.main()
