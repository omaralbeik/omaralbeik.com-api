# omaralbeik.com API

## Table of Contents

- [**Features**](#features)
- [**Structure**](#structure)
  - [Data Models](#data-models)
  - [API Endpoints](#api-endpoints)
- [**Getting Started**](#getting-started)
- [**Make it Yours**](#make-it-yours)
- [**Deploying to your own server**](#deploying-to-your-own-server)
- [**Contributing**](#contributing)
- [**License**](#license)



## Features

- `GET` / `POST` / `PUT` / `DELETE` endpoints using Django REST Framework.
- Modularized applications:
  - blog
  - projects
  - contents
- PostgreSQL or SQLite3.
- Results pagination.
- Requests Throttling system.
- CMS Admin dashboard to edit database entries.
- Markdown support!
  - Write text in Markdown and get instant preview in the admin dashboard
  - Get text as `html` from the API to present in client


## Structure

#### Data Models

- [Blog](blog/models.py)
- [Projects](projects/models.py)
- [Contents](contents/models.py)

#### API Endpoints

- **REST Endpoints**
  - Blog:
    - `/v1/blog/posts/`: all blog posts.
    - `/v1/blog/posts/<post_id>/`: specific blog post.
  - Projects:
    - `/v1/projects/`: all projects.
    - `/v1/projects/<project_id>/`: specific project.
  - Contents:
    - `/v1/contents/`: all static contents.
    - `/v1/contents/<slider_id>/`: specific static content.


## Getting Started

#### Install dependencies

This project requires Python and Django to build, if they are not installed on your device, you should install them first.

1. [Python3](https://www.python.org/downloads/)
2. [Django](https://www.djangoproject.com/)
3. [Django REST Framework](http://www.django-rest-framework.org/)
4. [Pygments](https://github.com/odeoncg/django-pygments)
5. [Markdownx](https://github.com/neutronX/django-markdownx)
6. [Markdown2](https://github.com/trentm/python-markdown2)
7. [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers)

#### Install Python dependencies

```bash
$ pip3 install -r requirements.txt
```

#### Initial Server Setup

1. Collect Static Files
```bash
$ ./manage.py collectstatic
$ ./manage.py migrate
```

2. Create Django Database
```bash
$ ./manage.py makemigrations
$ ./manage.py migrate
```

3. Create Admin account
```bash
$ ./manage.py createsuperuser
```

_Note:_ users info can be changed later from *AUTHENTICATION AND AUTHORIZATION* section in the admin dashboard

#### Running the server

```bash
./manage.py runserver -p 8000
```

#### Administration Dashboard
Server admin dashboard can be accessed by visiting the URL `localhost:8000/admin`


## Make it Yours

## Deploying to your own server
- [Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04) by [Digitalocean](https://www.digitalocean.com).
- [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python) by [Heroku](https://www.heroku.com/).



## Contributing

Your feedback is always appreciated and welcomed. If you find a bug in the source code or a mistake in the documentation, you can help me by submitting an issue [**here**](https://github.com/omaralbeik/omaralbeik.com-api/issues). Even better you can submit a Pull Request with a fix :)



## License

This repo is released under the [MIT License](LICENSE).
