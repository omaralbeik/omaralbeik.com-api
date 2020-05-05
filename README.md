# Deprecation Notice

This repo is depreacted, refer to v3.0 [here](https://github.com/albeiks/omaralbeik.com)

---

# omaralbeik.com

> Source code for [my website](https://omaralbeik.com) backend API.

## Features

- `GET` / `POST` / `PUT` / `DELETE` endpoints using Django REST Framework.
- Modularized applications:
  - blog
  - snippets
  - projects
  - contents
- PostgreSQL or SQLite3.
- Results pagination and throttling.
- CMS Admin dashboard to edit database entries.
- Markdown support!
  - Write text in Markdown and get instant preview in the admin dashboard
  - Get text as `html` from the API to present in client

## Dependencies

This project requires [**Python3**](https://www.python.org/downloads/) and [**Django**](https://www.djangoproject.com/) to build, if they are not installed on your device, you should install them first.

## Getting Started

### Install Python dependencies

```sh
pip install -r requirements.txt
```

### Initial Server Setup

#### 1. Collect Static Files

```sh
./manage.py collectstatic
./manage.py migrate
```

#### 2. Create Django Database

```sh
./manage.py makemigrations
./manage.py migrate
```

#### 3. Create Admin account

```sh
./manage.py createsuperuser
```

> Users info can be changed later from *AUTHENTICATION AND AUTHORIZATION* section in the admin dashboard

### Running the server

```sh
./manage.py runserver -p 8000
```

### Administration Dashboard

Server admin dashboard can be accessed by visiting the URL `localhost:8000/admin`

## Contributing

Your feedback is always appreciated and welcomed. If you find a bug in the source code or a mistake in the documentation, you can help me by submitting an issue [**here**](https://github.com/omaralbeik/omaralbeik.com-api/issues). Even better you can submit a Pull Request with a fix :)

## License

This repo is released under the [MIT License](LICENSE).
