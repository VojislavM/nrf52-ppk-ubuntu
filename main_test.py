import os
import subprocess

ppk_api_path = '~/Documents/nrf/ppk_py/ppk_api/main.py'

#get ppk jlink id
responce = subprocess.getstatusoutput("nrfjprog -i")
ppk_id = responce[1]

print('PPK J-link ID is: ' + ppk_id)

#get ppk jlink id
responce = subprocess.getstatusoutput("python3 " + ppk_api_path + " -s " + ppk_id + " -a 2 -p 1 -o ./res/graph1 -z -k -v")
ppk_average = responce[1]

print('PPK average: ' + ppk_average)