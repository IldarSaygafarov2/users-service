# Users-service


## Installation

* Clone repository
```shell
# ssh
git clone git@github.com:IldarSaygafarov2/DRF-test-app.git

# or https
git clone https://github.com/IldarSaygafarov2/DRF-test-app.git
```

## Install environment vars
* rename `example.env` to `.env` and set all values to actual values

## Run
Run project with make
```shell
make run

# RUN IT MANUALLY WITH SETTINGS
# dev
python manage.py runserver --settings=core.settings.dev

# with prod settings manually
python manage.py runserver --settings=core.settings.prod
```
## !!!WARNING!!!
Don't use make run on production(use gunicorn/uvicorn etc.)