import time
import re
#
# ISOTIMEFORMAT='%Y-%m-%d'
#
# dayd = time.strftime(ISOTIMEFORMAT,time.localtime())
# a = ('64 / 12756').split('/')
# a = [['6','4',5,6,7,8],['4','15',6,6,7,8],['4','6',87,76,54,3]]
# a.sort(cmp = lambda x,y:int(x[0])-int(y[0]) or int(x[1])-int(y[1]),reverse= True)
# print a
a = '123<dasdadad<hehe>123<dsdadsada>shabi<hehe>123<dsdada>shabi<hehe>'

pattern = re.compile('1(.*?)he>',re.S)

dd = re.findall(pattern, a)
pattern1 = re.compile('23<(.*?)>shabi',re.S)
result = []
for i in dd:
    itemts = re.search(pattern1, i)
    if itemts != None:
        result.append(itemts.group(1))
for i in result:
    print i
