import sys
import io
import requests
import zipfile
import csv
import codecs


r = requests.get("http://www.fia.gov.tw/opendata/bgmopen1.zip")

with zipfile.ZipFile(io.BytesIO(r.content), 'r') as zf:
  csv_file = zf.read('BGMOPEN1.csv')
  print (type(csv_file))

csv_data = list(csv.reader(codecs.iterdecode(csv_file, 'utf-8'), delimiter=','))
print (csv_data[0])
#for row in csv_data:
	#print (row)


