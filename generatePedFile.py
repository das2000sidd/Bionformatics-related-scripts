import time
import re
import sys
import argparse


def generatePed(b):
	if(len(b) < 1):
		raise ValueError('Error: Cannot parse empty string into boolean')
	if(b=='True'):
		return True
	if(b=='False'):
		return False
	raise ValueError('Error: Cannot parse string into boolean')

def Main():
	listOfArguements=[]
	parser=argparse.ArgumentParser(description='This is a tool similar to vcftools written in python')
	parser.add_argument('--vcf',nargs='?')
	parser.add_argument('--generatePed',type=generatePed)
	parser.add_argument('--out',nargs='?')
	
	##parser.add_argument('--getTsTv',type=)
	
	args=parser.parse_args()
	return args
	
	
	
	
if __name__=='__main__':
	Main()
	
	
	
def readTestFile(): ## Working fine
	allReturned=[]
	allReturned=Main()
	vcfSupplied=allReturned.vcf
	handle=open(vcfSupplied,'r')
	lines="\n"
	for line in handle:
		lines+=line
	handle.close()
	return lines
	
vcfRead = readTestFile() ## a multi sample vcf


def extractLinesWithVariants(): ## Working fine
	allReturned=[]
	allReturned=Main()
	vcfLinesToSplit=readTestFile()
	linesRead = re.split("\n",vcfLinesToSplit)
	return linesRead


linesToAList=extractLinesWithVariants()
print('\n')


def getOnlyVariantsFromList(): ## Working fine
	OnlyVariants=[]
	indexOfHeaderLine=0
	linesToAList=extractLinesWithVariants()
	##print("\n")
	for eachLine in linesToAList:
		
		if('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT' in eachLine):
			indexOfHeaderLine=linesToAList.index(eachLine)
			for anIndex in range(indexOfHeaderLine,len(linesToAList),1):
				splittingTheLinesToAList=re.split('\t',linesToAList[anIndex])
				OnlyVariants.append(splittingTheLinesToAList)
		
		
	return OnlyVariants


def getAllLinesBeforeChromLine(): ## Working fine
	
	indexOfHeaderLine=0
	linesToAList=extractLinesWithVariants()
	##print("\n")
	OnlyLines=[]
	indexOfHeaderLine=0
	for eachLine in linesToAList:
		
		if('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT' in eachLine):
			indexOfHeaderLine=linesToAList.index(eachLine)
			OnlyLines=linesToAList[0:indexOfHeaderLine+1]
		
		
	return OnlyLines



def convertRemoveChrWordAndMakeLociInfoInt():
	
	variantsReturned=getOnlyVariantsFromList()
	variantsReturned=variantsReturned[1:len(variantsReturned)-1]
	allVariants=[]
	for aVariant in variantsReturned:
		eachVarList=[]
		chrWord=aVariant[0]
		chrWordSplit=re.findall("\d+",chrWord)		
		intChr=int(chrWordSplit[0]) 
		intLoci=int(aVariant[1])
		eachVarList.extend([intChr,intLoci]) ## This is chr start and stop as integer
		listWithOutLoci=aVariant[2:len(aVariant)] ## This is the list without chr start and stop
		varListToReturn=eachVarList+listWithOutLoci
		allVariants.append(varListToReturn)
		
	return allVariants


def sortByChrLoci(listWithQualScoreFloatAndLociInt): ## not sure how to do it especially with the recursion
	
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


def retrieveGenotypeForFormingPedAllVar(): ### keeping missing genotypes as well, working fine
	allLinesBeforeChromLine=getAllLinesBeforeChromLine()
	headerLine=allLinesBeforeChromLine[-1]
	headerLineSplitted=re.split('\t',headerLine)
	headerLinePartToAppend=headerLineSplitted[0:2]+headerLineSplitted[3:5]+headerLineSplitted[8:]
	listWithQualScoreFloatAndLociInt=convertRemoveChrWordAndMakeLociInfoInt()
	listSortedByChrLoci=sortByChrLoci(listWithQualScoreFloatAndLociInt)
	listToReturn=[]
	genotypesAllVar=[]
	for eachVar in listSortedByChrLoci:
			genoTypes=eachVar[8:]
			variantLoci=eachVar[0:2]
			variantAlleles=eachVar[3:5]
			newGenotypeList=[]
			for eachGenotype in genoTypes:
				newGenotypeList.append(eachGenotype)
				genotypeInfoPerVar=variantLoci+variantAlleles+newGenotypeList
			genotypesAllVar.append(genotypeInfoPerVar)
	listToReturn.append(headerLinePartToAppend)
	listToReturn.extend(genotypesAllVar)
	return listToReturn
	




