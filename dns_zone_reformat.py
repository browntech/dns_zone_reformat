#This script takes zonefiles from DynDNS and combines their entries into a csv file
#Make sure zones/ folder exists in the same DIR as this file

from os import listdir
from os.path import isfile, join

def rw_file(file):
	#outputFile = open("dns_entries.csv", "a")
	lineNum = 0
	domain = ''
	subdomain = []
	forItem = []
	forFile = []
	file = open(file)
	for line in file:
		if(line.startswith("$ORIGIN") and lineNum == 0):
			domain = line.split(" ")[1].strip()[:-1]
			#print("Domain: %s" % domain)
			lineNum = 1;
		if not line.startswith(("                      ", "$ORIGIN","@","default","*","_")):
			sub = line.split(" ")[0].strip()
			if sub:
				if not sub in subdomain:
					subdomain.append(sub)
	#print('Results:')
	for sub in subdomain:
		#print(sub + ' ' + domain)
		lineInFile = sub + "," + domain + "," + sub + "." + domain
		#print(lineInFile)
		outputFile.write(lineInFile + '\n')

def list_files():
	for file in listdir(zonePath): 
		if isfile(join(zonePath, file)):
			rw_file(join(zonePath,file))

output = []
zonePath = "zones/"

#Setup new file, if exists, overwrite
outputFile = open("dns_entries.csv", "w")
outputFile.write("Sub Domain, Domain, FQDN" + "\n")

#Start us off
list_files()

#And we're done!
print("Done!")