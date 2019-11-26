from sklearn import svm
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from pyod.models import abod
from pyod.models import iforest
from pyod.models import knn

#D = cardboard
#E = Plastic
#F = cardboard
#datasets
SetDEF = [[1.071e+08,2.043e+08,2.925e+08,2.277e+08,6.066e+08],
[5.310e+07,8.820e+07,1.224e+08,3.150e+07,-2.700e+07],
[5.940e+07,1.233e+08,1.071e+08,6.930e+07,1.197e+08],
[7.650e+07,1.368e+08,1.944e+08,1.917e+08,2.763e+08],
[6.840e+07,9.270e+07,2.106e+08,2.700e+08,2.286e+08],
[9.090e+07,1.494e+08,2.385e+08,3.510e+08,4.653e+08],
[7.740e+07,1.755e+08,1.809e+08,1.917e+08,2.259e+08],
[6.840e+07,9.360e+07,1.278e+08,1.440e+08,1.368e+08],
[6.570e+07,7.380e+07,2.637e+08,3.510e+08,1.557e+08],
[6.300e+07,1.539e+08,2.610e+08,2.025e+08,2.088e+08],
[9.360e+07,1.692e+08,2.682e+08,2.331e+08,4.527e+08],
[9.360e+07,1.584e+08,1.782e+08,2.097e+08,4.878e+08],
[8.370e+07,1.539e+08,1.692e+08,1.107e+08,2.358e+08],
[1.512e+08,2.610e+08,3.654e+08,0.000e+00,9.666e+08],
[9.270e+07,1.854e+08,2.853e+08,4.023e+08,3.312e+08],
[9.360e+07,1.449e+08,2.457e+08,2.178e+08,4.923e+08],
[8.550e+07,2.043e+08,2.196e+08,2.619e+08,3.663e+08],
[1.188e+08,1.908e+08,1.935e+08,1.215e+08,5.751e+08],
[1.359e+08,2.682e+08,3.213e+08,2.070e+08,7.659e+08],
[1.197e+08,2.502e+08,3.996e+08,0.000e+00,8.469e+08],
[9.000e+07,2.268e+08,3.816e+08,4.176e+08,6.255e+08],
[9.720e+07,1.449e+08,1.665e+08,1.755e+08,5.058e+08],
[7.110e+07,1.404e+08,1.134e+08,1.593e+08,1.584e+08],
[7.380e+07,1.188e+08,3.006e+08,3.465e+08,2.160e+08],
[7.020e+07,1.836e+08,3.096e+08,1.080e+08,4.149e+08],
[9.360e+07,1.260e+08,1.224e+08,7.380e+07,4.995e+08],
[7.920e+07,1.962e+08,3.735e+08,4.428e+08,3.456e+08],
[8.010e+07,1.629e+08,2.736e+08,4.824e+08,3.321e+08],
[6.120e+07,7.560e+07,1.143e+08,1.998e+08,9.900e+07],
[8.550e+07,9.360e+07,1.062e+08,7.290e+07,1.368e+08],
[7.830e+07,7.110e+07,7.560e+07,7.560e+07,4.563e+08],
[9.270e+07,1.521e+08,2.340e+08,1.476e+08,4.959e+08],
[8.460e+07,1.296e+08,1.818e+08,2.295e+08,5.301e+08],
[8.010e+07,1.827e+08,2.214e+08,2.493e+08,2.880e+08],
[5.760e+07,1.476e+08,2.610e+08,2.493e+08,9.990e+07],
[7.650e+07,1.485e+08,1.773e+08,2.700e+08,1.530e+08],
[8.640e+07,1.737e+08,2.151e+08,2.412e+08,3.321e+08],
[8.100e+07,1.899e+08,3.033e+08,4.428e+08,1.845e+08],
[6.930e+07,1.467e+08,2.286e+08,2.322e+08,1.683e+08],
[8.100e+07,1.557e+08,1.755e+08,2.196e+08,4.491e+08],
[9.630e+07,3.141e+08,5.229e+08,6.552e+08,5.553e+08],
[6.120e+07,8.820e+07,3.042e+08,1.602e+08,4.500e+07],
[8.100e+07,1.386e+08,1.989e+08,2.916e+08,1.629e+08],
[1.4670e+08,1.9440e+08,2.5380e+08,1.7550e+08,1.0251e+09],
[6.390e+07,1.152e+08,2.349e+08,3.762e+08,1.179e+08],
[1.134e+08,3.798e+08,5.445e+08,6.480e+08,3.465e+08],
[9.360e+07,1.701e+08,2.979e+08,2.646e+08,4.860e+08],
[8.640e+07,1.827e+08,3.060e+08,4.050e+08,5.103e+08],
[58500000.,83700000.,45000000.,16200000.,76500000.],
[8.910e+07,2.178e+08,3.636e+08,4.473e+08,4.059e+08],#end of set D
[1.215e+08,1.476e+08,1.647e+08,9.000e+07,6.282e+08],
[1.539e+08,2.340e+08,3.636e+08,0.000e+00,9.387e+08],
[8.91e+07,9.09e+07,7.74e+07,3.60e+07,3.15e+08],
[5.760e+07,5.130e+07,3.420e+07,0.000e+00,-1.449e+08],
[8.100e+07,1.071e+08,1.620e+08,1.206e+08,9.720e+07],
[1.224e+08,1.674e+08,2.682e+08,2.331e+08,-3.690e+07],
[71100000.,61200000.,57600000.,43200000.,22500000.],
[1.017e+08,1.512e+08,2.259e+08,2.259e+08,-9.990e+07],
[1.350e+08,2.079e+08,3.177e+08,3.825e+08,6.993e+08],
[9.090e+07,1.197e+08,1.512e+08,1.242e+08,3.069e+08],
[1.503e+08,2.547e+08,3.609e+08,3.375e+08,9.063e+08],
[1.206e+08,1.512e+08,1.890e+08,1.350e+08,-2.673e+08],
[1.053e+08,1.836e+08,2.700e+08,3.843e+08,-4.320e+07],
[9.720e+07,1.494e+08,2.322e+08,2.097e+08,-2.673e+08],
[7.740e+07,1.017e+08,1.836e+08,2.637e+08,-2.682e+08],
[7.290e+07,6.660e+07,5.940e+07,0.000e+00,-2.682e+08],
[1.260e+08,2.187e+08,4.374e+08,4.986e+08,8.190e+07],
[9.000e+07,9.360e+07,8.910e+07,1.800e+07,2.502e+08],
[51300000.,48600000.,55800000.,45000000.,-35100000.],
[9.900e+07,1.026e+08,1.278e+08,1.197e+08,2.313e+08],
[8.550e+07,1.188e+08,1.548e+08,1.053e+08,2.457e+08],
[1.152e+08,1.476e+08,1.908e+08,1.593e+08,5.265e+08],
[9.000e+07,6.480e+07,5.130e+07,3.600e+06,1.773e+08],
[9.450e+07,1.071e+08,2.232e+08,2.682e+08,-2.682e+08],
[1.440e+08,2.421e+08,3.690e+08,4.068e+08,-3.960e+07],
[8.370e+07,1.053e+08,1.503e+08,1.602e+08,1.908e+08],
[9.180e+07,2.169e+08,2.817e+08,3.024e+08,6.750e+07],
[1.332e+08,1.926e+08,2.556e+08,2.943e+08,6.399e+08],
[6.750e+07,5.760e+07,8.280e+07,1.800e+06,-1.413e+08],
[72000000.,73800000.,69300000.,9900000.,49500000.],
[2.880e+07,5.400e+06,2.970e+07,0.000e+00,-1.683e+08],
[1.053e+08,1.260e+08,1.395e+08,6.930e+07,4.662e+08],
[1.332e+08,1.818e+08,2.619e+08,2.493e+08,-1.719e+08],
[1.080e+08,1.224e+08,1.170e+08,8.190e+07,4.869e+08],
[9.180e+07,1.161e+08,1.710e+08,1.512e+08,-2.682e+08],
[8.820e+07,1.107e+08,1.944e+08,1.539e+08,-2.457e+08],
[7.380e+07,8.910e+07,1.206e+08,6.210e+07,9.360e+07],
[9.450e+07,1.557e+08,2.043e+08,1.836e+08,3.312e+08],
[1.449e+08,2.268e+08,3.294e+08,3.573e+08,8.793e+08],
[1.359e+08,1.512e+08,1.863e+08,1.602e+08,7.200e+08],
[1.125e+08,1.350e+08,1.575e+08,9.810e+07,5.058e+08],
[7.830e+07,8.370e+07,9.810e+07,4.860e+07,-2.682e+08],
[4.230e+07,1.620e+07,4.230e+07,1.206e+08,-1.089e+08],
[7.830e+07,8.640e+07,8.460e+07,1.980e+07,1.611e+08],
[1.179e+08,1.512e+08,1.944e+08,1.593e+08,5.589e+08],
[8.370e+07,1.260e+08,1.521e+08,1.287e+08,1.026e+08],
[9.180e+07,1.305e+08,1.494e+08,1.431e+08,3.087e+08],
[1.341e+08,1.791e+08,2.340e+08,1.998e+08,6.426e+08],
[9.450e+07,1.422e+08,2.196e+08,2.169e+08,2.781e+08],
[9.990e+07,1.710e+08,2.457e+08,3.024e+08,-1.917e+08], # end of set E
[1.242e+08,1.854e+08,2.547e+08,2.376e+08,6.831e+08],
[9.450e+07,1.206e+08,1.377e+08,7.920e+07,3.141e+08],
[58500000.,21600000.,7200000.,0.,-34200000.],
[8.82e+07,8.28e+07,7.47e+07,1.26e+07,2.43e+08],
[7.290e+07,1.980e+08,2.979e+08,2.196e+08,1.422e+08],
[68400000.,69300000.,69300000.,17100000.,90900000.],
[4.680e+07,1.629e+08,9.270e+07,0.000e+00,9.000e+05],
[7.830e+07,8.460e+07,6.930e+07,0.000e+00,2.097e+08],
[8.55e+07,8.64e+07,8.46e+07,3.96e+07,2.25e+08],
[51300000.,43200000.,27900000.,0.,-31500000.],
[7.830e+07,9.090e+07,1.062e+08,1.269e+08,-2.664e+08],
[42300000.,36900000.,43200000.,18000000.,-51300000.],
[1.269e+08,2.529e+08,4.041e+08,5.427e+08,1.737e+08],
[39600000.,10800000.,-900000.,0.,-98100000.],
[6.930e+07,7.380e+07,9.900e+07,9.810e+07,-2.205e+08],
[44100000.,27000000.,21600000.,0.,-21600000.],
[63000000.,26100000.,1800000.,0.,32400000.],
[8.640e+07,2.313e+08,2.943e+08,3.312e+08,3.654e+08],
[5.580e+07,6.390e+07,9.540e+07,1.377e+08,3.600e+06],
[66600000.,81900000.,79200000.,44100000.,5400000.],
[39600000.,26100000.,27900000.,0.,-39600000.],
[1.161e+08,2.178e+08,3.357e+08,3.312e+08,6.327e+08],
[7.560e+07,7.380e+07,7.290e+07,7.200e+06,1.719e+08],
[1.161e+08,2.178e+08,3.357e+08,3.312e+08,6.327e+08],
[54900000.,51300000.,43200000.,0.,30600000.],
[8.730e+07,1.089e+08,1.233e+08,6.300e+07,3.132e+08],
[60300000.,16200000.,-4500000.,0.,9000000.],
[8.280e+07,9.720e+07,1.062e+08,5.850e+07,2.475e+08],
[44100000.,32400000.,30600000.,0.,-45900000.],
[4.230e+07,5.220e+07,9.720e+07,1.539e+08,8.460e+07],
[7.560e+07,8.730e+07,7.380e+07,5.400e+06,2.421e+08],
[1.017e+08,2.367e+08,3.438e+08,3.177e+08,3.393e+08],
[7.380e+07,5.580e+07,4.230e+07,0.000e+00,1.134e+08],
[9.000e+07,9.360e+07,1.224e+08,7.380e+07,3.384e+08],
[6.480e+07,8.910e+07,1.143e+08,1.764e+08,9.630e+07],
[67500000.,57600000.,51300000.,900000.,91800000.],
[8.730e+07,6.660e+07,7.830e+07,1.170e+07,3.132e+08],
[8.820e+07,1.017e+08,9.270e+07,3.960e+07,2.349e+08],
[9.990e+07,1.620e+08,2.007e+08,1.629e+08,4.275e+08],
[9.720e+07,1.494e+08,2.196e+08,2.655e+08,4.041e+08],
[1.017e+08,1.836e+08,1.944e+08,8.190e+07,6.183e+08],
[9.810e+07,1.773e+08,3.006e+08,3.618e+08,9.630e+07],
[1.035e+08,2.547e+08,3.753e+08,4.122e+08,6.021e+08],
[62100000.,51300000.,54000000.,0.,27000000.],
[5.670e+07,9.360e+07,1.836e+08,1.710e+07,-1.593e+08],
[62100000.,90900000.,63900000.,0.,25200000.],
[1.890e+07,7.200e+06,-2.700e+06,2.520e+07,-2.682e+08],
[1.197e+08,2.934e+08,4.248e+08,4.590e+08,7.227e+08],
[1.431e+08,3.078e+08,5.544e+08,7.218e+08,3.600e+07],
[6.120e+07,4.770e+07,4.860e+07,3.600e+06,-1.071e+08]]#end of set F


