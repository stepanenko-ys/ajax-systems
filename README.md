# Ajax Systems

## Installation

#### 1. Create virtualenv and activate:
```bash
pip install virtualenv
virtualenv -p python3 venv
```

#### 2. Activate virtualenv:

###### (for Linux and macOS)
```bash
source venv/bin/activate
```

###### (for Windows)
```bash
venv\scripts\activate.bat
```


#### 3. Requirements
```bash
cd ajax-systems
pip install -r requirements.txt
```

#### 4. Database
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

*  **  **

## Run backend
```bash
python manage.py run
```

*  **  **

## Fill the table with test data
Submit your Endpoint request (method POST, Headers can be empty):
```bash
/api_v1/upload
```
Body:
```bash
{
    "file": [upload your file "test_results.csv"]
}
```

###### After that, all data from the "test_results.csv" file will be automatically added to the database in the "Device" table

*  **  **

* Project was tested on manOS Catalina 
* Version 10.15.7
