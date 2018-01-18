import time
import re
import sys
import argparse
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parseBooleanIndel(b):
	if(len(b) < 1):
		raise ValueError('Error: Cannot parse empty string into boolean')
	##b=b[0].lower
	if b=='keepIndel':
		return True
	if b=='removeIndel':
		return False
	raise ValueError('Error: Cannot parse string into boolean')
	
def retrieveGenotypes(arg):
	if(arg=='getGenotypes'):
		return True
	raise ValueError('Error: Cannot parse string into boolean')
	
	
def getAlleleCount(arg):
	if(arg=='True'):
		return True
	raise ValueError('Error: Cannot parse string into boolean')	

def getAlleleFreq(arg):
	if(arg=='True'):
		return True
	raise ValueError('Error: Cannot parse string into boolean')

def parseKeepChrom(b):
	if(len(b) < 1):
		raise ValueError('Error: Cannot parse empty string into boolean')
	##b=b[0].lower
	if(b=='True'):
		return True
	if(b=='False'):
		return False
	raise ValueError('Error: Cannot parse string into boolean')


def parseRetrieveVariants(b):
	if(len(b) < 1):
		raise ValueError('Error: Cannot parse empty string into boolean')
	##b=b[0].lower
	if(b=='True'):
		return True
	if(b=='False'):
		return False
	raise ValueError('Error: Cannot parse string into boolean')

def getTs(b):
	if(len(b) < 1):
		raise ValueError('Error: Cannot parse empty string into boolean')
	##b=b[0].lower
	if(b=='Ts'): ### Transition
		return True
	else:
		return False
	raise ValueError('Error: Cannot parse string into boolean')

def getTv(b):
	if(len(b) < 1):
		raise ValueError('Error: Cannot parse empty string into boolean')
	##b=b[0].lower
	if(b=='Tv'): ### Transition
		return True
	else:	
		return False
	raise ValueError('Error: Cannot parse string into boolean')

def getTsTv(b):
	if(len(b) < 1):
		raise ValueError('Error: Cannot parse empty string into boolean')
	##b=b[0].lower
	if(b=='TsTv'): ### Transition
		return True
	else:	
		return False
	raise ValueError('Error: Cannot parse string into boolean')



def Main():
	listOfArguements=[]
	parser=argparse.ArgumentParser(description='This is a tool similar to vcftools written in python')
	##group=parser.add_mutually_exclusive_group(required=False)
	parser.add_argument('--vcf',nargs='?')
	##parser.add_argument('--chr',nargs=1)
	parser.add_argument('--qualScore',nargs='?')
	parser.add_argument('--bedFile',nargs='?')
	parser.add_argument('--keepChrom',type=parseKeepChrom)
	parser.add_argument('--chrom',nargs='?')
	parser.add_argument('--lociList',nargs='?')
	parser.add_argument('--keepLoci',type=parseRetrieveVariants)
	parser.add_argument('--Indel',type=parseBooleanIndel)
	parser.add_argument('--getGenotypes',type=retrieveGenotypes)
	parser.add_argument('--getAlleleCount',type=getAlleleCount)
	parser.add_argument('--getAlleleFreq',type=getAlleleFreq)
	parser.add_argument('--minDP',nargs=1)
	parser.add_argument('--getTs',type=getTs)
	parser.add_argument('--getTv',type=getTv)
	parser.add_argument('--getTsTv',type=getTsTv)
	##parser.add_argument('--getTsTv',type=)
	
	args=parser.parse_args()
	##print("This just prints the vcf file name")
	##print (args.vcf)
	return args
	
	
	
	
if __name__=='__main__':
	Main()
	

def readTestFile(): ## Working fine
	allReturned=[]
	allReturned=Main()
	print(allReturned) ## returns ['sample.vcf', '20']
	vcfSupplied=allReturned.vcf
	handle=open(vcfSupplied,'r')
	lines="\n"
	for line in handle:
		lines+=line
	handle.close()
	return lines
	
vcfRead = readTestFile() ## a multi sample vcf
print("Just reading in file name entered")
print (vcfRead)


def extractLinesWithVariants(): ## Working fine
	allReturned=[]
	allReturned=Main()
	vcfLinesToSplit=readTestFile()
	##print("Called the main and read test file function in extractLinesWithVariants function")
	print("\n")
	linesRead = re.split("\n",vcfLinesToSplit)
	return linesRead


linesToAList=extractLinesWithVariants()
print("Testing extractLinesWithVariants() function")
print('\n')
##print(linesToAList) ## working fine


def getOnlyVariantsFromList(): ## Working fine
	OnlyVariants=[]
	indexOfHeaderLine=0
	linesToAList=extractLinesWithVariants()
	print("\n")
	for eachLine in linesToAList:
		
		if('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT' in eachLine):
			indexOfHeaderLine=linesToAList.index(eachLine)
			for anIndex in range(indexOfHeaderLine,len(linesToAList),1):
				splittingTheLinesToAList=re.split('\t',linesToAList[anIndex])
				OnlyVariants.append(splittingTheLinesToAList)
		
		
	return OnlyVariants

listOfVariants=getOnlyVariantsFromList()
print("Testing the getOnlyVariantsFromList() function")
listOfVariantsNew=listOfVariants[0:len(listOfVariants)-1]
##print(listOfVariantsNew) ### Working fine,6 variants retrieved


def getAllLinesBeforeChromLine(): ## Working fine
	
	indexOfHeaderLine=0
	linesToAList=extractLinesWithVariants()
	print("\n")
	OnlyLines=[]
	indexOfHeaderLine=0
	for eachLine in linesToAList:
		
		if('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT' in eachLine):
			indexOfHeaderLine=linesToAList.index(eachLine)
			OnlyLines=linesToAList[0:indexOfHeaderLine+1]
		
		
	return OnlyLines


