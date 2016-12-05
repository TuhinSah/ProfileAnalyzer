import sys
import cPickle as pickle 

def getPredictedSalary(feat):
	model = pickle.load(open('../data/model.p', 'rb'))
	res = model.predict([feat])
	print res
	sys.stdout.flush()
	return res