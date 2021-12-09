# Academic and Co-Curricular Activity Council IITJ

## Web portal and forum for Students' Gymkhana of IIT Jodhpur

### Purpose

Simplify the workflow of updating the gymkhana website without much knowledge on how to code. And also provide certain utility features.

This project includes:

- A main `web portal` which can be updated dynamically through an admin interface.
- A `forum/discussion` app for general purpose discussions.
- An app called `Konnekt` to find/search people with a certain required skill set.

### Installation:

Requirements:

- Python 3.6 runtime
- Django >= 3.2.9
- Other dependencies in `Pipfile`

Procedure:

Setup Frontend:

If you haven't already, install the vue-cli service:  
`npm install -g @vue/cli`

Then follow these steps:

```
git clone https://github.com/devlup-labs/gymkhana-acac

cd <project-directory>/acac_frontend/

npm install
```

- Compiles and hot-reloads for development

```
npm run serve
```

- Compiles and minifies for production

```
npm run build
```

- Lints and fixes files

```
npm run lint
```

Setup Backend:

Make sure you have python 3.6 and pipenv installed on your pc.

Then follow these steps:

```
cd <project-directory>/acac_backend/

cp .env.example .env
```

```
pipenv --python 3.6 install --dev
```

- Activate the new virtual environment:

```
pipenv shell
```

- Make database migrations

```
python manage.py makemigrations
python manage.py migrate
```

- Create a superuser

```
python manage.py createsuperuser
```

- Run development server on localhost

```
python manage.py runserver
```

#### Dummy Data for Testing [OPTIONAL]:

This will populate the database with random values for testing:

```
python manage.py createfixture
```