print("Testing the getAllLinesBeforeChromLine() function")
allLinesBeforeChromLine=getAllLinesBeforeChromLine()
##print(allLinesBeforeChromLine)




def convertQualToFloat(): ## Working fine
	vcfInfoReturned=getOnlyVariantsFromList()
	vcfInfoReturned=vcfInfoReturned[0:len(vcfInfoReturned)]
	varWithQualScoreFloat=[]
	##print("Testing if returning value from convertQualToFloat() is working or not")
	for index in range(1,len(vcfInfoReturned)-1,1):## converting index to one such that first list is left untouched
			eachVar=vcfInfoReturned[index]
			
			qualScore=eachVar[5]
		
		
			qualScoreFloat=float(qualScore)
		
			eachVarWithOutQual=eachVar[0:5]+eachVar[6:]
			eachVarWithOutQual.append(qualScoreFloat)
			
			varWithQualScoreFloat.append(eachVarWithOutQual)
	return varWithQualScoreFloat

print("\n")
listWithQualScoreFloat=convertQualToFloat() ## working
print("This is the list of variants aftering converting qual score to float")
##print(listWithQualScoreFloat) ## 6 returned
##print(len(listWithQualScoreFloat))

def sortByQualScore(listOfAllVariants): ## Working fine
	
	##listWithQualScoreFloat=convertQualToFloat()
	if(len(listOfAllVariants) < 2):
		return listOfAllVariants
	sortedQualScoreList=[]
	
	mid=int(len(listOfAllVariants)/2)
	leftList=sortByQualScore(listOfAllVariants[:mid])
	rightList=sortByQualScore(listOfAllVariants[mid:])
	while(len(leftList) > 0) and (len(rightList) > 0):
		if(leftList[0][len(leftList[0])-1] > rightList[0][len(rightList[0])-1]):
			sortedQualScoreList.append(rightList[0])
			rightList.pop(0)
		else:
			sortedQualScoreList.append(leftList[0])
			leftList.pop(0)
	sortedQualScoreList=sortedQualScoreList+leftList
	sortedQualScoreList=sortedQualScoreList+rightList
	return sortedQualScoreList


listSortedAsPerQualScore=sortByQualScore(listWithQualScoreFloat)
##print("Testing if sorting by qual score is working or not") ## Logic is okay but calling listWithQualScoreFloat() is not working with recursion issues
print("\n")
print("The variants sorted by qual score are")
##print(listSortedAsPerQualScore)


def filterVariantsAboveAQualScore(qualScoreSupplied): ### here sorted list of variants by qual score gets passed, working okay
## Has bug is qual score above anything in list. NEED TO FIX IT
	##listWithQualScoreFloat=convertQualToFloat()
	qualScoreAsFloat=convertQualToFloat()
	variantsSortedByQualScore=sortByQualScore(qualScoreAsFloat)
	allReturned=[]
	allReturned=Main()
	print(allReturned) ## returns ['sample.vcf', '20']
	qualScoreSupplied=allReturned.qualScore
	aQualScore=float(qualScoreSupplied)
	##print(aQualScore)
	start=0
	end=len(listOfVariants)-1
	while(start <= end):
		mid=start+(end-start)/2
		mid=int(mid)
		if(variantsSortedByQualScore[mid][len(variantsSortedByQualScore[mid])-1] >= aQualScore and variantsSortedByQualScore[mid-1][len(variantsSortedByQualScore[mid-1])-1] < aQualScore ):
			return mid
		elif(variantsSortedByQualScore[mid][len(variantsSortedByQualScore[mid])-1] > aQualScore):
			end=mid-1
		else:
			if(variantsSortedByQualScore[mid][len(variantsSortedByQualScore[mid])-1] < aQualScore):
				start=mid+1		
	return -1

##listAfterFilterByQualScore=filterVariantsAboveAQualScore()
print("The variants sorted by qual scoore of 50 are")
##index=filterVariantsAboveAQualScore(listSortedAsPerQualScore) ## WORKS FINE
print("The variants of interest after filtering by 50 are")
##print(listSortedAsPerQualScore[index:len(listSortedAsPerQualScore)+1])## WORKS FINE
## python3 vcfAnnotatorWithArgParse.py --vcf sampleChr1Chr10.vcf --qualScore 1000

def retrieveVariantsWithQualScoreAboveMin(): ## This is working as expected
	allReturned=[]
	allReturned=Main()
	qualScoreSupplied=allReturned.qualScore
	variantsWithQualScoreAsFloat=convertQualToFloat()
	variantsSortedByQualScore=sortByQualScore(variantsWithQualScoreAsFloat)
	variantIndexGreaterThanQualOfInterest=filterVariantsAboveAQualScore(qualScoreSupplied)
	return(variantsSortedByQualScore[variantIndexGreaterThanQualOfInterest:])

print('\n')
print('\n')
print('\n')
print("TESTING IF FILTERING BY QUAL SCORE IS WORKING OR NOT")
variantsWithScoreAboveMin=retrieveVariantsWithQualScoreAboveMin()
print(len(variantsWithScoreAboveMin))
for i in range(0,len(variantsWithScoreAboveMin)):
	variant=variantsWithScoreAboveMin[i]
	print(variant)
	print("\n")


def writeAnyFilteredVariantsToAVcf(linesBeforeChromeLine,listOfVariants): ## This is okay
	##print(len(linesBeforeChromeLine))
	##print(len(listOfVariants))
	linesbeforeChromLineAsLines='\n'.join(linesBeforeChromeLine) 
	varList=[]
	for anyVar in listOfVariants:
		aVariantAsString='\t'.join(anyVar)
		varList.append(aVariantAsString)
	f=open('filteredVariants.vcf','w')
	f.write(linesbeforeChromLineAsLines+'\n')
	for variant in varList:
		f.write(variant+'\n')
	f.close()



