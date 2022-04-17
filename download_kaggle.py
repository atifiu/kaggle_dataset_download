from kaggle.api.kaggle_api_extended import KaggleApi
import subprocess
import os
import glob
#To authenticate with Kaggle use thsi link as reference https://www.kaggle.com/docs/api#getting-started-installation-&-authentication
api = KaggleApi()
api.authenticate()

#Provide the list of dataset to be downloaded in the format name_of_dataset_owner/dataset_name
list_search = ['shivamb/netflix-shows', 'sudalairajkumar/covid19-in-india']
for x in list_search:
    print(x)
    #datasets directory should be created at relative path i.e. path from where this script will be executed
    api.dataset_download_files(dataset=x, path='datasets', unzip=True)


# All files  ending with .csv
names = [os.path.basename(x) for x in glob.glob('datasets/*.csv')]
#print(names)
for with_ext in names:
    #os.path.splitext(with_ext)
    file_name = os.path.splitext(with_ext)[0]
    print(file_name)
    #Provide full path of sqlcl
    os.chdir(r"C:\sqlcl\sqlcl-21.4.1.17.1458\sqlcl\bin")

    #test.sql file should be placed in the bin directory of sqlcl or else provide the complete path
    subprocess.run(["sql",
                    "arup/arup@192.168.29.71:1521/testpdb1.localdomain",
                    "@",
                    r"test.sql", ""+file_name+"", ""+with_ext+"",
                    ";"])













