import importlib
import KNN
import matplotlib

import  matplotlib.pylab

importlib.reload(KNN)

datingDataMat, datingLabels = KNN.file2matrix('datingTestSet.txt')

print(datingDataMat)

print (datingLabels[0:20])