def convertRemoveChrWordAndMakeLociInfoInt():
	
	variantsReturned=getOnlyVariantsFromList()
	variantsReturned=variantsReturned[1:len(listOfVariants)-1]
	##print("Testing if calling getOnlyVariantsFromList() from convertRemoveChrWord() is working or not")
	print("\n")
	##print(variantsReturned)
	allVariants=[]
	for aVariant in variantsReturned:
		eachVarList=[]
		chrWord=aVariant[0]
		chrWordSplit=re.findall("\d+",chrWord)
		##print(chrWordSplit)
		
		intChr=int(chrWordSplit[0]) 
		intLoci=int(aVariant[1])
		##print(intLoci)
		eachVarList.extend([intChr,intLoci]) ## This is chr start and stop as integer
		listWithOutLoci=aVariant[2:len(aVariant)] ## This is the list without chr start and stop
		varListToReturn=eachVarList+listWithOutLoci
		##print(varListToReturn)
		##listPerVariant=eachVarList+listWithOutLoci
		allVariants.append(varListToReturn)
		
		##allVariants.append(onlyIntPart)
	return allVariants
	
print("New variant list after making chromosomes integer")
print("\n")
listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
##print(listWithQualScoreFloatAndLociInt) ## working fine


def sortByChrLoci(listWithQualScoreFloatAndLociInt): ## not sure how to do it especially with the recursion
	##print("Calling the convertRemoveChrWordAndMakeLociInfoInt() from the sortByChrLoci() function ")
	
	if(len(listWithQualScoreFloatAndLociInt) < 2):
		return listWithQualScoreFloatAndLociInt
	listSortedByChrAndPos=[]
	mid=int(len(listWithQualScoreFloatAndLociInt)/2)
	
	leftList=sortByChrLoci(listWithQualScoreFloatAndLociInt[:mid])
	rightList=sortByChrLoci(listWithQualScoreFloatAndLociInt[mid:])
	while(len(leftList) > 0) and (len(rightList) > 0):
		if(leftList[0][0] >= rightList[0][0]):
			if(leftList[0][1] > rightList[0][1]):
				listSortedByChrAndPos.append(rightList[0])
				rightList.pop(0)
			else:
				if(leftList[0][1] < rightList[0][1]):
					listSortedByChrAndPos.append(leftList[0])
					leftList.pop(0)
		else:
			if(leftList[0][0] <= rightList[0][0]):
				listSortedByChrAndPos.append(leftList[0])
				leftList.pop(0)
	
	listSortedByChrAndPos=listSortedByChrAndPos+leftList
	listSortedByChrAndPos=listSortedByChrAndPos+rightList

	return listSortedByChrAndPos


def functionToCallSortByChrLoci(): ## Works fine, no recursion error. Sorting by loci is also okay
	lociAllInt=convertRemoveChrWordAndMakeLociInfoInt()
	variantLociSorted=sortByChrLoci(lociAllInt)
	return variantLociSorted

listSortedByChrLoci=functionToCallSortByChrLoci()
print("This is the variant list sorted by loci. USE THIS FOR ALL SEARCHES") ## genotypes being included
print(listSortedByChrLoci) ### USE THIS FOR ALL SUBSEQUENT OPERATIONS AND WORKING FINE









## THE SYNTAX HAS TO BE SUCH THAT BASED ON WHAT IS INPUT A METHOD GETS CALLED

## FOR PULLING VARIANTS OUT BY CHROMOSOME IS FUNCTION FROM LINE 307 TILL 360
def findIndexOfFirstOccurenceOfParticularChrom(chromSupplied): ## working fine
	listOfVariantsSorted=functionToCallSortByChrLoci()
	low=0
	high=len(listOfVariantsSorted)-1
	result=-1
	while(low <= high):
		mid=low+(high-low)/2
		mid=int(mid)
		if(chromSupplied==listOfVariantsSorted[mid][0]):
			result=mid
			high=mid-1
		else:
			if(chromSupplied < listOfVariantsSorted[mid][0]):
				high=mid-1
			else:
				low=mid+1
	return result
	
firstOccurenceOfChr10=findIndexOfFirstOccurenceOfParticularChrom(10) ## works fine
firstOccurenceOfChr1=findIndexOfFirstOccurenceOfParticularChrom(1) ## works fine

print("This is first occurence of chromosome 1")
##print(firstOccurenceOfChr1)
##print(listSortedByChrLoci[firstOccurenceOfChr1])## works for chr 1 and chr10

	
def findIndexOfLastOccurenceOfParticularChrom(chromSupplied): ## working fine
	listOfVariantsSorted=functionToCallSortByChrLoci()
	low=0
	high=len(listOfVariantsSorted)-1
	result=-1
	while(low <= high):
		mid=low+(high-low)/2
		mid=int(mid)
		if(chromSupplied==listOfVariantsSorted[mid][0]):
			result=mid
			low=mid+1
		else:
			if(chromSupplied < listOfVariantsSorted[mid][0]):
				high=mid-1
			else:
				low=mid+1
	return result

lastOccurenceOfChr10=findIndexOfLastOccurenceOfParticularChrom(10)
lastOccurenceOfChr1=findIndexOfLastOccurenceOfParticularChrom(1)
print("This is last occurence of chromosome 1")	
##print(lastOccurenceOfChr1)
##print(listSortedByChrLoci[lastOccurenceOfChr1])## works for chr 1 and chr10