SetDE = [[1.071e+08,2.043e+08,2.925e+08,2.277e+08,6.066e+08],
[5.310e+07,8.820e+07,1.224e+08,3.150e+07,-2.700e+07],
[5.940e+07,1.233e+08,1.071e+08,6.930e+07,1.197e+08],
[7.650e+07,1.368e+08,1.944e+08,1.917e+08,2.763e+08],
[6.840e+07,9.270e+07,2.106e+08,2.700e+08,2.286e+08],
[9.090e+07,1.494e+08,2.385e+08,3.510e+08,4.653e+08],
[7.740e+07,1.755e+08,1.809e+08,1.917e+08,2.259e+08],
[6.840e+07,9.360e+07,1.278e+08,1.440e+08,1.368e+08],
[6.570e+07,7.380e+07,2.637e+08,3.510e+08,1.557e+08],
[6.300e+07,1.539e+08,2.610e+08,2.025e+08,2.088e+08],
[9.360e+07,1.692e+08,2.682e+08,2.331e+08,4.527e+08],
[9.360e+07,1.584e+08,1.782e+08,2.097e+08,4.878e+08],
[8.370e+07,1.539e+08,1.692e+08,1.107e+08,2.358e+08],
[1.512e+08,2.610e+08,3.654e+08,0.000e+00,9.666e+08],
[9.270e+07,1.854e+08,2.853e+08,4.023e+08,3.312e+08],
[9.360e+07,1.449e+08,2.457e+08,2.178e+08,4.923e+08],
[8.550e+07,2.043e+08,2.196e+08,2.619e+08,3.663e+08],
[1.188e+08,1.908e+08,1.935e+08,1.215e+08,5.751e+08],
[1.359e+08,2.682e+08,3.213e+08,2.070e+08,7.659e+08],
[1.197e+08,2.502e+08,3.996e+08,0.000e+00,8.469e+08],
[9.000e+07,2.268e+08,3.816e+08,4.176e+08,6.255e+08],
[9.720e+07,1.449e+08,1.665e+08,1.755e+08,5.058e+08],
[7.110e+07,1.404e+08,1.134e+08,1.593e+08,1.584e+08],
[7.380e+07,1.188e+08,3.006e+08,3.465e+08,2.160e+08],
[7.020e+07,1.836e+08,3.096e+08,1.080e+08,4.149e+08],
[9.360e+07,1.260e+08,1.224e+08,7.380e+07,4.995e+08],
[7.920e+07,1.962e+08,3.735e+08,4.428e+08,3.456e+08],
[8.010e+07,1.629e+08,2.736e+08,4.824e+08,3.321e+08],
[6.120e+07,7.560e+07,1.143e+08,1.998e+08,9.900e+07],
[8.550e+07,9.360e+07,1.062e+08,7.290e+07,1.368e+08],
[7.830e+07,7.110e+07,7.560e+07,7.560e+07,4.563e+08],
[9.270e+07,1.521e+08,2.340e+08,1.476e+08,4.959e+08],
[8.460e+07,1.296e+08,1.818e+08,2.295e+08,5.301e+08],
[8.010e+07,1.827e+08,2.214e+08,2.493e+08,2.880e+08],
[5.760e+07,1.476e+08,2.610e+08,2.493e+08,9.990e+07],
[7.650e+07,1.485e+08,1.773e+08,2.700e+08,1.530e+08],
[8.640e+07,1.737e+08,2.151e+08,2.412e+08,3.321e+08],
[8.100e+07,1.899e+08,3.033e+08,4.428e+08,1.845e+08],
[6.930e+07,1.467e+08,2.286e+08,2.322e+08,1.683e+08],
[8.100e+07,1.557e+08,1.755e+08,2.196e+08,4.491e+08],
[9.630e+07,3.141e+08,5.229e+08,6.552e+08,5.553e+08],
[6.120e+07,8.820e+07,3.042e+08,1.602e+08,4.500e+07],
[8.100e+07,1.386e+08,1.989e+08,2.916e+08,1.629e+08],
[1.4670e+08,1.9440e+08,2.5380e+08,1.7550e+08,1.0251e+09],
[6.390e+07,1.152e+08,2.349e+08,3.762e+08,1.179e+08],
[1.134e+08,3.798e+08,5.445e+08,6.480e+08,3.465e+08],
[9.360e+07,1.701e+08,2.979e+08,2.646e+08,4.860e+08],
[8.640e+07,1.827e+08,3.060e+08,4.050e+08,5.103e+08],
[58500000.,83700000.,45000000.,16200000.,76500000.],
[8.910e+07,2.178e+08,3.636e+08,4.473e+08,4.059e+08],#end of set D
[1.215e+08,1.476e+08,1.647e+08,9.000e+07,6.282e+08],
[1.539e+08,2.340e+08,3.636e+08,0.000e+00,9.387e+08],
[8.91e+07,9.09e+07,7.74e+07,3.60e+07,3.15e+08],
[5.760e+07,5.130e+07,3.420e+07,0.000e+00,-1.449e+08],
[8.100e+07,1.071e+08,1.620e+08,1.206e+08,9.720e+07],
[1.224e+08,1.674e+08,2.682e+08,2.331e+08,-3.690e+07],
[71100000.,61200000.,57600000.,43200000.,22500000.],
[1.017e+08,1.512e+08,2.259e+08,2.259e+08,-9.990e+07],
[1.350e+08,2.079e+08,3.177e+08,3.825e+08,6.993e+08],
[9.090e+07,1.197e+08,1.512e+08,1.242e+08,3.069e+08],
[1.503e+08,2.547e+08,3.609e+08,3.375e+08,9.063e+08],
[1.206e+08,1.512e+08,1.890e+08,1.350e+08,-2.673e+08],
[1.053e+08,1.836e+08,2.700e+08,3.843e+08,-4.320e+07],
[9.720e+07,1.494e+08,2.322e+08,2.097e+08,-2.673e+08],
[7.740e+07,1.017e+08,1.836e+08,2.637e+08,-2.682e+08],
[7.290e+07,6.660e+07,5.940e+07,0.000e+00,-2.682e+08],
[1.260e+08,2.187e+08,4.374e+08,4.986e+08,8.190e+07],
[9.000e+07,9.360e+07,8.910e+07,1.800e+07,2.502e+08],
[51300000.,48600000.,55800000.,45000000.,-35100000.],
[9.900e+07,1.026e+08,1.278e+08,1.197e+08,2.313e+08],
[8.550e+07,1.188e+08,1.548e+08,1.053e+08,2.457e+08],
[1.152e+08,1.476e+08,1.908e+08,1.593e+08,5.265e+08],
[9.000e+07,6.480e+07,5.130e+07,3.600e+06,1.773e+08],
[9.450e+07,1.071e+08,2.232e+08,2.682e+08,-2.682e+08],
[1.440e+08,2.421e+08,3.690e+08,4.068e+08,-3.960e+07],
[8.370e+07,1.053e+08,1.503e+08,1.602e+08,1.908e+08],
[9.180e+07,2.169e+08,2.817e+08,3.024e+08,6.750e+07],
[1.332e+08,1.926e+08,2.556e+08,2.943e+08,6.399e+08],
[6.750e+07,5.760e+07,8.280e+07,1.800e+06,-1.413e+08],
[72000000.,73800000.,69300000.,9900000.,49500000.],
[2.880e+07,5.400e+06,2.970e+07,0.000e+00,-1.683e+08],
[1.053e+08,1.260e+08,1.395e+08,6.930e+07,4.662e+08],
[1.332e+08,1.818e+08,2.619e+08,2.493e+08,-1.719e+08],
[1.080e+08,1.224e+08,1.170e+08,8.190e+07,4.869e+08],
[9.180e+07,1.161e+08,1.710e+08,1.512e+08,-2.682e+08],
[8.820e+07,1.107e+08,1.944e+08,1.539e+08,-2.457e+08],
[7.380e+07,8.910e+07,1.206e+08,6.210e+07,9.360e+07],
[9.450e+07,1.557e+08,2.043e+08,1.836e+08,3.312e+08],
[1.449e+08,2.268e+08,3.294e+08,3.573e+08,8.793e+08],
[1.359e+08,1.512e+08,1.863e+08,1.602e+08,7.200e+08],
[1.125e+08,1.350e+08,1.575e+08,9.810e+07,5.058e+08],
[7.830e+07,8.370e+07,9.810e+07,4.860e+07,-2.682e+08],
[4.230e+07,1.620e+07,4.230e+07,1.206e+08,-1.089e+08],
[7.830e+07,8.640e+07,8.460e+07,1.980e+07,1.611e+08],
[1.179e+08,1.512e+08,1.944e+08,1.593e+08,5.589e+08],
[8.370e+07,1.260e+08,1.521e+08,1.287e+08,1.026e+08],
[9.180e+07,1.305e+08,1.494e+08,1.431e+08,3.087e+08],
[1.341e+08,1.791e+08,2.340e+08,1.998e+08,6.426e+08],
[9.450e+07,1.422e+08,2.196e+08,2.169e+08,2.781e+08],
[9.990e+07,1.710e+08,2.457e+08,3.024e+08,-1.917e+08]] # end of set E

