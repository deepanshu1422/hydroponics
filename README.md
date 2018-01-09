### Quick summary  ###

This is a Django powered web application for a hydroponics setup
run on a raspberry pi.

### Installation ###
NOTE: For Rasbian OS

##### Clone and Setup Repository
```sh
Clone and enter repo:
`git clone https://github.com/psheppard16/hydroponics`
`cd hydroponics`

Install pip:
`sudo apt-get install python-pip python3-pip`

Create and activate virtual environment:
`pip install virtualenv`
`virtualenv -p python3 venv`
`source venv/bin/activate`
```

##### Install Dependencies
```sh
Install pip requirements:
`pip install -r requirements.txt`

Install node:
`curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -`
`sudo apt-get install -y nodejs`

Install node requirements:
`npm install`

Create settings_secret.py using template:
`cp hydro/settings_secret.py.template hydro/settings_secret.py`

Enter random characters for the 'SECRET_KEY' in `settings_secret.py`:
SECRET_KEY='super random characters'

Collect static resources for main site:
`gulp` (`gulp watch` for continuous collection)

Collect static resources for admin site:
`python manage.py collectstatic`
```

##### Database Setup
```sh
Install sqlite3:
`sudo apt-get install sqlite3`

Make the database:
`cd databases`
`sqlite3 db.sqlite3`
`cd ..`

Make migrations: 
`python manage.py makemigrations`

Run migrations: 
`python manage.py migrate`

Create a super user:
`python manage.py createsuperuser`

Populate database with default models:
`python manage.py configure_hydro`

```

### Documentation

##### Contributing
```sh
Documentation is written with [Sphinx](http://www.sphinx-doc.org/en/stable/). 
The .rst files are located in the `sphinx` folder.

To open the documentation in your browser:
`python manage.py open-docs` 

To build the documentation after changes:
`python manage.py build-docs`
```

### Testing ###

##### Running tests locally
```sh
Run all tests:
`driver=chrome REMOTE_USER=admin python manage.py --keepdb`

Run specific tests: 
`driver=[driver] REMOTE_USER=admin python manage.py --keepdb testing.[test file].[test class].[test]`
```

### Production Server ###

##### Installation
```sh
Update apt-get:
`sudo apt-get update`

Install lynx to check the server status:
`sudo aptitude install lynx`

Install apache2, and wsgi:
`sudo apt-get install apache2 libapache2-mod-wsgi-py3`
```

##### Configutation
```sh
Enter settings dir:
`sudo nano /etc/apache2/sites-available/000-default.conf`

Add the following to the config file:

Alias /static [project path]/hydroponics/static
<Directory [project path]/hydroponics/static>
    Require all granted
</Directory>

<Directory [project path]/hydroponics/hydroponics>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

WSGIDaemonProcess hydroponics python-path=[project path]/hydroponics python-home=[project path]/hydroponics/hydroponicsenv
WSGIProcessGroup hydroponics
WSGIScriptAlias / [project path]/hydroponics/hydroponics/wsgi.py
```

##### Permissions
```sh
Create group for apache, and all users
`sudo groupadd super_group`
`sudo gpasswd -a www-data super_group` # if the apache user is www-data
`sudo gpasswd -a pi super_group`       # if you have a user named pi
`sudo gpasswd -a foo super_group`      # if you have a user named foo
...

Give super_group permission to access the database:
`sudo chown :super_group [project path]/hydroponics/databases/db.sqlite3`
`sudo chown :super_group [project path]/hydroponics/databases`
`sudo chmod 664 [project path]/hydroponics/databases/db.sqlite3`

Give super_group permission to access the logs:
`sudo chown :super_group [project path]/hydroponics/logs/db_sql.log`
`sudo chown :super_group [project path]/hydroponics/logs/hydro.log`
`sudo chown :super_group [project path]/hydroponics/logs`
`sudo chmod 664 [project path]/hydroponics/logs/db_sql.log`
`sudo chmod 664 [project path]/hydroponics/logs/hydro.log`

Give super_group permission to access the GPIO pins:
`sudo adduser www-data gpio` # if the apache user is www-data
`sudo adduser pi gpio`       # if you have a user named pi
`sudo adduser foo gpio`      # if you have a user named foo
...
```

##### Server Name
```sh
Add the name localhost to the new servername config file:
`echo "serverName localhost" | sudo tee /etc/apache2/conf-available/servername.conf

Enable the servername config file:
`sudo a2enconf servername`

Reload apache:
`sudo service apache2 reload`

Reolad the apache daemon:
`sudo systemctl daemon-reload`
```

##### Enabeling Changes
```sh
Restart apache to finalize configuration:
`sudo service apache2 restart`
```
    
##### Starting and Stopping the Server:
```sh
Start:
`sudo apachetcl start`

Stop:
`sudo apachetcl stop`

Restart:
`sudo apachetcl restart`
```