def retrieveAllVariantsForAChrom(): ## working fine
	allReturned=[]
	allReturned=Main()
	aChromToExtract=(allReturned.keepChrom)
	allVariantsForChr=[]
	listOfVariantsSorted=functionToCallSortByChrLoci()
	if(aChromToExtract==True):
		chromToFind=int(allReturned.chrom)
		firstOccurenceOfChr=findIndexOfFirstOccurenceOfParticularChrom(chromToFind)
		lastOccurenceOfChr=findIndexOfLastOccurenceOfParticularChrom(chromToFind)
	##allVariantsForChr=listOfVariantsSorted[lastOccurenceOfChr]
		allVariantsForChr=listOfVariantsSorted[firstOccurenceOfChr:lastOccurenceOfChr+1]
	return allVariantsForChr
	
allChr1Vars= retrieveAllVariantsForAChrom() ## WORKS FINE
print("Testing if retrieveAllVariantsForAChrom() function is working or not ")
print(allChr1Vars) ## This is working perfectly fine

def removeAllVariantsForAChrom():
	allReturned=[]
	allReturned=Main()
	aChromToExtract=(allReturned.keepChrom)
	allVariantsNotInChr=[]
	if(aChromToExtract==False):
		chromToRemove=int(allReturned.chrom)
		listOfVariantsSorted=functionToCallSortByChrLoci()
		firstOccurenceOfChr=findIndexOfFirstOccurenceOfParticularChrom(chromToRemove)
		lastOccurenceOfChr=findIndexOfLastOccurenceOfParticularChrom(chromToRemove)
		allVariantsNotInChr=listOfVariantsSorted[0:firstOccurenceOfChr] + listOfVariantsSorted[lastOccurenceOfChr+1:]
	return allVariantsNotInChr
	
allNotChr1Vars=removeAllVariantsForAChrom()  ## WORKS FINE
print("Testing removeAllVariantsForAChrom() is working or not")
print(allNotChr1Vars)
print(len(allNotChr1Vars))


def readAnyFile(file): ## Working fine
	
	handle=open(file,'r')
	lines="\n"
	for line in handle:
		lines+=line
	handle.close()
	return lines

def readInBedConvertToList(): ## working fine
	allReturned=[]
	allReturned=Main()
	print(allReturned) ## returns ['sample.vcf', '20']
	bedFileSupplied=allReturned.bedFile
	##print("This is the function to read a bed file")## control comes here and reads in two bed entries
	print(bedFileSupplied)
	
	aBedFileRead=readAnyFile(bedFileSupplied)
	bedAsList=[]
	bedFileRead=re.split('\n',aBedFileRead)
	bedFileRead.remove(bedFileRead[0])
	bedFileRead.remove(bedFileRead[len(bedFileRead)-1])
	for aBed in bedFileRead:
		listPerLoci=[]
		splittedBed=re.split('\t',aBed)
		splittedBedChr=re.split('r',splittedBed[0])
		chrAsInt = int(splittedBedChr[1])
		chrStartAsInt=int(splittedBed[1])
		chrStopAsInt=int(splittedBed[2])
		listPerLoci.extend([chrAsInt,chrStartAsInt,chrStopAsInt])
		bedAsList.append(listPerLoci)
	return bedAsList


print("Testing if reading in a bed file and converting to list is working not")
##bedFileAsList=readInBedConvertToList() ## Working fine [[1, 11873, 14409], [1, 14361, 16765]]
##print(bedFileAsList) ## BED FILE MUST BE TAB DELIMITED WITH NO HEADER AND CHR WORD PRESENT IN FRONT OF CHROMOSOME




def findIndexOfLowestPosForVarGreaterThanStartOfBedRegion(bedEntry): ## THIS IS OKAY- APPLY ON VARIANTS FOR SPECIFIC CHR
	
	bedEntryChr=bedEntry[0]
	bedEntryStart=bedEntry[1]
	bedEntryStop=bedEntry[2]
	
	chrLastIndex=findIndexOfLastOccurenceOfParticularChrom(bedEntryChr)
	chrFirstIndex=findIndexOfFirstOccurenceOfParticularChrom(bedEntryChr)
	while(chrFirstIndex <= chrLastIndex):
		mid=(chrFirstIndex)+(chrLastIndex-chrFirstIndex)/2
		mid=int(mid)
		
		if(listSortedByChrLoci[mid][1] >= (bedEntryStart) and listSortedByChrLoci[mid-1][1] < bedEntryStart):
				return mid ## last position closest to end of bed
		elif(bedEntryStart < listSortedByChrLoci[mid][1]):
					 chrLastIndex=mid-1 ## variants of a bed are to the right of mid and hence firstIndex increment by mid
		else:
			if(bedEntryStart > listSortedByChrLoci[mid][1]):
					chrFirstIndex=mid+1
	return -1	
	
	
##aBedRegion=bedFileAsList[0] ##  [1, 14361, 19759]
print("Trying to find variant greater than start of bed")
##print(aBedRegion)
##indexOfStart=findIndexOfLowestPosForVarGreaterThanStartOfBedRegion(aBedRegion)
##print(indexOfStart)
##print(listSortedByChrLoci[indexOfStart]) ## works fine


	
def findIndexOfLargestVarSmallerThanEndOfBedRegion(bedEntry): ## THIS IS OKAY- APPLY ON VARIANTS FOR SPECIFIC CHR
	bedEntryChr=bedEntry[0]
	bedEntryStart=bedEntry[1]
	bedEntryStop=bedEntry[2]
	listOfVariantsSorted=functionToCallSortByChrLoci()
	chrLastIndex=findIndexOfLastOccurenceOfParticularChrom(bedEntryChr)
	chrFirstIndex=findIndexOfFirstOccurenceOfParticularChrom(bedEntryChr)
	specificChrVariants=listOfVariantsSorted[chrFirstIndex:chrLastIndex+1]
	##print(specificChrVariants)
	startIndex=0
	endIndex=len(specificChrVariants)-1
	while(startIndex <= endIndex):
		mid=(startIndex+endIndex)/2
		mid=int(mid)
		if(bedEntryStop > specificChrVariants[mid][1] and  bedEntryStop < specificChrVariants[mid+1][1] ):
			return mid+1
		elif(bedEntryStop > specificChrVariants[mid][1]):
				endIndex=mid-1
		else:
			if(bedEntryStop < specificChrVariants[mid][1]):
				endIndex=mid-1
	
	return -1
	
