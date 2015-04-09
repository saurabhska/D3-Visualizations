import sys
import os
import json

wordDocDict=dict()
docLinksDict=dict()
nodeList=list()
def createWordDocDict(inputFile):
  global wordDocDict
  infile=open(inputFile,'r')
  lines=infile.readlines()
  for line in lines:
    line=line.replace("\n","")
    words=line.split(',')
    docName=words[0]
    del words[0]
    for word in words:
      if word not in wordDocDict:
        tempList=list()
        tempList.append(docName)
        wordDocDict[word]=tempList
      else:
        wordDocDict[word].append(docName)
  print("printing wordDocDict............")
  #print(wordDocDict)
  

def updateDocLinks(iWord,jWord):
  global docLinksDict
  if iWord not in docLinksDict.keys():
    tempDict=dict()
    tempDict[jWord]=1
    docLinksDict[iWord]=tempDict
  else:
    valueDict=docLinksDict[iWord]
    if jWord not in valueDict:
      valueDict[jWord]=1
    else:
      valueDict[jWord]+=1
    docLinksDict[iWord]=valueDict

def computeDocLinks():
  global docLinksDict
  global wordDocDict
  global nodeList
  for word,docList in wordDocDict.items():
    for i in range(0,len(docList)):
      pivot=docList[i]
      if pivot not in nodeList:
        nodeList.append(pivot)
      for j in range(0,len(docList)):
        if pivot != docList[j]:
           updateDocLinks(pivot,docList[j])

def createJSON(outputFile,clusterFactor):
  global docLinksDict
  global nodeList
  #print('nodeList')
  #print(nodeList)
  nodeList.sort()
  #print(str(nodeList))
  nodesList=list()
  linksList=list()
  JSONDict=dict()
  linksDict=dict()
  counter=0
  groupNumber=1
  for key in nodeList:
    counter+=1
    if counter % clusterFactor == 0:
      groupNumber+=1
    tempDict=dict()
    tempDict['name']=key
    tempDict['group']=groupNumber
    nodesList.append(tempDict)
  JSONDict['nodes']=nodesList
  for key,valueDict in docLinksDict.items():
    for subKey, value in valueDict.items():
      tempDict=dict()
      tempDict['source']=nodeList.index(key)
      tempDict['target']=nodeList.index(subKey)
      tempDict['value']=value
      linksList.append(tempDict)
  JSONDict['links']=linksList
  with open(outputFile, "w") as f:
    f.write(json.dumps(JSONDict))
  
  

def main():
  global wordDocDict
  global docLinksDict
  if len(sys.argv)!=4:
    print('usage: python3 formatAdjacencyMatrix.py input output cluster-factor')
    exit(1)
  
  inputFile=sys.argv[1]
  outputFile=sys.argv[2]
  clusterFactor=int(sys.argv[3])
  print('creating createWordDocDict...')
  createWordDocDict(inputFile)
  print('created createWordDocDict...')
  #print(wordDocDict)
  print('computing Links...')
  computeDocLinks()
  print('computed Links...')
  #print(docLinksDict)
  print('creating JSON...')
  createJSON(outputFile,clusterFactor)
  print('created JSON...')

if __name__=='__main__':
  main()
