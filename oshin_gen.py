import re
import json


# set the patterns to sessions 
# so they make a dao de ching, 
# two words, and patterns set in 4 rungs
# so we get more diverse over the conversation
# 3 pattern rhyme being the other wheel, or other pattern
# ching 4 

with open('oshin.txt') as f:
	fin = list(f.readlines())
	f.close()
	corpus= {
	'u': {},
	'e': {},
	'i': {},
	'o': {},
	}

	for wave in fin:
		if wave == '\n':
			continue
		else:
			crest = wave[0]
			trough= []
	
			for w in wave.split():
				calm = w.replace(',','').replace(':','')
				trough.append(calm)
			tide = {trough[0]:trough[1:]}
			corpus[crest].update(tide)

f = open('oshin_json.txt', "w")
f.write(json.dumps(corpus))
f.close()