print("Trying to find variant smaller than stop of bed")
##print(aBedRegion)
##indexOfStop=findIndexOfLargestVarSmallerThanEndOfBedRegion(aBedRegion)
##print(indexOfStop)
##print(allChr1Vars[indexOfStop]) ## works fine. VERY IMP TO NOTE THE LIST BEING PASSED HERE IS THAT OF SPECIFIC CHROMOSOME AND NOT OF ALL VARS

	
	
def retrieveVariantsByBedFile(aSingleBedEntry): ## Worked for [1, 14361, 16765] 
	allReturned=[]
	allReturned=Main()
	allVariantsForTheBedRegion=[]
	chrOfBedFile=aSingleBedEntry[0]
	startPosOfBedRegion=aSingleBedEntry[1]
	endPosBedRegion=aSingleBedEntry[2]
	firstIndexOfOccurenceOfBedChr=findIndexOfFirstOccurenceOfParticularChrom(chrOfBedFile)
	lastIndexOfOccurenceOfBedChr=findIndexOfLastOccurenceOfParticularChrom(chrOfBedFile)
	listOfVariants = convertRemoveChrWordAndMakeLociInfoInt()
	listOfVariantsSorted=sortByChrLoci(listOfVariants) 
	allBedChrVariants=listOfVariantsSorted[firstIndexOfOccurenceOfBedChr:lastIndexOfOccurenceOfBedChr+1]
	firstIndexForVariantWithinSpecificBed=findIndexOfLowestPosForVarGreaterThanStartOfBedRegion(aSingleBedEntry)
	lastIndexForVariantWithinSpecificBed=findIndexOfLargestVarSmallerThanEndOfBedRegion(aSingleBedEntry)
	print(firstIndexForVariantWithinSpecificBed)
	print("THIS IS THE FIRST VARIANT IN BED")
	print(allBedChrVariants[firstIndexForVariantWithinSpecificBed])
	print("THIS IS THE LAST VARIANT IN BED")

	print(lastIndexForVariantWithinSpecificBed)
	print(allBedChrVariants[lastIndexForVariantWithinSpecificBed])

	variantsForBed=allBedChrVariants[firstIndexForVariantWithinSpecificBed:]
	return variantsForBed


print("Testing if retrieving variants for a single bed is working or not")
print("This is the bed ")
##print(aBedRegion)
print("These are variants within the bed")
##variantsRetrieved=retrieveVariantsByBedFile(aBedRegion)
##print(len(variantsRetrieved))
print("Displaying variants within bed")

	
	
def retrieveVariantsForAllBed():  ## THIS IS WORKING FINE
	listOfBedRetrieved=readInBedConvertToList()
	print(listOfBedRetrieved)
	##listOfVariantsSorted=functionToCallSortByChrLoci()
	allVariantsForAllBed=[]
	for eachBed in listOfBedRetrieved:
		variantsForSpecificBed=retrieveVariantsByBedFile(eachBed)
		allVariantsForAllBed.extend(variantsForSpecificBed)
	return allVariantsForAllBed
	
##variantsRetrievedForAllBed=retrieveVariantsForAllBed()
##print("Variants for all bed")




def retrieveJustLoci(): ## THIS IS WORKING FINE
	allReturned=[]
	allReturned=Main()
	print(allReturned) ## returns ['sample.vcf', '20']
	lociList=allReturned.lociList
	listOfVars=[]
	handle=open(lociList,'r')
	lines="\n"
	for line in handle:
		lines+=line
	handle.close()
	return lines
	

##variantsSupplied=retrieveJustLoci()
print("These are the variants supplied by the user")
##print(variantsSupplied)


def convertLinesOfVarstolist(): ## THIS IS WORKING FINE
	linesRead=retrieveJustLoci()
	linesToList = re.split("\n",linesRead)
	return linesToList
	
##variantsAsList=convertLinesOfVarstolist()
print("These are the variants as python list")
##print(variantsAsList)

def modifyFileWithLociToExtractVars(): ## Working fine
	listOfVars=[]
	variantsAsList=convertLinesOfVarstolist()
	for index in range(1,len(variantsAsList)-1,1):
		listPerVar=[]
		aVar=re.split('\t',variantsAsList[index])
		aVarFirstIndex=re.split('r',aVar[0])
		onlyChr=[int (x) for x in aVarFirstIndex[1]]
		chrPosition=int(aVar[1])
		listPerVar.append(onlyChr[0]) ## append is for element
		listPerVar.append(chrPosition)
		listOfVars.append(listPerVar) ## append also works for a list
		 ##listOfVars.append(onlyChr)
	return listOfVars
	
##variantsAsListOfLists=modifyFileWithLociToExtractVars()
print("These are variants to extract as list of lists")
##print(variantsAsListOfLists)

def extractOneVariantIndex(aVariantToSearch): ## THIS IS WORKING FINE
	
	
	
	variantChr=aVariantToSearch[0]
	variantPosOnChr=aVariantToSearch[1]
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	indexOfFirstOccurenceOfChr=findIndexOfFirstOccurenceOfParticularChrom(variantChr)
	indexOfLastOccurenceOfChr=findIndexOfLastOccurenceOfParticularChrom(variantChr)
	
	arraySize=indexOfLastOccurenceOfChr-indexOfFirstOccurenceOfChr+1
	
	while(indexOfFirstOccurenceOfChr <= indexOfLastOccurenceOfChr):
		
		mid=(indexOfFirstOccurenceOfChr+indexOfLastOccurenceOfChr)/2
		mid=int(mid)
		if(listSortedByChrLoci[mid][1]==variantPosOnChr):
			return mid
		elif(variantPosOnChr < listSortedByChrLoci[mid][1]):
			indexOfLastOccurenceOfChr=mid-1
		else:
			if(variantPosOnChr > listSortedByChrLoci[mid][1]):
				indexOfFirstOccurenceOfChr=mid+1
	return -1	
			