def functionToFormDictOfGenotypeBySampleInPlinkStyle(oneIndv):
	genotypeInfoRetrieved=retrieveGenotypeForFormingPedAllVar()
	onlyVariantInfo=genotypeInfoRetrieved[1:]
	onlyHeader=genotypeInfoRetrieved[0]
	
	listOfAllGenoPerIndiv=[]
	noOfVariants=0
	indexOfindiv=onlyHeader.index(oneIndv)
	for aVariant in onlyVariantInfo:
		refAllele=aVariant[2]
		altAllele=aVariant[3]
		if(len(refAllele)==len(altAllele)):
			noOfVariants=noOfVariants+1
			genotypeOfVariant=aVariant[indexOfindiv]
			listOfAllelePerGenotype=[]
			if(genotypeOfVariant!='.'):
				genotypeSplitted=re.split(':',genotypeOfVariant)
				actualGenotype=genotypeSplitted[0]
			
				if(actualGenotype=='0/0'):
					listOfAllelePerGenotype.extend([refAllele,refAllele])
				elif(actualGenotype=='0/1'):
					listOfAllelePerGenotype.extend([refAllele,altAllele])
				else:
					if(actualGenotype=='1/1'):
						listOfAllelePerGenotype.extend([altAllele,altAllele])
			else:
				listOfAllelePerGenotype.extend(['0','0'])
			listOfAllGenoPerIndiv.append(listOfAllelePerGenotype)
	
	return 	listOfAllGenoPerIndiv
	




def formingTheMapFile():
	genotypeInfoRetrieved=retrieveGenotypeForFormingPedAllVar()
	onlyVariantInfo=genotypeInfoRetrieved[1:]
	mapFormatAllVariants=[]
	for aVariant in onlyVariantInfo:
		if(len(aVariant[2])==len(aVariant[3])):
			eachLineOfMap=[]
			chrNo=aVariant[0]## the chromosome
			chrNoAsString=str(chrNo)
			posOnChr=str(aVariant[1])
			secondColOfMap="chr"+str(chrNo)+":"+posOnChr
			eachLineOfMap.extend([chrNoAsString,secondColOfMap,'0',posOnChr])
			mapFormatAllVariants.append(eachLineOfMap)
	return mapFormatAllVariants
	

		

		
		
					
def functionToReturnPedForAllSample():
	genotypeInfoRetrieved=retrieveGenotypeForFormingPedAllVar()
	onlyHeader=genotypeInfoRetrieved[0]
	allSampleId=onlyHeader[5:]
	dictOfGenoForPlink={}
	for aSampleId in allSampleId:
		plinkGenoFormatForASample=functionToFormDictOfGenotypeBySampleInPlinkStyle(aSampleId)
		dictOfGenoForPlink[aSampleId]=plinkGenoFormatForASample
	return dictOfGenoForPlink
	
	


def finalPedFormatToWriteToFile():
	pedDataForAllSamples= functionToReturnPedForAllSample()
	listOfAllPedToWriteToFile=[]
	for sampleId,genotypeInfo in pedDataForAllSamples.items():
		pedLinePerSample=[]
		pedLinePerSample.extend([sampleId,sampleId,'0','0','0','0'])
		for eachGenoList in genotypeInfo:
			pedLinePerSample.extend(eachGenoList)
		listOfAllPedToWriteToFile.append(pedLinePerSample)
	return listOfAllPedToWriteToFile
		
			
		
		
				
def writeAnyNonVCFToFile(dataToWriteToFile,choiceOfFileName,choiceOfFileExt):
	lineList=[]
	for anyLine in dataToWriteToFile:
		anyLineAsString=[str(anyLine[i]) for i in range(0,len(anyLine))]
		aLineAsStringTabbed='\t'.join(anyLineAsString)
		lineList.append(aLineAsStringTabbed)
	f=open('{}.{}' .format(choiceOfFileName,choiceOfFileExt),'w')
	for line in lineList:
		f.write(line+'\n')
	f.close()	
		
def writePedDataToFile():
	allReturned=[]
	allReturned=Main()
	fileName=allReturned.out
	pedDataToWrite=	finalPedFormatToWriteToFile()
	
	writeAnyNonVCFToFile(pedDataToWrite,fileName,'ped')
		
def writeTheMapToFile():
	allReturned=[]
	allReturned=Main()
	fileName=allReturned.out
	mapToWriteToFile=formingTheMapFile()
	writeAnyNonVCFToFile(mapToWriteToFile,fileName,'map')	

def callThePedAndMapWriteFunctions():
	writePedDataToFile()
	writeTheMapToFile()
	



callThePedAndMapWriteFunctions()	