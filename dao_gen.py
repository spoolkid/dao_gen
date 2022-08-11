import random 
import json
 
fin = open('oshin_json.txt', 'r')
oshin = json.loads(fin.read())
fin.close()

fis = {
    "u": {
    'corpus': 'u',
    'porpus': ['aab']
    },
    "n": {
    'corpus': 'u',
    'porpus': ['abb']
    },
    "s": {
    'corpus': 'e',
    'porpus': ['abc'],
    },
    "o": {
    'corpus': 'o',
    'porpus': ['aab'],
    },
    "i": {
    'corpus': 'i',
    'porpus': ['abc'],
    },
    "l": {
    'corpus': 'i',
    'porpus': ['aab'],
    },
    "e": {
    'corpus': 'e',
    'porpus': ['aba'],
    },
    "d": {
    'corpus': 'o',
    'porpus': ['aba'],
    }
    }

class tank:
    def __init__(self, soles):
        self.barrel = list(soles.keys())
        self.soles = soles
        self.metre = 6
    
    def revolve(self):
        if len(self.barrel) < 1: return 
        diamateur = len(self.barrel)//2
        round=[]

        for sole in range(diamateur):
            ballad = self.dual(sole, sole+diamateur)
            round.append(ballad['nym'])
            self.fyre(ballad)

        self.barrel = round
        self.revolve()

    def freestyle(self, n):
        c = self.soles[n]['corpus'] #u   
        p = self.soles[n]['porpus'] #abab
        
        duet = []
        wave = list(oshin[c].keys())

        for i in range(2):
            for ool in range(len(p)):
                s = len(set(p[ool]))
                strokes = random.sample(wave,s)

                for lap in range(2):
                    for tide in p[ool]:          
                        if tide == 'a':
                            duet.append(random.choice(list(oshin[c][strokes[0]])))
                        elif tide == 'b':
                            duet.append(random.choice(list(oshin[c][strokes[1]])))
                        elif tide == 'c':
                            duet.append(random.choice(list(oshin[c][strokes[2]])))
                        elif tide == 'd':
                            duet.append(random.choice(list(oshin[c][strokes[3]])))

        return (duet)

    def fyre(self, ballad):
        print('\n' + ballad['nym'] + ' ' + ballad['spin'][0])
        for l in range(len(ballad['spin'])//self.metre): 
            print(' '.join(ballad['spin'][l*self.metre:l*self.metre+self.metre]))

    def dual(self, b, w):
        fis1 = {
        'nym':self.barrel[b],
        'fin': False, 
        'spin': [] 
        }
        fis2 = {
        'nym':self.barrel[w],
        'fin': False, 
        'spin': [] 
        }
        
        fis1['spin'] = (self.freestyle(fis1['nym']))
        fis2['spin'] = (self.freestyle(fis2['nym']))
        ballad = random.choice([fis1, fis2])
        ballad['fin'] = True

        #both porpus update, not winning sole
        if fis1['fin']:
            self.soles[fis1['nym']]['porpus'].append(self.soles[fis2['nym']]['porpus'][0])
        elif fis2['fin']:
            self.soles[fis2['nym']]['porpus'].append(self.soles[fis1['nym']]['porpus'][0])
        return ballad


dao = tank(fis) 
dao.revolve()