##aVariantToExtract=variantsAsListOfLists[1]

##variantExtracted=extractOneVariant(aVariantToExtract)
print("Testing if extractOneVariant() function is working or not")
##print(variantExtracted)



def keepVariantsAtTheseLoci(): ## working fine
	allReturned=[]
	allReturned=Main()
	varsToKeepBool=(allReturned.keepLoci)
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	variantsExtracted = modifyFileWithLociToExtractVars()
	allInfoForAllVars=[]
	if(varsToKeepBool==True):
		for aVar in variantsExtracted:
			eachLociIndexInListByChr=extractOneVariantIndex(aVar)
			##print(eachLociIndexInListByChr)
			if(eachLociIndexInListByChr != -1):
				##print("This is a variant present in the VCF file")
				##print(eachLociIndexInListByChr)
				##print(listSortedByChrLoci[eachLociIndexInListByChr])
				allInfoForAllVars.append(listSortedByChrLoci[eachLociIndexInListByChr])
	return allInfoForAllVars
	

##print("Testing if keeping certain variants is working or not")
##print(keepVariantsAtTheseLoci())



def removeVariantsAtTheseLoci(): 
	allReturned=[]
	allReturned=Main()
	varsToKeepBool=(allReturned.keepLoci)
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	variantsExtracted = modifyFileWithLociToExtractVars()
	allInfoForAllVars=[]
	if(varsToKeepBool==False):
		for aVar in variantsExtracted:
			eachLociIndexInListByChr=extractOneVariantIndex(aVar)
			if(eachLociIndexInListByChr != -1):
				print(eachLociIndexInListByChr)
				print(listSortedByChrLoci[eachLociIndexInListByChr])
				##variantToRemove=listSortedByChrLoci[eachLociIndexInListByChr]
				listSortedByChrLoci.pop(eachLociIndexInListByChr)
	return listSortedByChrLoci
	
##allLociExtracted=removeVariantsAtTheseLoci()
##print("The variants extracted after removing some vars")
##print(allLociExtracted)


def keepOnlyIndels(): ## This is working fine
	allReturned=[]
	allReturned=Main()
	print(allReturned) ## returns ['sample.vcf', '20']
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	indelBoolean=allReturned.Indel
	
	allIndelVariantsToKeep=[]
	if(indelBoolean==True): ## This is a boolean argument
		for variant in listSortedByChrLoci:
			refVar=variant[3]
			altVar=variant[4]
			if((len(refVar)!=len(altVar)) or refVar=='.' or altVar=='.'):
				print("This is an indel var")
				allIndelVariantsToKeep.append(variant)	
	return allIndelVariantsToKeep
	
	
print("Testing if keepOnlyIndels() is working or not")
##print(keepOnlyIndels())

def removeIndels(): ## This is working fine
	allReturned=[]
	allReturned=Main()
	print(allReturned) ## returns ['sample.vcf', '20']
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	indelBoolean=allReturned.Indel
	
	allSNVariantsToKeep=[]
	if(indelBoolean==False): ## This is a boolean argument
		for variant in listSortedByChrLoci:
			refVar=variant[3]
			altVar=variant[4]
			if(len(refVar)==len(altVar)):
				##print("This is a snp")
				allSNVariantsToKeep.append(variant)	
	return allSNVariantsToKeep
	
	
print("Testing if removeIndels() is working or not")
##print(removeIndels())
##print(len(removeIndels()))


def retrieveGenotypeInfoForAllVar(): ### keeping missing genotypes as well, working fine
	
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	genotypesAllVar=[]
	for eachVar in listSortedByChrLoci:
		##dictOfAlleleFreq={}
			##print("This is a call to the retrieveGenotypeInfoForAllVar() function")
			genoTypes=eachVar[8:len(eachVar)-1]
			variantLoci=eachVar[0:2]
			variantAlleles=eachVar[3:5]
			newGenotypeList=[]
		##genotypeInfoPerVar=variantLoci+variantAlleles+genoTypes
			for eachGenotype in genoTypes:
				newGenotypeList.append(eachGenotype)
				genotypeInfoPerVar=variantLoci+variantAlleles+newGenotypeList
		##print(len(genoTypes))
			genotypesAllVar.append(genotypeInfoPerVar)
	return genotypesAllVar
	
print("Testing if retrieveGenotypeInfoForAllVar() function is working or not")
##print(retrieveGenotypeInfoForAllVar()) ## Giving expected output

def functionToReturnGenotypes():
	allReturned=[]
	allReturned=Main()
	genotypesAllVar=[]
	retrieveGenotype=allReturned.getGenotypes
	if(retrieveGenotype==True):
		print("This is a call to the retrieveGenotypeInfoForAllVar() function")
		genotypesAllVar=retrieveGenotypeInfoForAllVar()
	return genotypesAllVar

print("Testing if boolean function to return genotypes is working or not")		
##print(functionToReturnGenotypes())	 ## Giving expected output	