SetEF = [[1.215e+08,1.476e+08,1.647e+08,9.000e+07,6.282e+08],
[1.539e+08,2.340e+08,3.636e+08,0.000e+00,9.387e+08],
[8.91e+07,9.09e+07,7.74e+07,3.60e+07,3.15e+08],
[5.760e+07,5.130e+07,3.420e+07,0.000e+00,-1.449e+08],
[8.100e+07,1.071e+08,1.620e+08,1.206e+08,9.720e+07],
[1.224e+08,1.674e+08,2.682e+08,2.331e+08,-3.690e+07],
[71100000.,61200000.,57600000.,43200000.,22500000.],
[1.017e+08,1.512e+08,2.259e+08,2.259e+08,-9.990e+07],
[1.350e+08,2.079e+08,3.177e+08,3.825e+08,6.993e+08],
[9.090e+07,1.197e+08,1.512e+08,1.242e+08,3.069e+08],
[1.503e+08,2.547e+08,3.609e+08,3.375e+08,9.063e+08],
[1.206e+08,1.512e+08,1.890e+08,1.350e+08,-2.673e+08],
[1.053e+08,1.836e+08,2.700e+08,3.843e+08,-4.320e+07],
[9.720e+07,1.494e+08,2.322e+08,2.097e+08,-2.673e+08],
[7.740e+07,1.017e+08,1.836e+08,2.637e+08,-2.682e+08],
[7.290e+07,6.660e+07,5.940e+07,0.000e+00,-2.682e+08],
[1.260e+08,2.187e+08,4.374e+08,4.986e+08,8.190e+07],
[9.000e+07,9.360e+07,8.910e+07,1.800e+07,2.502e+08],
[51300000.,48600000.,55800000.,45000000.,-35100000.],
[9.900e+07,1.026e+08,1.278e+08,1.197e+08,2.313e+08],
[8.550e+07,1.188e+08,1.548e+08,1.053e+08,2.457e+08],
[1.152e+08,1.476e+08,1.908e+08,1.593e+08,5.265e+08],
[9.000e+07,6.480e+07,5.130e+07,3.600e+06,1.773e+08],
[9.450e+07,1.071e+08,2.232e+08,2.682e+08,-2.682e+08],
[1.440e+08,2.421e+08,3.690e+08,4.068e+08,-3.960e+07],
[8.370e+07,1.053e+08,1.503e+08,1.602e+08,1.908e+08],
[9.180e+07,2.169e+08,2.817e+08,3.024e+08,6.750e+07],
[1.332e+08,1.926e+08,2.556e+08,2.943e+08,6.399e+08],
[6.750e+07,5.760e+07,8.280e+07,1.800e+06,-1.413e+08],
[72000000.,73800000.,69300000.,9900000.,49500000.],
[2.880e+07,5.400e+06,2.970e+07,0.000e+00,-1.683e+08],
[1.053e+08,1.260e+08,1.395e+08,6.930e+07,4.662e+08],
[1.332e+08,1.818e+08,2.619e+08,2.493e+08,-1.719e+08],
[1.080e+08,1.224e+08,1.170e+08,8.190e+07,4.869e+08],
[9.180e+07,1.161e+08,1.710e+08,1.512e+08,-2.682e+08],
[8.820e+07,1.107e+08,1.944e+08,1.539e+08,-2.457e+08],
[7.380e+07,8.910e+07,1.206e+08,6.210e+07,9.360e+07],
[9.450e+07,1.557e+08,2.043e+08,1.836e+08,3.312e+08],
[1.449e+08,2.268e+08,3.294e+08,3.573e+08,8.793e+08],
[1.359e+08,1.512e+08,1.863e+08,1.602e+08,7.200e+08],
[1.125e+08,1.350e+08,1.575e+08,9.810e+07,5.058e+08],
[7.830e+07,8.370e+07,9.810e+07,4.860e+07,-2.682e+08],
[4.230e+07,1.620e+07,4.230e+07,1.206e+08,-1.089e+08],
[7.830e+07,8.640e+07,8.460e+07,1.980e+07,1.611e+08],
[1.179e+08,1.512e+08,1.944e+08,1.593e+08,5.589e+08],
[8.370e+07,1.260e+08,1.521e+08,1.287e+08,1.026e+08],
[9.180e+07,1.305e+08,1.494e+08,1.431e+08,3.087e+08],
[1.341e+08,1.791e+08,2.340e+08,1.998e+08,6.426e+08],
[9.450e+07,1.422e+08,2.196e+08,2.169e+08,2.781e+08],
[9.990e+07,1.710e+08,2.457e+08,3.024e+08,-1.917e+08], # end of set E
[1.242e+08,1.854e+08,2.547e+08,2.376e+08,6.831e+08],
[9.450e+07,1.206e+08,1.377e+08,7.920e+07,3.141e+08],
[58500000.,21600000.,7200000.,0.,-34200000.],
[8.82e+07,8.28e+07,7.47e+07,1.26e+07,2.43e+08],
[7.290e+07,1.980e+08,2.979e+08,2.196e+08,1.422e+08],
[68400000.,69300000.,69300000.,17100000.,90900000.],
[4.680e+07,1.629e+08,9.270e+07,0.000e+00,9.000e+05],
[7.830e+07,8.460e+07,6.930e+07,0.000e+00,2.097e+08],
[8.55e+07,8.64e+07,8.46e+07,3.96e+07,2.25e+08],
[51300000.,43200000.,27900000.,0.,-31500000.],
[7.830e+07,9.090e+07,1.062e+08,1.269e+08,-2.664e+08],
[42300000.,36900000.,43200000.,18000000.,-51300000.],
[1.269e+08,2.529e+08,4.041e+08,5.427e+08,1.737e+08],
[39600000.,10800000.,-900000.,0.,-98100000.],
[6.930e+07,7.380e+07,9.900e+07,9.810e+07,-2.205e+08],
[44100000.,27000000.,21600000.,0.,-21600000.],
[63000000.,26100000.,1800000.,0.,32400000.],
[8.640e+07,2.313e+08,2.943e+08,3.312e+08,3.654e+08],
[5.580e+07,6.390e+07,9.540e+07,1.377e+08,3.600e+06],
[66600000.,81900000.,79200000.,44100000.,5400000.],
[39600000.,26100000.,27900000.,0.,-39600000.],
[1.161e+08,2.178e+08,3.357e+08,3.312e+08,6.327e+08],
[7.560e+07,7.380e+07,7.290e+07,7.200e+06,1.719e+08],
[1.161e+08,2.178e+08,3.357e+08,3.312e+08,6.327e+08],
[54900000.,51300000.,43200000.,0.,30600000.],
[8.730e+07,1.089e+08,1.233e+08,6.300e+07,3.132e+08],
[60300000.,16200000.,-4500000.,0.,9000000.],
[8.280e+07,9.720e+07,1.062e+08,5.850e+07,2.475e+08],
[44100000.,32400000.,30600000.,0.,-45900000.],
[4.230e+07,5.220e+07,9.720e+07,1.539e+08,8.460e+07],
[7.560e+07,8.730e+07,7.380e+07,5.400e+06,2.421e+08],
[1.017e+08,2.367e+08,3.438e+08,3.177e+08,3.393e+08],
[7.380e+07,5.580e+07,4.230e+07,0.000e+00,1.134e+08],
[9.000e+07,9.360e+07,1.224e+08,7.380e+07,3.384e+08],
[6.480e+07,8.910e+07,1.143e+08,1.764e+08,9.630e+07],
[67500000.,57600000.,51300000.,900000.,91800000.],
[8.730e+07,6.660e+07,7.830e+07,1.170e+07,3.132e+08],
[8.820e+07,1.017e+08,9.270e+07,3.960e+07,2.349e+08],
[9.990e+07,1.620e+08,2.007e+08,1.629e+08,4.275e+08],
[9.720e+07,1.494e+08,2.196e+08,2.655e+08,4.041e+08],
[1.017e+08,1.836e+08,1.944e+08,8.190e+07,6.183e+08],
[9.810e+07,1.773e+08,3.006e+08,3.618e+08,9.630e+07],
[1.035e+08,2.547e+08,3.753e+08,4.122e+08,6.021e+08],
[62100000.,51300000.,54000000.,0.,27000000.],
[5.670e+07,9.360e+07,1.836e+08,1.710e+07,-1.593e+08],
[62100000.,90900000.,63900000.,0.,25200000.],
[1.890e+07,7.200e+06,-2.700e+06,2.520e+07,-2.682e+08],
[1.197e+08,2.934e+08,4.248e+08,4.590e+08,7.227e+08],
[1.431e+08,3.078e+08,5.544e+08,7.218e+08,3.600e+07],
[6.120e+07,4.770e+07,4.860e+07,3.600e+06,-1.071e+08]]#end of set F

