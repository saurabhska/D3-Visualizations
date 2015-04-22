import sys
import os
import json

wordDocDict=dict()
keywordsDict=dict()
JSONDict=dict()

def getNode():
  tempDict=dict()
  tempDict['user_id']=0
  tempDict['name']='keywords'
  childrenList=list()
  return tempDict
  
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
  #print("printing wordDocDict............")
  #print(wordDocDict)

def computeKeywordLinks():
  global wordDocDict
  global keywordsDict
  allkeywordsList=wordDocDict.keys()
  for word in allkeywordsList:
    if word[0] not in keywordsDict.keys():
      tempList=list()
      tempList.append(word)
      keywordsDict[word[0]]=tempList
    else:
      keywordsDict[word[0]].append(word)

def createJSON():
  global JSONDict
  global wordDocDict
  global keywordsDict
  JSONDict['user_id']=0
  JSONDict['name']='Keywords'
  JSONDict['children']=list()
  #childrenList=list()
  counter1=-1
  for key,valueList in keywordsDict.items():
    counter1+=1
    tempDict1=dict()
    tempDict1['user_id']=counter1
    tempDict1['name']=key
    tempDict1['children']=list()
    counter2=-1
    for inner_key in valueList:
      counter2+=1
      tempDict2=dict()
      tempDict2['user_id']=counter2
      tempDict2['name']=inner_key
      tempDict2['children']=list()
      docList=wordDocDict[inner_key]
      counter3=-1
      for doc in docList:
        counter3+=1
        tempDict3=dict()
        tempDict3['user_id']=counter3
        tempDict3['name']=doc
        tempDict2['children'].append(tempDict3)
      tempDict1['children'].append(tempDict2)
    JSONDict['children'].append(tempDict1)
  #print(json.dumps(JSONDict))
  with open("input.json", "w") as f:
    f.write(json.dumps(JSONDict))
      

  
def main():
  global wordDocDict
  global keywordsDict
  if len(sys.argv)!=2:
    print('usage: python3 formatAdjacencyMatrix.py input')
    exit(1)
  inputFile=sys.argv[1]
  print('creating createWordDocDict...')
  createWordDocDict(inputFile)
  print('created createWordDocDict...')
  #print(wordDocDict)
  print('computing Keyword Links...')
  computeKeywordLinks()
  print('computed Keyword Links...')
  #print(docLinksDict)
  print('creating JSON...')
  createJSON()
  print('created JSON...')
  #wordDocDict=dict()
  #keywordsDict=dict()
  #print('wordDocDict.....')
  #print(wordDocDict)
  #print('keywordsDict.....')
  #print(keywordsDict)

if __name__=='__main__':
  main()
