#-*- coding: utf-8 -*
import urllib3

http = urllib3.PoolManager()

zabbixURL = 'http://ncsma.ncsoft.net/zabbix/ip10.txt'
ncsmaURL = 'http://ncsma.ncsoft.net/game/ip10.txt'

sourceFileName = 'scanned-no-ad.txt'
outputFileName = 'ip-resolved.txt'
sFile = open(sourceFileName, 'r')
oFile = open(outputFileName, 'w')

#모든 파일을 닫는다
def closeAllFiles():
    sFile.close()
    oFile.close()

#sourceFile을 읽어서 dictionary에 저장
sDic = {}
dDic = [] # 순서가 중요함
rList = []

def loadData(store, inputStream):
    while True:
        line = inputStream.readline()
        line.replace(' ', '')
        line = line.rstrip('\r\n')
        line = line.lower()
        store.append(line)
        # print(line)
        if line == "":
            return

def loadZabbixData(store, url):
    r = http.request('GET', url)
    s = str(r.data)
    parsed = s.split('\\n')
    print(len(parsed))
    for i in parsed:
        splitted = i.split('\\t')
        if len(splitted) == 2:
            store[splitted[1].lower()] = splitted[0].lower()

def loadNCSMAData(store, url):
    r = http.request('GET', url)
    s = str(r.data)
    parsed = s.split('\\n')
    print(len(parsed))
    for i in parsed:
        splitted = i.split('\\t')
        # print(len(splitted))
        if len(splitted) == 3:
            store[splitted[2].lower()] = splitted[1].lower()
            # print('%s %s' %(splitted[1],splitted[2]))

def dumpData(store):
    if str(type(store)) == "<class 'dict'>":
        for i in store:
            print('%s : %s' %(i,store[i]))
    elif str(type(store)) == "<class 'list'>":
        for i in store:
            print('%s' %(i))
    else:
        print("no matched type for dumping")
        print("no matched type for dumping")

def saveData(store, outputStream):
    for i in store:
        outputStream.write(i+'\n')

def resolveIP(table, ips, outputStore):
    for i in ips:
        if i in table:
            matched = table[i]
            outputStore.append(matched)
            # print(matched)
        else:
            # print('null')
            outputStore.append('null')

loadZabbixData(sDic, zabbixURL)
loadNCSMAData(sDic, ncsmaURL)

# dumpData(sDic)
loadData(dDic, sFile)

resolveIP(sDic, dDic, rList)
dumpData(rList)

saveData(rList, oFile)

# saveData(rSet, oFile)

closeAllFiles()
# print('------------- Statistics -------------')
# print('%s: %s' % (sourceFileName, len(sSet)))
# print('%s: %s' % (destFileName, len(dSet)))
# print('Difference: %s' % len(rSet))
# print('Difference: %s' % len(rSet))
# print('Difference: %s' % len(rSet))
# feature branch
