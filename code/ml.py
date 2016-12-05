import numpy as np
import cPickle as pickle
from sklearn.linear_model import LinearRegression
import pdb
from sklearn.metrics import mean_squared_error
from math import sqrt


def loadData():
	gfeat = pickle.load(open('../githubfeatures.p', 'rb'))
	lfeat = pickle.load(open('../data/linkedinfeat.p', 'rb'))
	xsamp = []
	ysamp = []
	with open('../data/profilesalaries2.txt', 'r') as f1:
		for line in f1:
			uid, salary = line.rstrip('\n').split(',')
			salary = int(salary)
			xsamp.append(lfeat[uid][4:])
			ysamp.append(salary)

	#pdb.set_trace()
	c = int(0.8*(len(xsamp)))
	xtrain = xsamp[:c]
	ytrain = ysamp[:c]
	xtest = xsamp[c:]
	ytest = ysamp[c:]

	return xtrain, ytrain, xtest, ytest

xtrain, ytrain, xtest, ytest = loadData()


regr = LinearRegression()
regr.fit(xtrain, ytrain)
ypred = regr.predict(xtest)
rms = sqrt(mean_squared_error(ytest, ypred))
print rms