SetDF = [[1.071e+08,2.043e+08,2.925e+08,2.277e+08,6.066e+08],
[5.310e+07,8.820e+07,1.224e+08,3.150e+07,-2.700e+07],
[5.940e+07,1.233e+08,1.071e+08,6.930e+07,1.197e+08],
[7.650e+07,1.368e+08,1.944e+08,1.917e+08,2.763e+08],
[6.840e+07,9.270e+07,2.106e+08,2.700e+08,2.286e+08],
[9.090e+07,1.494e+08,2.385e+08,3.510e+08,4.653e+08],
[7.740e+07,1.755e+08,1.809e+08,1.917e+08,2.259e+08],
[6.840e+07,9.360e+07,1.278e+08,1.440e+08,1.368e+08],
[6.570e+07,7.380e+07,2.637e+08,3.510e+08,1.557e+08],
[6.300e+07,1.539e+08,2.610e+08,2.025e+08,2.088e+08],
[9.360e+07,1.692e+08,2.682e+08,2.331e+08,4.527e+08],
[9.360e+07,1.584e+08,1.782e+08,2.097e+08,4.878e+08],
[8.370e+07,1.539e+08,1.692e+08,1.107e+08,2.358e+08],
[1.512e+08,2.610e+08,3.654e+08,0.000e+00,9.666e+08],
[9.270e+07,1.854e+08,2.853e+08,4.023e+08,3.312e+08],
[9.360e+07,1.449e+08,2.457e+08,2.178e+08,4.923e+08],
[8.550e+07,2.043e+08,2.196e+08,2.619e+08,3.663e+08],
[1.188e+08,1.908e+08,1.935e+08,1.215e+08,5.751e+08],
[1.359e+08,2.682e+08,3.213e+08,2.070e+08,7.659e+08],
[1.197e+08,2.502e+08,3.996e+08,0.000e+00,8.469e+08],
[9.000e+07,2.268e+08,3.816e+08,4.176e+08,6.255e+08],
[9.720e+07,1.449e+08,1.665e+08,1.755e+08,5.058e+08],
[7.110e+07,1.404e+08,1.134e+08,1.593e+08,1.584e+08],
[7.380e+07,1.188e+08,3.006e+08,3.465e+08,2.160e+08],
[7.020e+07,1.836e+08,3.096e+08,1.080e+08,4.149e+08],
[9.360e+07,1.260e+08,1.224e+08,7.380e+07,4.995e+08],
[7.920e+07,1.962e+08,3.735e+08,4.428e+08,3.456e+08],
[8.010e+07,1.629e+08,2.736e+08,4.824e+08,3.321e+08],
[6.120e+07,7.560e+07,1.143e+08,1.998e+08,9.900e+07],
[8.550e+07,9.360e+07,1.062e+08,7.290e+07,1.368e+08],
[7.830e+07,7.110e+07,7.560e+07,7.560e+07,4.563e+08],
[9.270e+07,1.521e+08,2.340e+08,1.476e+08,4.959e+08],
[8.460e+07,1.296e+08,1.818e+08,2.295e+08,5.301e+08],
[8.010e+07,1.827e+08,2.214e+08,2.493e+08,2.880e+08],
[5.760e+07,1.476e+08,2.610e+08,2.493e+08,9.990e+07],
[7.650e+07,1.485e+08,1.773e+08,2.700e+08,1.530e+08],
[8.640e+07,1.737e+08,2.151e+08,2.412e+08,3.321e+08],
[8.100e+07,1.899e+08,3.033e+08,4.428e+08,1.845e+08],
[6.930e+07,1.467e+08,2.286e+08,2.322e+08,1.683e+08],
[8.100e+07,1.557e+08,1.755e+08,2.196e+08,4.491e+08],
[9.630e+07,3.141e+08,5.229e+08,6.552e+08,5.553e+08],
[6.120e+07,8.820e+07,3.042e+08,1.602e+08,4.500e+07],
[8.100e+07,1.386e+08,1.989e+08,2.916e+08,1.629e+08],
[1.4670e+08,1.9440e+08,2.5380e+08,1.7550e+08,1.0251e+09],
[6.390e+07,1.152e+08,2.349e+08,3.762e+08,1.179e+08],
[1.134e+08,3.798e+08,5.445e+08,6.480e+08,3.465e+08],
[9.360e+07,1.701e+08,2.979e+08,2.646e+08,4.860e+08],
[8.640e+07,1.827e+08,3.060e+08,4.050e+08,5.103e+08],
[58500000.,83700000.,45000000.,16200000.,76500000.],
[8.910e+07,2.178e+08,3.636e+08,4.473e+08,4.059e+08], #end of set D
[1.242e+08,1.854e+08,2.547e+08,2.376e+08,6.831e+08],
[9.450e+07,1.206e+08,1.377e+08,7.920e+07,3.141e+08],
[58500000.,21600000.,7200000.,0.,-34200000.],
[8.82e+07,8.28e+07,7.47e+07,1.26e+07,2.43e+08],
[7.290e+07,1.980e+08,2.979e+08,2.196e+08,1.422e+08],
[68400000.,69300000.,69300000.,17100000.,90900000.],
[4.680e+07,1.629e+08,9.270e+07,0.000e+00,9.000e+05],
[7.830e+07,8.460e+07,6.930e+07,0.000e+00,2.097e+08],
[8.55e+07,8.64e+07,8.46e+07,3.96e+07,2.25e+08],
[51300000.,43200000.,27900000.,0.,-31500000.],
[7.830e+07,9.090e+07,1.062e+08,1.269e+08,-2.664e+08],
[42300000.,36900000.,43200000.,18000000.,-51300000.],
[1.269e+08,2.529e+08,4.041e+08,5.427e+08,1.737e+08],
[39600000.,10800000.,-900000.,0.,-98100000.],
[6.930e+07,7.380e+07,9.900e+07,9.810e+07,-2.205e+08],
[44100000.,27000000.,21600000.,0.,-21600000.],
[63000000.,26100000.,1800000.,0.,32400000.],
[8.640e+07,2.313e+08,2.943e+08,3.312e+08,3.654e+08],
[5.580e+07,6.390e+07,9.540e+07,1.377e+08,3.600e+06],
[66600000.,81900000.,79200000.,44100000.,5400000.],
[39600000.,26100000.,27900000.,0.,-39600000.],
[1.161e+08,2.178e+08,3.357e+08,3.312e+08,6.327e+08],
[7.560e+07,7.380e+07,7.290e+07,7.200e+06,1.719e+08],
[1.161e+08,2.178e+08,3.357e+08,3.312e+08,6.327e+08],
[54900000.,51300000.,43200000.,0.,30600000.],
[8.730e+07,1.089e+08,1.233e+08,6.300e+07,3.132e+08],
[60300000.,16200000.,-4500000.,0.,9000000.],
[8.280e+07,9.720e+07,1.062e+08,5.850e+07,2.475e+08],
[44100000.,32400000.,30600000.,0.,-45900000.],
[4.230e+07,5.220e+07,9.720e+07,1.539e+08,8.460e+07],
[7.560e+07,8.730e+07,7.380e+07,5.400e+06,2.421e+08],
[1.017e+08,2.367e+08,3.438e+08,3.177e+08,3.393e+08],
[7.380e+07,5.580e+07,4.230e+07,0.000e+00,1.134e+08],
[9.000e+07,9.360e+07,1.224e+08,7.380e+07,3.384e+08],
[6.480e+07,8.910e+07,1.143e+08,1.764e+08,9.630e+07],
[67500000.,57600000.,51300000.,900000.,91800000.],
[8.730e+07,6.660e+07,7.830e+07,1.170e+07,3.132e+08],
[8.820e+07,1.017e+08,9.270e+07,3.960e+07,2.349e+08],
[9.990e+07,1.620e+08,2.007e+08,1.629e+08,4.275e+08],
[9.720e+07,1.494e+08,2.196e+08,2.655e+08,4.041e+08],
[1.017e+08,1.836e+08,1.944e+08,8.190e+07,6.183e+08],
[9.810e+07,1.773e+08,3.006e+08,3.618e+08,9.630e+07],
[1.035e+08,2.547e+08,3.753e+08,4.122e+08,6.021e+08],
[62100000.,51300000.,54000000.,0.,27000000.],
[5.670e+07,9.360e+07,1.836e+08,1.710e+07,-1.593e+08],
[62100000.,90900000.,63900000.,0.,25200000.],
[1.890e+07,7.200e+06,-2.700e+06,2.520e+07,-2.682e+08],
[1.197e+08,2.934e+08,4.248e+08,4.590e+08,7.227e+08],
[1.431e+08,3.078e+08,5.544e+08,7.218e+08,3.600e+07],
[6.120e+07,4.770e+07,4.860e+07,3.600e+06,-1.071e+08]] #end of set F


