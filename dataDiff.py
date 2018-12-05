#-*- coding: utf-8 -*
sourceFileName = 'winrm-needs-to-be-enabled.txt'

destFileName = 'winrm-enable-excluded.txt'
outputFileName = 'diff.txt'

sFile = open(sourceFileName, 'r')
dFile = open(destFileName, 'r')
oFile = open(outputFileName, 'w')

#모든 파일을 닫는다
def closeAllFiles():
    sFile.close()
    dFile.close()
    oFile.close()
#sourceFile을 읽어서 dictionary에 저장
sSet = set()
dSet = set()
def loadData(store, inputStream):
    while True:
        line = inputStream.readline()
        line.replace(' ', '')
        line = line.rstrip('\r\n')
        line = line.lower()
        store.add(line)
        print(line)
        if line == "":
            return

loadData(sSet, sFile)
loadData(dSet, dFile)

rSet = sSet.difference(dSet)

def saveData(store, outputStream):
    for i in store:
        outputStream.write(i+'\n')

saveData(rSet, oFile)

closeAllFiles()
print(str(rSet))
print('------------- Statistics -------------')
print('%s: %s' % (sourceFileName , len(sSet)))
print('%s: %s' % (destFileName , len(dSet)))
print('Difference: %s' % len(rSet))
print('Difference: %s' % len(rSet))
