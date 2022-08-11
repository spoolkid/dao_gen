import random 
import json
import re
 
fin = open('oshin_json.txt', 'r')
oshin = json.loads(fin.read())
fin.close()

fish = {
    "u": {
    'nym': 'u',
    'corpus': 'u',
    'porpus': [['a', 'pro', 'b'], ['a', 'pro', 'b'], ['d', 'pro', 'g']],
    'pod': 'u'
    },
    "n": {
    'nym': 'n',
    'corpus' : 'u', 
    'porpus' : [['d', 'pro', 'ull',], ['d', 'c', 'ull']],
    'pod': 'u'
    },
    "s": {
    'nym':'s',
    'corpus': 'e',
    'porpus': [['ell', 'pro', 'd', 'b', 'a', ], ['a', 'd', 'etter', 'pro', 'een']],
    'pod': 'e'
    },
    "o": {
    'nym': 'o',
    'corpus': 'o',
    'porpus': [['pro', 'f'], ['b', 'own'], ['pro','d'], ['pro', 'b']],
    'pod': 'o'
    },
    "i": {
    'nym':'i',
    'corpus': 'i',
    'porpus': [['a', 'pro', 'b', 'a', 'pro', 'c'], ['g', 'ice', 'c', 'd', 'pro', 'b']],
    'pod': 'i'
    },
    "l": {
    'nym': 'l',
    'corpus': 'i',
    'porpus': [['a', 'b', 'pro', 'f'], ['c', 'pro', 'd', 'f']],
    'pod': 'i'
    },
    "e": {
    'nym': 'e',
    'corpus': 'e',
    'porpus': [['h', 'c', 'pro', 'a'], ['g', '', 'pro', 'et']],
    'pod': 'e'
    },
    "d": {
    'nym':'d',
    'corpus': 'o',
    'porpus': [['h', 'pro', 'e', 'pro', 'b'], ['b', 'pro', 'c', 'pro', 'a']],
    'pod': 'o'
    }
    }

class tank:
    def __init__(self, soles):
        self.soles = soles
        self.ballad = []
        self.cycle = 2
    
    def revolve(self):
        self.duet(self.soles['e'], self.soles['i'])
        self.duet(self.soles['o'], self.soles['s'])
        self.duet(self.soles['u'], self.soles['n'])
        self.duet(self.soles['l'], self.soles['d'])
        self.fyre()

    def duet(self, fis1, fis2):
        sg1 = self.freestyle(fis1)
        sg2 = self.freestyle(fis2)
        swap = fis1['pod']
        fis1['pod'] = fis2['pod']
        fis2['pod'] = swap
        sg3 = self.freestyle(fis1)
        sg4 = self.freestyle(fis2)
        fis2['pod']=fis1['pod']
        fis1['pod']=swap
        self.ballad.extend([{fis1['nym']:sg1, 'metre':len(fis1['porpus'][0]), 'len':len(fis1['porpus']), 'round':1}, {fis2['nym']:sg2, 'metre':len(fis2['porpus'][0]), 'len':len(fis1['porpus']), 'round':1},
            {fis1['nym']:sg3, 'metre':len(fis1['porpus'][0]),'len':len(fis1['porpus']), 'round':2}, {fis2['nym']:sg4, 'metre':len(fis2['porpus'][0]),'len':len(fis1['porpus']), 'round':2}])

    def fyre(self):
        print(self.ballad)
        for poe in self.ballad:
            nym = list(poe.keys())[0]
            spin = poe[nym]
            print(f'\t{nym} {spin[0]}')
            for step in range(0,len(spin)//poe['metre']):
                print(' '.join(spin[step*poe['metre']:step*poe['metre']+poe['metre']]))
            print('\n')

    def freestyle(self, fish):
        rage = []
        prep = ['a', 'the', 'of', 'an', 'i', 'with', 'on', 'to', 'in']
        sand = {'pro': prep}
        soil = oshin[fish['corpus']]
        tide = oshin[fish['pod']]
        pool = dict(zip(['a','b','c','d','e','f','g','h'],random.sample([key for key in tide],8)))

        for wave in fish['porpus']:
            for w in range(self.cycle):
                for stroke in wave:
                    if len(stroke)==1:
                        if stroke in pool:
                            rage.append(random.choice(tide[pool[stroke]]))
                        else:
                            rage.append('error-{stroke}')
                            print(f'pattern {stroke} is not in stroke, redice')
                    else: 
                        if stroke in list(soil.keys()):
                            rage.append(random.choice(soil[stroke]))
                        elif stroke in list(sand.keys()):
                            rage.append(random.choice(sand[stroke]))
                        else:
                            print(f"some problem parsing {stroke} family with ")
        return(rage)

dao = tank(fish) 
dao.revolve()
