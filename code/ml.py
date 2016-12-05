import numpy as np
import cPickle as pickle
from sklearn import linear_model
import pdb
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
from random import random
import statsmodels.api as smapi
from statsmodels.formula.api import ols
import statsmodels.graphics as smgraphics
from sklearn.metrics import r2_score


def loadData():
	gfeat = pickle.load(open('../githubfeatures.p', 'rb'))
	lfeat = pickle.load(open('../data/linkedinfeat.p', 'rb'))
	xsamp = []
	ysamp = []
	with open('../data/profilesalaries2.txt', 'r') as f1:
		for line in f1:
			uid, salary = line.rstrip('\n').split(',')
			salary = int(salary)
			xsamp.append(gfeat[uid] + lfeat[uid])
			ysamp.append(salary)

	with open('../data/searchsalaries2.txt', 'r') as f1:
		for line in f1:
			uid, salary = line.rstrip('\n').split(',')
			salary = int(salary)
			xsamp.append(gfeat[uid] + lfeat[uid])
			ysamp.append(salary)
	#pdb.set_trace()
	print len(xsamp)
	c = int(0.8*(len(xsamp)))
	xtrain = xsamp[:c]
	ytrain = ysamp[:c]
	xtest = xsamp[c:]
	ytest = ysamp[c:]

	return xtrain, ytrain, xtest, ytest, xsamp, ysamp

xtrain, ytrain, xtest, ytest, xsamp, ysamp = loadData()



regr = linear_model.LinearRegression()
regr.fit(xsamp, ysamp)
ypred = regr.predict(xsamp)
rms = sqrt(mean_squared_error(ysamp, ypred))
print rms

pickle.dump(regr, open('../data/model.p', 'wb'))

xs = np.array(xsamp)
#pdb.set_trace()
#print xs.shape

#mn = np.mean(xs, axis=0)
#st = np.std(xs, axis=0)
#pickle.dump((mn, st), open('../data/datanorm.p', 'wb'))
# clf = linear_model.Lars(n_nonzero_coefs=1)
# clf.fit(xtrain, ytrain)
# ypred2 = clf.predict(xtest)
# rms = sqrt(mean_squared_error(ytest, ypred2))
# print rms
coefficient_of_dermination = r2_score(ysamp, ypred)
print coefficient_of_dermination

x = np.array([x[0] for x in xsamp])
m, b = np.polyfit(x, ysamp, 1)
y = ysamp

regression = ols("data ~ x", data=dict(data=y, x=x)).fit()
#test = regression.outlier_test()
#outliers = ((x[i],y[i]) for i,t in enumerate(test.icol(2)) if t < 0.8)
#print 'Outliers: ', list(outliers)
# Figure #
figure = smgraphics.regressionplots.plot_fit(regression, 1)
# Add line #
smgraphics.regressionplots.abline_plot(model_results=regression, ax=figure.axes[0])
#plt.show()
#plt.scatter(x, ysamp)
#plt.plot(x, m*x + b, '-')
#plt.show()