expectedV1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
              2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

expectedOvA1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
              2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
              2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

expectedOvA2 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
              1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
              2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

expectedOvA3 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
              2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
              1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

expectedDEF = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
              2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
              3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]


        
#leave one out cross validation
def loocv(dataset,expectedValues,classifier,scale,minimum,maximum,printResults):
    X = np.array(dataset)
    y = np.array(expectedValues)
    clf = classifier
    results = []
    misses = 0
    miss1 = 0
    miss2 = 0
    miss3 = 0

    #scalling data
    if(scale == True):
        min_max_scaler = preprocessing.MinMaxScaler(feature_range =(minimum,maximum))
        X = min_max_scaler.fit_transform(X)

    #performing loocv
    for x in range(len(X)):
        A = np.delete(X,x,0)
        b = np.delete(y,x)
        clf.fit(A,b)
        prediction = clf.predict([X[x]])
        if(prediction[0]!=y[x]):
            if(y[x] == 1):
                miss1 += 1
            elif(y[x] == 2):
                miss2 +=1
            else:
                miss3 +=1
            misses+=1
        results.append(prediction[0])

    if(printResults):
        print("********************************************************************")
        print("expected: " + str(expectedValues))
        print("outcome: " + str(results))
        print("number of correct classifications " + str(len(X)-misses) + "/" + str(len(X)))
        print("misclassified 1's: " + str(miss1))
        print("misclassified 2's: " + str(miss2))
        print("misclassified 3's: " + str(miss3))

    return results, misses, miss1, miss2

