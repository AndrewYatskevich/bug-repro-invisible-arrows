# Bug Reproduce Invisible arrows django-grappelli 3.0.8

Repository to reproduce bug with calendar invisible arrows of django-grappelli 3.0.8.
Prev next links are invisible on Google Chrome Version 124.0.6367.118 (Official Build) (64-bit)

## Installation

### Pre-requisites

python 3.11.9

### Clone the repository to your local machine

`git clone https://github.com/AndrewYatskevich/bug-repro-invisible-arrows.git`

### Move to the root folder of the project

`cd bug-repro-invisible-arrows/`

### Create the .env file and fill it out

- Create the .env file `touch .env`
- Fill out the .env file by referring to .env.example

### Create venv using python 3.11.9

`python -m venv venv`

### Activate venv and install dependencies

```
source venv/bin/activate
pip install -r requirements.txt
```

### Run migrations, collect static and create superuser

```
cd bug_repro_invisible_arrows/
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### Run server and open post creation page to see the bug

`python manage.py runserver`
Open http://127.0.0.1:8000/admin/login/ and sign in.\
Go to http://127.0.0.1:8000/admin/posts/post/add/ and click on the date field calendar icon\
to see that prev and next links are invisible.

## License
MIT © [Andrew Yatskevich](https://github.com/AndrewYatskevich)
