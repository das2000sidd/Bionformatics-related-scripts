# Bionformatics-related-scripts

Annovar Using Python Documentation: (annovarUsingPython.py)
Some sample usage is:

python3 annovarUsingPython.py --vcf onlySixVariants.vcf --humandbDirPath ./humandb --buildver hg19 --out onlySixVariantsAnnotated --protocol refGene,snp135 --operation g,f --nastring .

Above script annotates a vcf with gene and dbsnp135 annotation.

python3 annovarUsingPython.py --vcf onlySixVariants.vcf --humandbDirPath ./humandb --buildver hg19 --out onlySixVariantsAnnotated --protocol esp6500ea --operation f --nastring .


ABove script filters as per the esp6500ea database variant allele frequency.

## IMP : Before running the script download the database and create a folder called humandb in folder where your annovar perl scripts are
## Put all databases in humandb
## Just check annovar's documentation for that
## The way this script is know python script and perl script have to be in the same directory 
## This only uses the table_annovar.pl function. So you can use any of the functionality of that tool.

Just type: python3 annovarUsingPython.py -h for instructions to supply command line arguments


Download UCSC source file documentation: (downloadUCSChg19DatabaseFile.py)

This python script can be used to download any hg19 based database from the UCSC downloads. It works for all file names of the format .txt.gz. Run the script as below:

python3 downloadFileAsFunc.py --typeOfDatabase affyCytoScan

The above script will download the file affyCytoScan.txt.gz and save it in your current directory.


Generate ped and map file from VCF file: (generatePedFile.py)


This is a python script that generates ped and map file compatibe with plink from a VCF file with multiple samples. Since plink only accepts snps, it will exclude indels from the vcf in the generated ped and the map file.

To run it type:

python3 generatePedFile.py --vcf myVcf.vcf --out myVcfPlinkFormat


Analyse a VCF file: (vcfAnalyser.py)

This is a python script that can be used to analyse a VCF file for some general information, as well as filter VCF file using various criterions. The various functionalities with sample scripts are in the word document.