def determineGenotypeCount(): ## Working fine
	variantLociWithGenotypes=retrieveGenotypeInfoForAllVar()
	dictOfGenotypeCount={}
	for eachVar in variantLociWithGenotypes:
		genotypesList=eachVar[5:] ## a list
		listOfAllPossibleAlleleFreq=[]
		heterozygoteCount=0
		homozygoteRefCount=0
		homozygoteAltCount=0
		listOfGenotypesPervar=[]
		for aGenotype in genotypesList:
			genotypeStringSplit=re.split(':',aGenotype)
			genotypeExtracted=genotypeStringSplit[0]
			listOfGenotypesPervar.append(genotypeExtracted)
		heterozygoteCount=listOfGenotypesPervar.count('0/1')
		homozygoteRefCount=	listOfGenotypesPervar.count('0/0')
		homozygoteAltCount=listOfGenotypesPervar.count('1/1')
		totalGenotypeCount=heterozygoteCount+homozygoteRefCount+homozygoteAltCount
		listOfAllPossibleAlleleFreq.extend([homozygoteRefCount,heterozygoteCount,homozygoteAltCount,totalGenotypeCount])
		##listOfAllPossibleAlleleFreq.extend([float("{0:.2f}".format(homozygoteRefCount/totalGenotypeCount)),float("{0:.2f}".format(heterozygoteCount/totalGenotypeCount)),float("{0:.2f}".format(homozygoteAltCount/totalGenotypeCount))])

		keyForDict=eachVar[0:4]
		keyForDictStr=[str(x) for x in keyForDict]
		locusInfoPerVar=':'.join(keyForDictStr)
		dictOfGenotypeCount[locusInfoPerVar]=listOfAllPossibleAlleleFreq
	return dictOfGenotypeCount	

##print("Displaying genotype count")
##print(determineGenotypeCount()) ## THERE IS OUTPUT HERE

def alleleCountByVariant():  ## Working fine
	dictOfGenotypeCount={}
	dictOfAlleleCount={}
	dictOfGenotypeCount=determineGenotypeCount()
	for variant,genotypeCount in dictOfGenotypeCount.items():
		alleleCountList=[]
		refAlleleCount=2*(genotypeCount[0])+genotypeCount[1]
		altAlleleCount=genotypeCount[1]+2*(genotypeCount[2])
		alleleCountList.append(refAlleleCount)
		alleleCountList.append(altAlleleCount)
		dictOfAlleleCount[variant]=alleleCountList
	return dictOfAlleleCount


## python3 vcfAnnotatorWithArgParse.py --vcf sampleChr1Chr10.vcf --getAlleleCount True

def functionToReturnAlleleCount():
	allReturned=[]
	allReturned=Main()
	alleleCountByVar={}
	retrieveAlleleCount=allReturned.getAlleleCount
	if(retrieveAlleleCount==True):
		print("This is a call to the alleleCountPerVariant() function")
		alleleCountByVar=alleleCountByVariant()
	return alleleCountByVar
	
##print(functionToReturnAlleleCount())
print("Displaying allele count")
##print(functionToReturnAlleleCount()) ## Working fine 

## python3 vcfAnnotatorWithArgParse.py --vcf sampleChr1Chr10.vcf --getAlleleCount True

def getAlleleFrequency():
	dictOfAlleleFreq={}
	dictOfAlleleCount={}
	dictOfAlleleCount=alleleCountByVariant()
	for variant,genotypeCount in dictOfAlleleCount.items():
		listOfAllPossibleAlleleFreq=[]
		refAlleleFreq=genotypeCount[0]/(genotypeCount[0]+genotypeCount[1])
		altAlleleFreq=genotypeCount[1]/(genotypeCount[0]+genotypeCount[1])
		listOfAllPossibleAlleleFreq.extend([float("{0:.2f}".format(refAlleleFreq)),float("{0:.2f}".format(altAlleleFreq))])
		##listOfAlleleFreq.append(refAlleleFreq)
		##listOfAlleleFreq.append(altAlleleFreq)
		dictOfAlleleFreq[variant]=listOfAllPossibleAlleleFreq
	return dictOfAlleleFreq




def functionToReturnAlleleFreq():
	allReturned=[]
	allReturned=Main()
	alleleCountByFreq={}
	retrieveAlleleCount=allReturned.getAlleleFreq
	if(retrieveAlleleCount==True):
		print("This is a call to the alleleCountPerVariant() function")
		alleleCountByFreq=getAlleleFrequency()
	return alleleCountByFreq
	
print("Testing getting allele frequency")
##print(functionToReturnAlleleFreq())

## python3 vcfAnnotatorWithArgParse.py --vcf sampleChr1Chr10.vcf --getAlleleFreq True



def functionToAddDPToEndOfList(): 
	variantsWithDPAtEnd=[]
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	print("Calling from within getIndexWithDP() function")
	##print(listSortedByChrLoci)
	for index in range(0,len(listSortedByChrLoci)):
		variant=listSortedByChrLoci[index]
		dpFieldVal=variant[7]
		dpFieldValFound=re.findall('(DP=\d+)',dpFieldVal) ## 
		##print(dpFieldValFound)
		##dpValue=dpFieldValSplit[2]
		dpList=re.split("=",dpFieldValFound[0])
		##print(dpList)
		dpAsInt=int(dpList[1])
		variant.append(dpAsInt)
		variantsWithDPAtEnd.append(variant)
		##listOfVariants.append(variant)
	return variantsWithDPAtEnd

print("Testing converting DP to int")
##variantsWithDPAsIntAtEndOfList=functionToAddDPToEndOfList()
####print(len(variantsWithDPAsIntAtEndOfList))


def sortByDP(variantsWithDPAsIntAtEndOfList): ## WORKING
	if(len(variantsWithDPAsIntAtEndOfList) < 2):
		return variantsWithDPAsIntAtEndOfList
	listSortedByDP=[]
	mid=int(len(variantsWithDPAsIntAtEndOfList)/2)
	leftList=sortByDP(variantsWithDPAsIntAtEndOfList[:mid])
	rightList=sortByDP(variantsWithDPAsIntAtEndOfList[mid:])
	while(len(leftList) > 0) and (len(rightList) > 0):
		if(leftList[0][len(leftList[0])-1] > rightList[0][len(rightList[0])-1]):
			listSortedByDP.append(rightList[0])
			rightList.pop(0)
		else:
			listSortedByDP.append(leftList[0])
			leftList.pop(0)
	listSortedByDP=listSortedByDP+leftList
	listSortedByDP=listSortedByDP+rightList

	return listSortedByDP




