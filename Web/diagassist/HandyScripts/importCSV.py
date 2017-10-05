# Code from https://mitchfournier.com/2011/10/11/how-to-import-a-csv-or-tsv-file-into-a-django-model/
# Full path and name to your csv file 
csv_filepathname="diagnostics.csv" 
# Full path to your django project directory 
your_djangoproject_home="" 
import sys,os,csv
sys.path.append(your_djangoproject_home) 
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 

from diagassist.models import Diagnostic
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 
for row in dataReader:
	diag = Diagnostic() 
	diag.ICD9 = row[0] 
	diag.ICD10 = row[1] 
	diag.name = row[2] 
	diag.page = row[3] 
	diag.save()
	