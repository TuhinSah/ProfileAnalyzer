import csv

results = {}
matches = 0
resultsCount = 0
trueMatchesCount = 0

with open('../data/results.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for line in reader:
		resultsCount += 1
		results[line['Id@github']]= line['Link@sourceB']

print results

with open('../data/truematches.txt') as trueMatches:
	for line in trueMatches:
		trueMatchesCount += 1
		githubId = line.split(',')[0]
		linkedinId = line.split(',')[4].split('/')[-1]
		print "githubId: " + str(githubId) + ", linkedinId: " + str(linkedinId)
		if githubId in results:
			print "results[" + githubId + "]: " + results[githubId] + ", linkedinId: " + linkedinId
			if results[githubId] == linkedinId:
				matches += 1 

precision = matches/resultsCount
recall = matches/trueMatchesCount

print "precision: " + str(precision) + ", recall: " + str(recall)