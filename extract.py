import json

grp = {
    'tc' : 0,
    'app' : 1,
    'tf' : 2,
    'fl' : 3,
    'int' : 4,
    'amg' : 5,
    'aut' : 6
}

#exit()

fin = open("psup.json")
da = json.load(fin)
fin.close()

print("nmcf \t nmf \t nme \t rec \t bac0 \t bac1 \t bac2 \ pla")

for f in da['formations'].keys():
    tmp =  da['formations'][f]
    etTmp = da['etablissements'][tmp['gea']]
    print("{} \t {} \t {} \t {} \t {} \t {} \t{} \t{} \t".format(tmp['nmc'], tmp['nm'], etTmp['nm'], etTmp['rec'],
    tmp['bac'][0], tmp['bac'][1], tmp['bac'][2], tmp['pla']))