def functionToCallDPSort():
	variantsWithDPAtEnd=functionToAddDPToEndOfList()
	variantsSortedByDP=sortByDP(variantsWithDPAtEnd)
	return variantsSortedByDP

##print("Testing if ascending merge sort by DP is working or not")
##variantsSortedByDP=functionToCallDPSort()
##print(variantsSortedByDP)
	

def findIndexOfVarWithDPLessThanParticularDP(): ## logic is okay
	allReturned=[]
	allReturned=Main()
	minDPSupplied=allReturned.minDP
	print("This is the user minimum DP arguement")
	print(minDPSupplied)
	DPAsInt=int(minDPSupplied[0])
	variantsSortedByDP=functionToCallDPSort()
	theIndexToSearchFor=0
	for index in range(0,len(variantsSortedByDP)):
		aVariant=variantsSortedByDP[index]
		if(aVariant[len(aVariant)-1] >= DPAsInt):
			return index
			break
		else:
			if(DPAsInt <= aVariant[len(aVariant)-1]) and (index==len(variantsSortedByDP)-1):
				return (len(variantsSortedByDP)-1) ## such that last variant gets returned
		
##print("Testing find index of var with DP just below choice of threshold")
##print(findIndexOfVarWithDPLessThanParticularDP())
##indexReturned=findIndexOfVarWithDPLessThanParticularDP()
##print(indexReturned)
##print(variantsSortedByDP[indexReturned])


def returnTheVariantsWithDPAboveMin(): ## logic is okay
	indexAboveMinDP=findIndexOfVarWithDPLessThanParticularDP()
	variantsSortedByDP=functionToCallDPSort()
	return (variantsSortedByDP[indexAboveMinDP:])


##print("These are the variants with DP above minimum DP")
##print(returnTheVariantsWithDPAboveMin()) ## This is working fine



def determineBaseChangeOfSpecificType(originalBase,changedBase):
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	countOfParticularTypeOfBaseChange=0
	for aVariant in listSortedByChrLoci:
		refBase=aVariant[3]
		altBase=aVariant[4]
		if(len(refBase)==len(altBase)):
			if(refBase==originalBase) and (altBase==changedBase):
				countOfParticularTypeOfBaseChange=countOfParticularTypeOfBaseChange+1
	return countOfParticularTypeOfBaseChange
	

def determineNoOfTransitions(): ## logic is okay
	dictOfAllTypesOfTransitions={}
	listOfAllTransitions=[["A","G"],["G","A"],["T","C"],["C","T"]]
	for aBasePair in listOfAllTransitions:
		originalBase=aBasePair[0]
		changedBase=aBasePair[1]
		noOfBaseChanges=determineBaseChangeOfSpecificType(originalBase,changedBase)
		changeRepresentation=originalBase+ "->" + changedBase
			##print("Base change type is")
			##print(changeRepresentation)
			##print("No of changes is")	
			##print(noOfBaseChanges)		
		dictOfAllTypesOfTransitions[changeRepresentation]=noOfBaseChanges
	return dictOfAllTypesOfTransitions


##print("Checing if transition count dict is working or not")
##print(determineNoOfTransitions())

def determineNoOfTransversions():
	dictOfAllTypesOfTransversions={}
	listOfAllTransversions=[["A","C"],["C","A"],["A","T"],["T","A"],["C","G"],["G","C"],["G","T"],["T","G"]]
	for aBasePair in listOfAllTransversions:
		originalBase=aBasePair[0]
		changedBase=aBasePair[1]
		noOfBaseChanges=determineBaseChangeOfSpecificType(originalBase,changedBase)
		changeRepresentation=originalBase+ "->" + changedBase
		dictOfAllTypesOfTransversions[changeRepresentation]=noOfBaseChanges
	return dictOfAllTypesOfTransversions

##print("Checing if transversion count dict is working or not")
##print(determineNoOfTransversions())

def returnEitherTransitionOrTransversion():
	allReturned=[]
	allReturned=Main()
	tsArg=allReturned.getTs
	tvArg=allReturned.getTv
	if(tsArg==True):
		return determineNoOfTransitions()
	else:
		if(tvArg==True):
			return determineNoOfTransversions()

##print("Checking if returnEitherTransitionOrTransversion() is working or not")
##print(returnEitherTransitionOrTransversion())
## python3 vcfAnnotatorWithArgParse.py --vcf sampleChr1Chr10.vcf --getTv Tv
##python3 vcfAnnotatorWithArgParse.py --vcf sampleChr1Chr10.vcf --getTs Ts

def returnSummaryOfTransitionAndTransversion():
	allReturned=[]
	allReturned=Main()
	tstvArg=allReturned.getTsTv
	if(tstvArg==True):
		listSummaryOfChanges=[]
		dictOfTransitions=determineNoOfTransitions()
		dictOfTransversion=determineNoOfTransversions()
		listSummaryOfChanges.append(dictOfTransitions)
		listSummaryOfChanges.append(dictOfTransversion)
	return listSummaryOfChanges
	
##print("Checking whether the returnSummaryOfTransitionAndTransversion() function is working or not")
##print(returnSummaryOfTransitionAndTransversion())
## python3 vcfAnnotatorWithArgParse.py --vcf sampleChr1Chr10.vcf --getTsTv TsTv


## Two functions needed of which one is to write filtered variants to VCF and statistics generation output to a file
