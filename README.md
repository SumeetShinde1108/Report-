# Report Lab Installation 
## For free version (Report Lab PDF Toolkit)
```shell
pip install reportlab
```
## For paid versiom (Report Lab PLUS)
### Step 1) Visit the report lab website, purchase the Report Lab PLUS license. You will recieve credentials and access the private PyPI server.
### Step 2) Create pip confuguation file i Notepad as Administrator and create file as a %APPDATA%\pip\pip.conf
```
[global]
extra-index-url:https://username:password@plus.reportlab.com/pypi/
```
### step 3) Then install ReportLab PLUS by using pip
```
pip install reportlab-plus 
```
