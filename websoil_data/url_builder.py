import os
import sys
import glob

file_store = "https://websoilsurvey.sc.egov.usda.gov/DSD/Download/Cache/SSA/"
all_unclean_zip_urls = glob.glob("./unclean_zip_urls/unclean_*.txt")
clean_zip_urls_dir = "./clean_zip_urls/clean_*.txt"
zips = []


for unclean_urls in all_unclean_zip_urls:
    print(unclean_urls)
exit()
with open("./unclean_zip_urls/unclean_ca_zip_urls.txt", 'r') as f:
    for line in f:
        # discard newlines
        if(len(line) > 1):
            #print(line)
            zip_name = file_store + line.strip().strip('\n')
            zips.append(zip_name)
print(zips)