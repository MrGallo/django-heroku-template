#TODO: Add debug toolbar

### Set up c9 workspace
```sh
$ sudo pip3 install pipenv
$ pipenv --python 3.6
```

### Use the PipEnv
```sh
pipenv shell
```

### Start New Project
Create a directory for your project
```sh
$ mkdir projectname
$ cd projectname
```

Create a Pipfile
```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true


[packages]
django = "*"
gunicorn = "*"
psycopg2-binary = "*"
django-heroku = "*"
redgreenunittest = "*"
coverage = "*"
mixer = "*"


[requires]
python_version = "3.6"
```

### Install requirements
```sh
$ pipenv install
$ pipenv shell
```

### Create the Django project
```sh
$ django-admin startproject config
```

### Create the core application
```sh
$ python manage.py startapp core
```

### Config the database
In the `config/settings.py` file change `DATABASES` to:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'app_name',
        'USER': 'app_name',
        'PASSWORD': 'development',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

In the terminal:
```sh
$ psql
ubuntu=# CREATE DATABASE app_name;
ubuntu=# CREATE USER app_name;
ubuntu=# GRANT ALL ON DATABASE app_name to "app_name";
ubuntu=# ALTER USER app_name PASSWORD 'development';
ubuntu=# ALTER USER app_name CREATEDB;
```

Press `CTRL + d` to exit the `psql` shell.

If database shuts down, `sudo service postgresql restart`

### Verify setup
In the terminal start the local web server.
```sh
$ python manage.py runserver $IP:$PORT
```
To stop the server, in the terminal press `CTRL + D`.


## Testing
`python runtests.py`
`coverage run --source='.' runtests.py`
`coverage report -m`
`coverage html`


### Deploy
Following files must be at top level of repository.
```
Pipfile
Pipfile.lock
Procfile
```
If `Procfile` is at top level and not in the same folder as `manage.py`, edit the `Procfile`:
```
web: gunicorn --chdir django config.wsgi
```

#### Multiple settings files
[Article here](https://thinkster.io/tutorials/configuring-django-settings-for-production)

Set heroku Env Var `DJANGO_SETTINGS_MODULE` to `config.settings.production`.

[Multiple Heroku Environments](https://devcenter.heroku.com/articles/multiple-environments)