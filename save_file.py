import os
import sys

def outcome_file(keywords, counts, path, count):
    name = "abstract" + str(count) + ".txt"
    if os.path.exists(path + name):
        print "File exists"
    else:
        open(path + name, 'w')
    thefile = open(path + name, 'w')
    for n in range(0, len(keywords)):
        keyword = keywords[n]
        count = counts[n]
        thefile.write(keyword + "  " + count + "\n")
    thefile.close()

outcome_file(["['alloy']", "['appears']", "['atoms']", "['attributes']", "['available']", "['boundaries']", "['coarse']", "['concluded']", "['condensation']", "['confers']", "['conventional']", "['current']", "['density']", "['design']", "['diffusivity']", "['ductility']", "['emerging']", "['emphasis']", "['gas']", "['grain']", "['higher']", "['improved']", "['increased']", "['investigated']", "['located']", "['lower']", "['materials']", "['mechanical']", "['nanocrystalline']", "['nanoglasses']", "['picture']", "['polycrystalline']", "['potential']", "['properties']", "['quite']", "['recent']", "['reduced']", "['reviewed']", "['sizes']", "['soft']", "['special']", "['spray']", "['strength']", "['structure']", "['superior']", "['thermal']", "['toughness']", "['volume']", "['whereas']", "['years']"], ["['2']", "['1']", "['1']", "['1']", "['1']", "['3']", "['4']", "['1']", "['1']", "['1']", "['2']", "['1']", "['1']", "['1']", "['1']", "['1']", "['1']", "['1']", "['1']", "['8']", "['2']", "['1']", "['3']", "['2']", "['1']", "['1']", "['1', '7']", "['1']", "['1', '0']", "['1']", "['1']", "['2']", "['1']", "['3']", "['1']", "['2']", "['2']", "['2']", "['1']", "['1']", "['2']", "['1']", "['2']", "['4']", "['2']", "['2']", "['2']", "['1']", "['1']", "['1']"], "/Users/Robert/Desktop/", 1)