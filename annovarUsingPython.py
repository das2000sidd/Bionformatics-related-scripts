import subprocess ## to start new applications from python
import argparse ## for supplying command line arguments
import re




def Main():
	listOfArguments=[]
	parser=argparse.ArgumentParser(description="This is a tool that calls annovar from python")
	parser.add_argument('--vcf',nargs='?') ## User supplied vcf
	
	parser.add_argument('--buildver',nargs='?') ## What human genome version they will use hg18 or hg19
	## Annovar expects annotation file name of type hg19_ or hg18_. Example: hg19_snp135
	parser.add_argument('--out',nargs='?') ## arguement to assign a name to output file
	parser.add_argument('--protocol',nargs='?') ## the part of database name except for hg19_. So snp135 for hg19_snp135. 
	parser.add_argument('--operation',nargs='?') ## what is the operation type. There are 3 as per annovar. g,f,r. Look at annovar webpage for details
	## the number of arguments in protocol must equal no of arguments in operation. Else annovar throws its error
	parser.add_argument('--humandbDirPath',nargs='?') ## where are the databases located.
	## If database in current  directory ty[e "./humandb" else give full path to humandb
	parser.add_argument('--nastring',nargs='?')
	## if supposed nothing is found for the variant in annotation, what symbol to use. Common usage is "."
	args=parser.parse_args()
	return args ## List of whatever arguements user supplied
	
	
if __name__=='__main__':
	Main()




def functionToAnnotateUsingTableDotAnnovar():
	allArgsReturned=[] 
	allArgsReturned=Main() ## whatever arguement user supplied  is stored as a list
	vcfReturned=allArgsReturned.vcf ## access a particular arguement using the "dotArguementName" syntax
	## Line 37-42 is similar syntax to line 36 and they will be inputs to call of annovar
	allProtocols=allArgsReturned.protocol
	allTypesOfOperation=allArgsReturned.operation
	humanDbDirPath=allArgsReturned.humandbDirPath
	buildVer=allArgsReturned.buildver
	nameOfOutput=allArgsReturned.out
	typeOfOperation=[]
	allTypesOfOperationSplit=re.split(',',allTypesOfOperation) ## The --operation needs arguement separated by commas eg refGene,snp135
	## FOr line 44 I have followed annovar style of supplying arguements
	allProtocolsSplit=re.split(',',allProtocols)
	allTypesOfOperationSplitAsString=','.join(allTypesOfOperationSplit) ## The arguements have to be passed as string and so converting list of strings to strings separated by commas
	allProtocolsSplitAsString=','.join(allProtocolsSplit) ## Same idea as line 47
	print("This is type of operation")
	print(str(allTypesOfOperationSplitAsString)) ## User gets to see what are the supplied operations. Can be removed later if deemed unnecessary
	print("These are the protocol/annotation type names") 
	print(str(allProtocolsSplitAsString)) ## Same idea as line 50
	annovarScriptToExecute=("perl table_annovar.pl " + vcfReturned + " " + humanDbDirPath + " -buildver " + buildVer + " -out "
	+ nameOfOutput + " -remove " + " -protocol " + str(allProtocolsSplitAsString) + " -operation " + str(allTypesOfOperationSplitAsString) + " -nastring " + "." + " -vcfinput")
	print(annovarScriptToExecute) ## The actual perl script to be executed as a string
	subprocess.call(annovarScriptToExecute,shell=True) ## the call function of subprocess to call a program. Executes annovar script
	return 0	## A function needs a return statement. Has no specific purpose
	
## Sample scripts:	
## python3 callingPerlScriptUsingPython.py --vcf onlySixVariants.vcf --humandbDirPath ./humandb --buildver hg19 --out onlySixVariantsAnnotated --protocol refGene,snp135 --operation g,f --nastring .
##python3 callingPerlScriptUsingPython.py --vcf onlySixVariants.vcf --humandbDirPath ./humandb --buildver hg19 --out onlySixVariantsAnnotated --protocol esp6500ea --operation f --nastring .
## IMP : Before running the script download the database and create a folder called humandb in folder where your annovar perl scripts are
## Put all databases in humandb
## Just check annovar's documentation for that
## The way this script is know python script and perl script have to be in the same directory but we can modify that later to specify the path. I am not completely sure. We have to look into that.



functionToAnnotateUsingTableDotAnnovar()