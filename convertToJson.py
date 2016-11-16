import cPickle as pickle 
import json
import io

f2 = io.open('extractions.json', 'w', encoding='utf-8')
allusersinfo = pickle.load(open('allusersinfo.p', 'rb'))
for user in allusersinfo:
	f2.write(unicode(json.dumps(allusersinfo[user], ensure_ascii=False)+'\n'))
