# Code from https://mitchfournier.com/2011/10/11/how-to-import-a-csv-or-tsv-file-into-a-django-model/
from eship import settings
import django
import codecs
from decimal import *
# Full path and name to your csv file 
csv_filepathname="diagnostics.csv" 
# Full path to your django project directory 
your_djangoproject_home="diagassist/" 
import sys,os,csv
sys.path.append(your_djangoproject_home) 
os.environ['DJANGO_SETTINGS_MODULE'] = 'eship.settings' 
django.setup()

# Lines 16-23 from https://stackoverflow.com/questions/13590749/reading-unicode-file-data-with-bom-chars-in-python
bytes = min(32, os.path.getsize(csv_filepathname))
raw = open(csv_filepathname, 'rb').read(bytes)
if raw.startswith(codecs.BOM_UTF8):
    encoding = 'utf-8-sig'
else:
    result = chardet.detect(raw)
    encoding = result['encoding']
from diagassist.models import Diagnostic
openFile = open(csv_filepathname, encoding=encoding)
dataReader = csv.reader(openFile, delimiter=',', quotechar='"') 
for row in dataReader:
	diag = Diagnostic() 
	print(row[0])
	print(type(row[0]))
	diag.ICD9 = Decimal(row[0])
	diag.ICD10 = row[1] 
	diag.name = row[2] 
	diag.page = row[3] 
	diag.save()
	