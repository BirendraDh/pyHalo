import numpy as np
from scipy.interpolate import interp1d

logxvalues = np.array([-3.00000000e+00, -2.99198397e+00, -2.98396794e+00, -2.97595190e+00,
       -2.96793587e+00, -2.95991984e+00, -2.95190381e+00, -2.94388778e+00,
       -2.93587174e+00, -2.92785571e+00, -2.91983968e+00, -2.91182365e+00,
       -2.90380762e+00, -2.89579158e+00, -2.88777555e+00, -2.87975952e+00,
       -2.87174349e+00, -2.86372745e+00, -2.85571142e+00, -2.84769539e+00,
       -2.83967936e+00, -2.83166333e+00, -2.82364729e+00, -2.81563126e+00,
       -2.80761523e+00, -2.79959920e+00, -2.79158317e+00, -2.78356713e+00,
       -2.77555110e+00, -2.76753507e+00, -2.75951904e+00, -2.75150301e+00,
       -2.74348697e+00, -2.73547094e+00, -2.72745491e+00, -2.71943888e+00,
       -2.71142285e+00, -2.70340681e+00, -2.69539078e+00, -2.68737475e+00,
       -2.67935872e+00, -2.67134269e+00, -2.66332665e+00, -2.65531062e+00,
       -2.64729459e+00, -2.63927856e+00, -2.63126253e+00, -2.62324649e+00,
       -2.61523046e+00, -2.60721443e+00, -2.59919840e+00, -2.59118236e+00,
       -2.58316633e+00, -2.57515030e+00, -2.56713427e+00, -2.55911824e+00,
       -2.55110220e+00, -2.54308617e+00, -2.53507014e+00, -2.52705411e+00,
       -2.51903808e+00, -2.51102204e+00, -2.50300601e+00, -2.49498998e+00,
       -2.48697395e+00, -2.47895792e+00, -2.47094188e+00, -2.46292585e+00,
       -2.45490982e+00, -2.44689379e+00, -2.43887776e+00, -2.43086172e+00,
       -2.42284569e+00, -2.41482966e+00, -2.40681363e+00, -2.39879760e+00,
       -2.39078156e+00, -2.38276553e+00, -2.37474950e+00, -2.36673347e+00,
       -2.35871743e+00, -2.35070140e+00, -2.34268537e+00, -2.33466934e+00,
       -2.32665331e+00, -2.31863727e+00, -2.31062124e+00, -2.30260521e+00,
       -2.29458918e+00, -2.28657315e+00, -2.27855711e+00, -2.27054108e+00,
       -2.26252505e+00, -2.25450902e+00, -2.24649299e+00, -2.23847695e+00,
       -2.23046092e+00, -2.22244489e+00, -2.21442886e+00, -2.20641283e+00,
       -2.19839679e+00, -2.19038076e+00, -2.18236473e+00, -2.17434870e+00,
       -2.16633267e+00, -2.15831663e+00, -2.15030060e+00, -2.14228457e+00,
       -2.13426854e+00, -2.12625251e+00, -2.11823647e+00, -2.11022044e+00,
       -2.10220441e+00, -2.09418838e+00, -2.08617234e+00, -2.07815631e+00,
       -2.07014028e+00, -2.06212425e+00, -2.05410822e+00, -2.04609218e+00,
       -2.03807615e+00, -2.03006012e+00, -2.02204409e+00, -2.01402806e+00,
       -2.00601202e+00, -1.99799599e+00, -1.98997996e+00, -1.98196393e+00,
       -1.97394790e+00, -1.96593186e+00, -1.95791583e+00, -1.94989980e+00,
       -1.94188377e+00, -1.93386774e+00, -1.92585170e+00, -1.91783567e+00,
       -1.90981964e+00, -1.90180361e+00, -1.89378758e+00, -1.88577154e+00,
       -1.87775551e+00, -1.86973948e+00, -1.86172345e+00, -1.85370741e+00,
       -1.84569138e+00, -1.83767535e+00, -1.82965932e+00, -1.82164329e+00,
       -1.81362725e+00, -1.80561122e+00, -1.79759519e+00, -1.78957916e+00,
       -1.78156313e+00, -1.77354709e+00, -1.76553106e+00, -1.75751503e+00,
       -1.74949900e+00, -1.74148297e+00, -1.73346693e+00, -1.72545090e+00,
       -1.71743487e+00, -1.70941884e+00, -1.70140281e+00, -1.69338677e+00,
       -1.68537074e+00, -1.67735471e+00, -1.66933868e+00, -1.66132265e+00,
       -1.65330661e+00, -1.64529058e+00, -1.63727455e+00, -1.62925852e+00,
       -1.62124248e+00, -1.61322645e+00, -1.60521042e+00, -1.59719439e+00,
       -1.58917836e+00, -1.58116232e+00, -1.57314629e+00, -1.56513026e+00,
       -1.55711423e+00, -1.54909820e+00, -1.54108216e+00, -1.53306613e+00,
       -1.52505010e+00, -1.51703407e+00, -1.50901804e+00, -1.50100200e+00,
       -1.49298597e+00, -1.48496994e+00, -1.47695391e+00, -1.46893788e+00,
       -1.46092184e+00, -1.45290581e+00, -1.44488978e+00, -1.43687375e+00,
       -1.42885772e+00, -1.42084168e+00, -1.41282565e+00, -1.40480962e+00,
       -1.39679359e+00, -1.38877756e+00, -1.38076152e+00, -1.37274549e+00,
       -1.36472946e+00, -1.35671343e+00, -1.34869739e+00, -1.34068136e+00,
       -1.33266533e+00, -1.32464930e+00, -1.31663327e+00, -1.30861723e+00,
       -1.30060120e+00, -1.29258517e+00, -1.28456914e+00, -1.27655311e+00,
       -1.26853707e+00, -1.26052104e+00, -1.25250501e+00, -1.24448898e+00,
       -1.23647295e+00, -1.22845691e+00, -1.22044088e+00, -1.21242485e+00,
       -1.20440882e+00, -1.19639279e+00, -1.18837675e+00, -1.18036072e+00,
       -1.17234469e+00, -1.16432866e+00, -1.15631263e+00, -1.14829659e+00,
       -1.14028056e+00, -1.13226453e+00, -1.12424850e+00, -1.11623246e+00,
       -1.10821643e+00, -1.10020040e+00, -1.09218437e+00, -1.08416834e+00,
       -1.07615230e+00, -1.06813627e+00, -1.06012024e+00, -1.05210421e+00,
       -1.04408818e+00, -1.03607214e+00, -1.02805611e+00, -1.02004008e+00,
       -1.01202405e+00, -1.00400802e+00, -9.95991984e-01, -9.87975952e-01,
       -9.79959920e-01, -9.71943888e-01, -9.63927856e-01, -9.55911824e-01,
       -9.47895792e-01, -9.39879760e-01, -9.31863727e-01, -9.23847695e-01,
       -9.15831663e-01, -9.07815631e-01, -8.99799599e-01, -8.91783567e-01,
       -8.83767535e-01, -8.75751503e-01, -8.67735471e-01, -8.59719439e-01,
       -8.51703407e-01, -8.43687375e-01, -8.35671343e-01, -8.27655311e-01,
       -8.19639279e-01, -8.11623246e-01, -8.03607214e-01, -7.95591182e-01,
       -7.87575150e-01, -7.79559118e-01, -7.71543086e-01, -7.63527054e-01,
       -7.55511022e-01, -7.47494990e-01, -7.39478958e-01, -7.31462926e-01,
       -7.23446894e-01, -7.15430862e-01, -7.07414830e-01, -6.99398798e-01,
       -6.91382766e-01, -6.83366733e-01, -6.75350701e-01, -6.67334669e-01,
       -6.59318637e-01, -6.51302605e-01, -6.43286573e-01, -6.35270541e-01,
       -6.27254509e-01, -6.19238477e-01, -6.11222445e-01, -6.03206413e-01,
       -5.95190381e-01, -5.87174349e-01, -5.79158317e-01, -5.71142285e-01,
       -5.63126253e-01, -5.55110220e-01, -5.47094188e-01, -5.39078156e-01,
       -5.31062124e-01, -5.23046092e-01, -5.15030060e-01, -5.07014028e-01,
       -4.98997996e-01, -4.90981964e-01, -4.82965932e-01, -4.74949900e-01,
       -4.66933868e-01, -4.58917836e-01, -4.50901804e-01, -4.42885772e-01,
       -4.34869739e-01, -4.26853707e-01, -4.18837675e-01, -4.10821643e-01,
       -4.02805611e-01, -3.94789579e-01, -3.86773547e-01, -3.78757515e-01,
       -3.70741483e-01, -3.62725451e-01, -3.54709419e-01, -3.46693387e-01,
       -3.38677355e-01, -3.30661323e-01, -3.22645291e-01, -3.14629259e-01,
       -3.06613226e-01, -2.98597194e-01, -2.90581162e-01, -2.82565130e-01,
       -2.74549098e-01, -2.66533066e-01, -2.58517034e-01, -2.50501002e-01,
       -2.42484970e-01, -2.34468938e-01, -2.26452906e-01, -2.18436874e-01,
       -2.10420842e-01, -2.02404810e-01, -1.94388778e-01, -1.86372745e-01,
       -1.78356713e-01, -1.70340681e-01, -1.62324649e-01, -1.54308617e-01,
       -1.46292585e-01, -1.38276553e-01, -1.30260521e-01, -1.22244489e-01,
       -1.14228457e-01, -1.06212425e-01, -9.81963928e-02, -9.01803607e-02,
       -8.21643287e-02, -7.41482966e-02, -6.61322645e-02, -5.81162325e-02,
       -5.01002004e-02, -4.20841683e-02, -3.40681363e-02, -2.60521042e-02,
       -1.80360721e-02, -1.00200401e-02, -2.00400802e-03,  6.01202405e-03,
        1.40280561e-02,  2.20440882e-02,  3.00601202e-02,  3.80761523e-02,
        4.60921844e-02,  5.41082164e-02,  6.21242485e-02,  7.01402806e-02,
        7.81563126e-02,  8.61723447e-02,  9.41883768e-02,  1.02204409e-01,
        1.10220441e-01,  1.18236473e-01,  1.26252505e-01,  1.34268537e-01,
        1.42284569e-01,  1.50300601e-01,  1.58316633e-01,  1.66332665e-01,
        1.74348697e-01,  1.82364729e-01,  1.90380762e-01,  1.98396794e-01,
        2.06412826e-01,  2.14428858e-01,  2.22444890e-01,  2.30460922e-01,
        2.38476954e-01,  2.46492986e-01,  2.54509018e-01,  2.62525050e-01,
        2.70541082e-01,  2.78557114e-01,  2.86573146e-01,  2.94589178e-01,
        3.02605210e-01,  3.10621242e-01,  3.18637275e-01,  3.26653307e-01,
        3.34669339e-01,  3.42685371e-01,  3.50701403e-01,  3.58717435e-01,
        3.66733467e-01,  3.74749499e-01,  3.82765531e-01,  3.90781563e-01,
        3.98797595e-01,  4.06813627e-01,  4.14829659e-01,  4.22845691e-01,
        4.30861723e-01,  4.38877756e-01,  4.46893788e-01,  4.54909820e-01,
        4.62925852e-01,  4.70941884e-01,  4.78957916e-01,  4.86973948e-01,
        4.94989980e-01,  5.03006012e-01,  5.11022044e-01,  5.19038076e-01,
        5.27054108e-01,  5.35070140e-01,  5.43086172e-01,  5.51102204e-01,
        5.59118236e-01,  5.67134269e-01,  5.75150301e-01,  5.83166333e-01,
        5.91182365e-01,  5.99198397e-01,  6.07214429e-01,  6.15230461e-01,
        6.23246493e-01,  6.31262525e-01,  6.39278557e-01,  6.47294589e-01,
        6.55310621e-01,  6.63326653e-01,  6.71342685e-01,  6.79358717e-01,
        6.87374749e-01,  6.95390782e-01,  7.03406814e-01,  7.11422846e-01,
        7.19438878e-01,  7.27454910e-01,  7.35470942e-01,  7.43486974e-01,
        7.51503006e-01,  7.59519038e-01,  7.67535070e-01,  7.75551102e-01,
        7.83567134e-01,  7.91583166e-01,  7.99599198e-01,  8.07615230e-01,
        8.15631263e-01,  8.23647295e-01,  8.31663327e-01,  8.39679359e-01,
        8.47695391e-01,  8.55711423e-01,  8.63727455e-01,  8.71743487e-01,
        8.79759519e-01,  8.87775551e-01,  8.95791583e-01,  9.03807615e-01,
        9.11823647e-01,  9.19839679e-01,  9.27855711e-01,  9.35871743e-01,
        9.43887776e-01,  9.51903808e-01,  9.59919840e-01,  9.67935872e-01,
        9.75951904e-01,  9.83967936e-01,  9.91983968e-01,  1.00000000e+00])
