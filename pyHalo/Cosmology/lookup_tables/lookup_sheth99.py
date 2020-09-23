import numpy as np
norm_z_dV = [1.81137e-07, 1.8207e-07, 1.83009e-07, 1.83956e-07, 1.84908e-07, 1.85866e-07, 1.8683e-07, 1.87799e-07, 1.88773e-07, 1.89751e-07, 1.90733e-07, 1.91719e-07, 1.92707e-07, 1.93698e-07, 1.94691e-07, 1.95686e-07, 1.96682e-07, 1.97679e-07, 1.98677e-07, 1.99675e-07, 2.00673e-07, 2.01671e-07, 2.02668e-07, 2.03664e-07, 2.04659e-07, 2.05653e-07, 2.06645e-07, 2.07635e-07, 2.08622e-07, 2.09608e-07, 2.10591e-07, 2.11571e-07, 2.12548e-07, 2.13521e-07, 2.14491e-07, 2.15458e-07, 2.1642e-07, 2.17379e-07, 2.18333e-07, 2.19282e-07, 2.20227e-07, 2.21166e-07, 2.22101e-07, 2.2303e-07, 2.23954e-07, 2.24872e-07, 2.25785e-07, 2.26691e-07, 2.27592e-07, 2.28486e-07, 2.29374e-07, 2.30257e-07, 2.31132e-07, 2.32002e-07, 2.32865e-07, 2.33721e-07, 2.3457e-07, 2.35413e-07, 2.36249e-07, 2.37078e-07, 2.379e-07, 2.38715e-07, 2.39523e-07, 2.40324e-07, 2.41117e-07, 2.41903e-07, 2.42681e-07, 2.43451e-07, 2.44214e-07, 2.4497e-07, 2.45717e-07, 2.46457e-07, 2.47189e-07, 2.47912e-07, 2.48628e-07, 2.49336e-07, 2.50035e-07, 2.50727e-07, 2.5141e-07, 2.52086e-07, 2.52753e-07, 2.53412e-07, 2.54063e-07, 2.54706e-07, 2.5534e-07, 2.55966e-07, 2.56584e-07, 2.57193e-07, 2.57795e-07, 2.58388e-07, 2.58972e-07, 2.59548e-07, 2.60116e-07, 2.60675e-07, 2.61226e-07, 2.61769e-07, 2.62303e-07, 2.62828e-07, 2.63345e-07, 2.63854e-07, 2.64354e-07, 2.64845e-07, 2.65328e-07, 2.65802e-07, 2.66268e-07, 2.66725e-07, 2.67174e-07, 2.67614e-07, 2.68046e-07, 2.68469e-07, 2.68883e-07, 2.69289e-07, 2.69686e-07, 2.70075e-07, 2.70455e-07, 2.70827e-07, 2.7119e-07, 2.71544e-07, 2.71891e-07, 2.72228e-07, 2.72557e-07, 2.72878e-07, 2.7319e-07, 2.73494e-07, 2.73789e-07, 2.74076e-07, 2.74354e-07, 2.74624e-07, 2.74885e-07, 2.75138e-07, 2.75383e-07, 2.75619e-07, 2.75847e-07, 2.76067e-07, 2.76278e-07, 2.76481e-07, 2.76676e-07, 2.76862e-07, 2.7704e-07, 2.7721e-07, 2.77372e-07, 2.77525e-07, 2.7767e-07, 2.77807e-07, 2.77936e-07, 2.78057e-07, 2.7817e-07, 2.78274e-07, 2.78371e-07, 2.78459e-07, 2.7854e-07, 2.78612e-07, 2.78677e-07, 2.78733e-07, 2.78782e-07, 2.78822e-07, 2.78855e-07, 2.7888e-07, 2.78897e-07, 2.78907e-07, 2.78908e-07, 2.78902e-07, 2.78888e-07, 2.78867e-07, 2.78838e-07, 2.78801e-07, 2.78756e-07, 2.78704e-07, 2.78645e-07, 2.78577e-07, 2.78503e-07, 2.78421e-07, 2.78331e-07, 2.78235e-07, 2.7813e-07, 2.78019e-07, 2.779e-07, 2.77774e-07, 2.77641e-07, 2.775e-07, 2.77352e-07, 2.77198e-07, 2.77036e-07, 2.76867e-07, 2.76691e-07, 2.76508e-07, 2.76318e-07, 2.76121e-07, 2.75917e-07, 2.75707e-07, 2.75489e-07, 2.75265e-07, 2.75034e-07, 2.74797e-07, 2.74552e-07, 2.74301e-07, 2.74044e-07, 2.7378e-07, 2.73509e-07, 2.73232e-07, 2.72949e-07, ]
plaw_index_z = [-1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.97, -1.97, -1.97, ]
z_range = np.array([0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33, 0.35, 0.37, 0.39, 0.41, 0.43, 0.45, 0.47, 0.49, 0.51, 0.53, 0.55, 0.57, 0.59, 0.61, 0.63, 0.65, 0.67, 0.69, 0.71, 0.73, 0.75, 0.77, 0.79, 0.81, 0.83, 0.85, 0.87, 0.89, 0.91, 0.93, 0.95, 0.97, 0.99, 1.01, 1.03, 1.05, 1.07, 1.09, 1.11, 1.13, 1.15, 1.17, 1.19, 1.21, 1.23, 1.25, 1.27, 1.29, 1.31, 1.33, 1.35, 1.37, 1.39, 1.41, 1.43, 1.45, 1.47, 1.49, 1.51, 1.53, 1.55, 1.57, 1.59, 1.61, 1.63, 1.65, 1.67, 1.69, 1.71, 1.73, 1.75, 1.77, 1.79, 1.81, 1.83, 1.85, 1.87, 1.89, 1.91, 1.93, 1.95, 1.97, 1.99, 2.01, 2.03, 2.05, 2.07, 2.09, 2.11, 2.13, 2.15, 2.17, 2.19, 2.21, 2.23, 2.25, 2.27, 2.29, 2.31, 2.33, 2.35, 2.37, 2.39, 2.41, 2.43, 2.45, 2.47, 2.49, 2.51, 2.53, 2.55, 2.57, 2.59, 2.61, 2.63, 2.65, 2.67, 2.69, 2.71, 2.73, 2.75, 2.77, 2.79, 2.81, 2.83, 2.85, 2.87, 2.89, 2.91, 2.93, 2.95, 2.97, 2.99, 3.01, 3.03, 3.05, 3.07, 3.09, 3.11, 3.13, 3.15, 3.17, 3.19, 3.21, 3.23, 3.25, 3.27, 3.29, 3.31, 3.33, 3.35, 3.37, 3.39, 3.41, 3.43, 3.45, 3.47, 3.49, 3.51, 3.53, 3.55, 3.57, 3.59, 3.61, 3.63, 3.65, 3.67, 3.69, 3.71, 3.73, 3.75, 3.77, 3.79, 3.81, 3.83, 3.85, 3.87, 3.89, 3.91, 3.93, 3.95, 3.97, 3.99, 4.01, ])

delta_z = 0.02