def majorityVote(dataset,expectedValues,classifiers,scale,minimum,maximum):
    #classifiers voting
    votes = []
    for c in classifiers:
        votes.append(loocv(dataset,expectedValues,c,scale,minimum,maximum,False)[0])


    #tallying votes
    subvotes = []
    majority = []
    for col in range(len(votes[0])):
        subvotes.clear()
        count1 = 0
        count2 = 0
        for row in range(len(classifiers)):
            subvotes.append(votes[row][col])
        for x in subvotes:
            if x == 1:
                count1 += 1
            else:
                count2 += 1
        if count1 > count2:
            majority.append(1)
        elif count2 > count1:
            majority.append(2)
        else:
            majority.append(0)

    misses = 0
    for i in range(len(majority)):
        if(majority[i] != expectedValues[i]):
            misses+=1

    print("********************************************************************")
    for x in range(len(classifiers)):
        print("classifier " + str(x) + " votes:" + str(votes[x]))
    print("Majority votes: " + str(majority))
    print("Expected: " + str(expectedValues))
    print("Correctly Classified: " + str(len(expectedValues)-misses) + "/" + str(len(expectedValues)))
    return misses, len(expectedValues)-misses


def detectOutliers(data,detector):
    # Angle base outlier detection using pyod module
    outliers = 0
    X = np.array(data)
    detector.fit(X)
    predictions = detector.predict(X)
    for x in predictions:
        if(x == 1):
            outliers +=1

    print("number of outliers: " + str(outliers))
    print(predictions)



