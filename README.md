# Bionformatics-related-scripts

This is a python script that calls annovar for annotation. 

Some sample usage is:

python3 callingPerlScriptUsingPython.py --vcf onlySixVariants.vcf --humandbDirPath ./humandb --buildver hg19 --out onlySixVariantsAnnotated --protocol refGene,snp135 --operation g,f --nastring .
gives a vcf gene and dbsnp135 annotation.

##python3 callingPerlScriptUsingPython.py --vcf onlySixVariants.vcf --humandbDirPath ./humandb --buildver hg19 --out onlySixVariantsAnnotated --protocol esp6500ea --operation f --nastring .
filters as per the esp6500ea database variant allele frequency

## IMP : Before running the script download the database and create a folder called humandb in folder where your annovar perl scripts are
## Put all databases in humandb
## Just check annovar's documentation for that
## The way this script is know python script and perl script have to be in the same directory 