logenergy = np.array([-9.09515608, -9.07165517, -9.04816272, -9.02467885, -9.00120367,
       -8.97773727, -8.95427976, -8.93083124, -8.90739183, -8.88396163,
       -8.86054075, -8.83712928, -8.81372735, -8.79033505, -8.7669525 ,
       -8.7435798 , -8.72021706, -8.69686438, -8.67352188, -8.65018967,
       -8.62686784, -8.60355651, -8.58025578, -8.55696577, -8.53368658,
       -8.51041831, -8.48716107, -8.46391497, -8.44068011, -8.41745661,
       -8.39424455, -8.37104406, -8.34785522, -8.32467816, -8.30012622,
       -8.27835972, -8.25521856, -8.23208958, -8.20897286, -8.18586851,
       -8.16277663, -8.13969731, -8.11663066, -8.09357676, -8.07053571,
       -8.0475076 , -8.02449252, -8.00149057, -7.97850183, -7.9555264 ,
       -7.93256435, -7.90961578, -7.88668076, -7.86375939, -7.84085173,
       -7.81795788, -7.7950779 , -7.77221188, -7.74935989, -7.72652201,
       -7.7036983 , -7.68088884, -7.65809369, -7.63531292, -7.61254659,
       -7.58979478, -7.56705754, -7.54433492, -7.521627  , -7.49893382,
       -7.47625543, -7.4535919 , -7.43094327, -7.40830959, -7.3856909 ,
       -7.36308726, -7.3404987 , -7.31792527, -7.29536701, -7.27282395,
       -7.25029613, -7.22778358, -7.20528634, -7.18280444, -7.16033791,
       -7.13788677, -7.11545105, -7.09303078, -7.07062597, -7.04823665,
       -7.02586284, -7.00350456, -6.98116182, -6.95883463, -6.93652302,
       -6.91422699, -6.89194656, -6.86968174, -6.84743253, -6.82519895,
       -6.80298099, -6.78077868, -6.75859201, -6.73642099, -6.71426562,
       -6.6921259 , -6.67000185, -6.64789346, -6.62580073, -6.60372366,
       -6.58166226, -6.55961653, -6.53758647, -6.51557208, -6.49357337,
       -6.47159032, -6.44962295, -6.42767126, -6.40573525, -6.38381492,
       -6.36191028, -6.34002133, -6.31814808, -6.29629053, -6.27444869,
       -6.25262257, -6.23081217, -6.20901751, -6.1872386 , -6.16547545,
       -6.14372808, -6.1219965 , -6.10028073, -6.07858079, -6.0568967 ,
       -6.03522848, -6.01357617, -5.99193977, -5.97031933, -5.94871488,
       -5.92712644, -5.90555406, -5.88399776, -5.8624576 , -5.84093362,
       -5.81942585, -5.79793435, -5.77645917, -5.75500035, -5.73355797,
       -5.71213206, -5.69072271, -5.66932996, -5.64795389, -5.62659456,
       -5.60525206, -5.58392645, -5.56261781, -5.54132623, -5.52005179,
       -5.49879458, -5.47755468, -5.45633221, -5.43512724, -5.41393989,
       -5.39277026, -5.37161845, -5.35048457, -5.32936874, -5.30827108,
       -5.2871917 , -5.26613073, -5.2450883 , -5.22406453, -5.20305956,
       -5.18207353, -5.16110657, -5.14015883, -5.11923046, -5.0983216 ,
       -5.07743241, -5.05656304, -5.03571366, -5.01488442, -4.9940755 ,
       -4.97328706, -4.95251927, -4.93177231, -4.91104637, -4.89034161,
       -4.86965824, -4.84899643, -4.82835638, -4.80774049, -4.78714234,
       -4.76656875, -4.74601772, -4.72548946, -4.70498418, -4.68450209,
       -4.66404341, -4.64360836, -4.62319717, -4.60281006, -4.58244726,
       -4.56210901, -4.54179554, -4.52150709, -4.50124391, -4.48100624,
       -4.46079433, -4.44060844, -4.42044881, -4.4003157 , -4.38020939,
       -4.36013013, -4.34007819, -4.32005385, -4.30005737, -4.28008903,
       -4.26014912, -4.24023792, -4.22035572, -4.2005028 , -4.18067946,
       -4.160886  , -4.14112271, -4.1213899 , -4.10168788, -4.08201695,
       -4.06237745, -4.04276971, -4.02319405, -4.00365063, -3.98414004,
       -3.96466232, -3.94521795, -3.92580742, -3.90643074, -3.88708843,
       -3.867781  , -3.84850844, -3.82927129, -3.8100699 , -3.7909048 ,
       -3.771776  , -3.75268404, -3.7336293 , -3.71461231, -3.69563308,
       -3.67669218, -3.65779   , -3.63892691, -3.62010329, -3.6013197 ,
       -3.58257619, -3.56387334, -3.54521154, -3.52659119, -3.5080127 ,
       -3.48947661, -3.47098304, -3.45253256, -3.43412557, -3.41576251,
       -3.39744378, -3.37916982, -3.36094104, -3.342758  , -3.32462089,
       -3.30653026, -3.28848656, -3.27049021, -3.25254167, -3.23464138,
       -3.21678979, -3.19898734, -3.18123457, -3.16353176, -3.14587944,
       -3.12827809, -3.11072817, -3.09323012, -3.07578441, -3.05839152,
       -3.0410519 , -3.02376602, -3.00653443, -2.98935744, -2.9722356 ,
       -2.95516939, -2.93815929, -2.92120575, -2.90430927, -2.88747031,
       -2.87068935, -2.85396688, -2.83730336, -2.82069928, -2.80415516,
       -2.78767138, -2.77124845, -2.75488688, -2.73858714, -2.72234969,
       -2.70617504, -2.69006361, -2.67401591, -2.6580324 , -2.64211355,
       -2.62625984, -2.61047187, -2.59474969, -2.57909418, -2.56350568,
       -2.54798462, -2.53253147, -2.51714668, -2.50183071, -2.486584  ,
       -2.47140701, -2.45630017, -2.44126391, -2.42629869, -2.41140494,
       -2.39658305, -2.38183346, -2.3671566 , -2.35255288, -2.3380227 ,
       -2.32356646, -2.30918458, -2.29487743, -2.28064541, -2.2664889 ,
       -2.25240826, -2.2384039 , -2.22447613, -2.21062534, -2.19685186,
       -2.18315606, -2.16953825, -2.15599877, -2.14253794, -2.12915608,
       -2.11585348, -2.10263045, -2.08948727, -2.07642424, -2.06344161,
       -2.05053967, -2.03771865, -2.02497883, -2.01232041, -1.99974364,
       -1.98724874, -1.97483592, -1.96250537, -1.9502573 , -1.93809188,
       -1.92600928, -1.91400967, -1.9020932 , -1.89026   , -1.87851021,
       -1.86684395, -1.85526134, -1.84376246, -1.83234742, -1.82101628,
       -1.80976913, -1.798606  , -1.78752696, -1.77653204, -1.76562127,
       -1.75479464, -1.74405218, -1.73339386, -1.72281969, -1.71232961,
       -1.7019236 , -1.69160161, -1.68136357, -1.6712094 , -1.66113903,
       -1.65115236, -1.64124928, -1.63142969, -1.62169345, -1.61204043,
       -1.60247047, -1.59298343, -1.58357914, -1.57425741, -1.56501805,
       -1.55586088, -1.54678569, -1.53779224, -1.52888033, -1.52004971,
       -1.51130013, -1.50263133, -1.49404306, -1.48553504, -1.47710699,
       -1.46875861, -1.46048961, -1.45229968, -1.44418849, -1.43615573,
       -1.42820106, -1.42032415, -1.41252463, -1.40480216, -1.39715638,
       -1.38958691, -1.38209338, -1.3746754 , -1.36733259, -1.36006454,
       -1.35287085, -1.34575112, -1.33870493, -1.33173185, -1.32483147,
       -1.31800335, -1.31124706, -1.30456215, -1.29794818, -1.29140469,
       -1.28493124, -1.27852737, -1.2721926 , -1.26592648, -1.25972853,
       -1.25359829, -1.24753527, -1.24153899, -1.23560897, -1.22974473,
       -1.22394577, -1.21821161, -1.21254175, -1.2069357 , -1.20139296,
       -1.19591304, -1.19049543, -1.18513964, -1.17984515, -1.17461147,
       -1.16943809, -1.16432451, -1.15927022, -1.15427471, -1.14933748,
       -1.14445802, -1.13963584, -1.1348704 , -1.13016122, -1.12550778,
       -1.12090958, -1.11636611, -1.11187687, -1.10744136, -1.10305907,
       -1.0987295 , -1.09445216, -1.09022653, -1.08605213, -1.08192845,
       -1.077855  , -1.0738313 , -1.06985684, -1.06593113, -1.0620537 ,
       -1.05822405, -1.0544417 , -1.05070616, -1.04701696, -1.04337363,
       -1.03977568, -1.03622264, -1.03271405, -1.02924943, -1.02582832,
       -1.02245026, -1.01911479, -1.01582146, -1.01256979, -1.00935937,
       -1.00618972, -1.0030604 , -0.99997097, -0.996921  , -0.99391004,
       -0.99093766, -0.98800344, -0.98510694, -0.98224774, -0.97942542])

interpEnergy = interp1d(logxvalues, logenergy)

def _energyNFW(r, rhos, rs):

    G = 4.1e-6

    x = r * rs ** -1

    logenergy_x = interpEnergy(np.log10(x))

    mass_s = 4*np.pi*rs**3*rhos
    velocity_squared = 4*np.pi*rs**2*rhos*G

    return 0.5*mass_s*velocity_squared*10**logenergy_x