#machine learning parameters
high = 1
low = -1
scale = True
svm1 = svm.SVC( kernel = "rbf", decision_function_shape='ovr', gamma = "scale", C = 100) #creating svm object
rf = RandomForestClassifier(n_estimators=10,random_state=10) #creating rf object
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 3), random_state=1) #creating mlp object
clfs = [rf,svm1,mlp]
clf = rf

#outlier detectors
angleBased = abod.ABOD(method="fast")
isolationForrest = iforest.IForest(n_estimators=100,behaviour="new")
kNearestNeighbors = knn.KNN(method="median")
detector = kNearestNeighbors


#Todo confusion matrix plotting
#remove outliers
#only focus on D vs Rest, and E vs F
#do majority votes give best cases or single classifier

'''
#detecting outliers
print("outliers in set D")
#detectOutliers(SetDEF[:50],detector)
print("outliers in set E")
#detectOutliers(SetDEF[50:100],detector)
print("outliers in set F")
#detectOutliers(SetDEF[100:150],detector)
'''



#Majority vote predictions
print("D vs Rest")
majorityVote(SetDEF,expectedOvA1,clfs,scale,low,high)

print("\nE vs Rest")
majorityVote(SetDEF,expectedOvA2,clfs,scale,low,high)

print("\nF vs Rest")
majorityVote(SetDEF,expectedOvA3,clfs,scale,low,high)

