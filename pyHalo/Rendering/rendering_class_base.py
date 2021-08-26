from abc import ABC, abstractmethod

class RenderingClassBase(ABC):

    """
    This is the base class for a rendering_class, or a python object that generates the masses and positions of structure
    in strong lens systems. A rendering_class in pyHalo is defined as an object that contains the following methods:

    1) render: returns the object masses [numpy array], x coordinate in arcsec [numpy array],
    y coordinate in arcsec [numpy array], three dimensional position inside host halo in physical kpc
    if the object is a subhalo, else None [numpy array], the redshifts of each object [numpy array],
    and a list of bools that specify whether the object is a subhalo, or an object in the field [python list]

    2) convergence_sheet_correction: returns the lenstronomy keywords, the lenstronomy profile name, and the redshifts of
    lens models that subtract mass from the lensing volume to correct for the mass added in the form of dark matter
    halos.

    3) keyword_parse_render: extracts just the keyword arguments required to render halos from a giant dictionary that
    specifies all keyword arguments for the mass function, spatial distribution, mass definition, etc.

    4) keys_convergence_sheets: extracts just the keyword arguments required to specify the form of the convergence
    sheet correction

    """

    @staticmethod
    def _redshift_dependent_mass_range(z, log_mlow_object, log_mhigh_object):
        """
        Evaluates a possibly redshift-dependent minimum/maximum halo mass
        :param z: redshift
        :param log_mlow_object: either a number representing the minimum halo mass, or a callable function that returns
        log10(M_min) as a function z
        :param log_mhigh_object: either a number representing the maximum halo mass, or a callable function that returns
        log10(M_max) as a function z
        :return: the minimum and maximum halo mass (in log10)
        """

        if callable(log_mlow_object):
            log_mlow = log_mlow_object(z)
        else:
            log_mlow = log_mlow_object

        if callable(log_mhigh_object):
            log_mhigh = log_mhigh_object(z)
        else:
            log_mhigh = log_mhigh_object

        return log_mlow, log_mhigh

    @abstractmethod
    def render(self, *args, **kwargs):
        ...

    @abstractmethod
    def convergence_sheet_correction(self, *args, **kwargs):
        ...

    @staticmethod
    @abstractmethod
    def keys_convergence_sheets(keywords_master):
        ...

    @staticmethod
    @abstractmethod
    def keyword_parse_render(keywords_master):
        ...



