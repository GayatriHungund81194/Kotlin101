import collections
tsvFile = open('/Users/gayatrihungund/Downloads/mars-rover-takehome/test/sample/problem.tsv', 'r') 
lineList = list(tsvFile.readlines())
print(lineList)
total_bytes = lineList[0].rstrip()
total_bytes = int(total_bytes)
print(total_bytes)
metaDict = dict()
count = 0
for line in lineList:
    if count > 0:
        line = line.rstrip()
        line = list(line.split("\t"))
        print(line)
        addn = int(line[1]) + int(line[2])
        print(addn)
        metaDict[line[0]] = [(int(line[1]),addn,int(line[2]))] 
    count = count + 1
print(metaDict)
intervalList = list()
for key in metaDict:
    intervalList.append((metaDict[key][0]))
print(intervalList)
lastList = list()
tempList = list()
for index,value in enumerate(intervalList):
    if value[1] == total_bytes:
        lastList.append(value)
print(lastList)
for rangeTuple in lastList:
    for eachTuple in intervalList:
        if (eachTuple[0]<rangeTuple[0] and eachTuple[1]>rangeTuple[0] and eachTuple not in lastList):
            tempList.append(eachTuple)
    if len(tempList) == 1:
        lastList.append(tempList[0])
        tempList.clear()
    elif len(tempList)>1:
        mini = (0,0,99999999)
        tempList.sort(key=lambda x: x[0])
        minimumStart = tempList[0]
        tempList.sort(key=lambda x: x[2],reverse=True)
        maxByteSize = tempList[0]
        tempList.sort(key=lambda x: x[0])
        
        print("Temppppppp",tempList)
        if minimumStart == maxByteSize:
            mini = tempList[1]
        else:
            mini = tempList[0]
        # for i in range(len(tempList)):
        #     if tempList[i][2] < mini[2]:
        #         mini = tempList[i]
        tempList.clear()
        if mini != (0,0,99999999):
            lastList.append(mini)
print(lastList)
keyList = list()
for selectedTuple in lastList:
    for key,val in metaDict.items():
        if val[0] == selectedTuple:
            keyList.append(key)
print(sorted(keyList))