print("\nD vs E")
majorityVote(SetDE,expectedV1,clfs,scale,low,high)

print("\nE vs F")
majorityVote(SetEF,expectedV1,clfs,scale,low,high)

print("\nD vs F")
majorityVote(SetDF,expectedV1,clfs,scale,low,high)

"""
#single model predictions
#D vs E vs F MLP
loocv(SetDEF,expectedDEF,mlp,scale,low,high,True)

#D vs E vs F rf
loocv(SetDEF,expectedDEF,rf,scale,low,high,True)

#D vs Rest
print("Classifying D")
loocv(SetDEF,expectedOvA1,clf,scale,low,high,True)

#E vs Rest
print("Classifying E")
loocv(SetDEF,expectedOvA2,clf,scale,low,high,True)

#F vs Rest
print("Classifying F")
loocv(SetDEF,expectedOvA3,clf,scale,low,high,True)

#D vs E
print("Classifying D vs E")
loocv(SetDE,expectedV1,clf,scale,low,high,True)

#E vs F
print("Classifying E vs F")
loocv(SetEF,expectedV1,clf,scale,low,high,True)

#D vs F
print("Classifying D vs f")
loocv(SetDF,expectedV1,clf,scale,low,high,True)
'''

#try removing different combinations of features
#try different decision functions

"""




