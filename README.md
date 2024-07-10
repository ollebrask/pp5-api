# Cold Beer

Cold Beer is my final project for Code Institute, serving as a vibrant platform designed for beer enthusiasts to explore and share their favorite brews. This site enables users to effortlessly browse posts about different beer varieties, breweries, and tasting experiences. The inclusion of user accounts allows individuals to create personalized posts, engage with the community through likes and comments, and track their favorite posts for future reference. A user-friendly contact form facilitates seamless communication with the site administrators.

Deployed API Heroku: [API link](https://pp5-olle-4b42abf5cfb4.herokuapp.com/)

Deployed Frontend Heroku: [Cold Beer](https://coldbeer-e9a4ef1fda7f.herokuapp.com/)

Backend Github [Repository](https://github.com/ollebrask/pp5-api)

Frontend Github [Repository](https://github.com/ollebrask/coldbeer)


## User Stories

I have created user stories with Github Issues and this is the [KANBAN board](https://github.com/users/ollebrask/projects/5/).

## Database Diagram

[Database Diagram](/documentation/erd.png)

## Technologies Used

### Languages Used

* [Python 3.12.2](https://www.python.org/downloads/release/python-3122/): the primary language used to develop the api.

### Database

* [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/)

### Frameworks Used

* [Django Project](https://www.djangoproject.com/) - A framework to build the app.
* [Django REST Framework](https://www.django-rest-framework.org/) - A toolkit for building Web APIs

### Packages Used

* [Asgiref](https://pypi.org/project/asgiref/) - Contains various ASGI-related helpers and utilities.
* [Cloudinary](https://cloudinary.com/) - To host images.
* [Cryptography](https://pypi.org/project/cryptography/) - Provides cryptographic recipes and primitives to Python developers.
* [Dj_database_url](https://pypi.org/project/dj-database-url/) - To parse the database URL from the environment variables in Heroku.
* [Dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - Provides a set of REST API endpoints for Django authentication.
* [Django](https://www.djangoproject.com/) - High-level Python web framework that encourages rapid development and clean, pragmatic design.
* [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) - For authentication, registration, account management.
* [Django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - A Django package that facilitates integration with Cloudinary.
* [Django-cors-headers](https://pypi.org/project/django-cors-headers/) - To allow in-browser requests to Django application from other origins.
* [Django-filter](https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html#adding-a-filterset-with-filterset-class) - To create range filters.
* [Djangorestframework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs.
* [Djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Provides a JSON Web Token authentication backend for the Django REST Framework.
* [Gunicorn](https://gunicorn.org/) - As the server for Heroku.
* [Oauthlib](https://pypi.org/project/oauthlib/) - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic.
* [Pillow](https://pypi.org/project/pillow/) - Image Processing.
* [Psycopg2](https://pypi.org/project/psycopg2/) - As an adaptor for Python and PostgreSQL databases.
* [PyJWT](https://pyjwt.readthedocs.io/en/stable/) - JSON Web Token implementation in Python.
* [Python3-openid](https://pypi.org/project/python3-openid/) - Python OpenID library.
* [Pytz](https://pypi.org/project/pytz/) - World Timezone Definitions for Python.
* [Requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuthlib support for Python Requests.
* [Setuptools](https://pypi.org/project/setuptools/) - Easily download, build, install, upgrade, and uninstall Python packages.
* [Sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser.
* [Urllib3](https://pypi.org/project/urllib3/) - HTTP library with thread-safe connection pooling, file post support, user friendly, and more.

### Tools Used

* [GitHub](https://github.com/): used to host the website's source code.
* [GitPod](https://gitpod.io/): the IDE used to develop the website.
* [CI Python Linter](https://pep8ci.herokuapp.com/): was used to validate Python code.
* [Lucidchart](https://www.lucidchart.com/): To create the ERD.

## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).
- If you don't already have an account to Cloudinary, create one [here](https://cloudinary.com/).
- For students of Code Institute, create a database [here](https://dbs.ci-dbs.net/)

1. Open the repository in GitPod

2. Install the dependencies:

    - Open the terminal window and type:
    - `pip3 install -r requirements.txt`

3. Create a `env.py` file. Add this code printed below. os.environ['DEV'] = '1' should be commented out to be able to migrate to an external database.

    ```python
    import os

    os.environ['CLOUDINARY_URL'] = 'Your cloudinary url'
    # os.environ['DEV'] = '1'
    os.environ['DATABASE_URL'] = "Your database url"
    os.environ.setdefault("SECRET_KEY", "Your secret key")
    ```


4. Run the following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
5. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter the required information (your username, email and password).

### To deploy the project to Heroku:

1.  Login to your account at [Heroku](https://dashboard.heroku.com)

2.	Click "New" to create a new app.

3.	Select a unique name, selected the region, and click Create app.

4.	Within the created app, select the tab, Settings.

5.	At the Config Vars section, click Reveal Config Vars.

6.	Add Config Vars:
- `ALLOWED_HOST` = .herokuapp.com
- `CLOUDINARY_URL` = Your cloudinary url
- `DATABASE_URL` = Your database url
- `DISABLE_COLLECTSTATIC` = 1
- `SECRET_KEY` = Your secret key

7.	Commit and push to GitHub

8.	Back to Heroku, go to the deployment tab.

9.	Select GitHub as the deployment method and connected to GitHub.

10.	Search for repository name and Connect.

11.	Click Deploy Branch. Click the View button when it is done.


## Testing

Please see [Testing](TESTING.md)

## Credits

- [Code Institute's](https://codeinstitute.net/) - Walkthrough project for Django REST Framework
- [Heroku](https://www.heroku.com/) for hosting the site.
- For tips and help: [Stackoverflow](https://stackoverflow.com)
- Github were used to store my repository: [GitHub](https://github.com)
- Django documentation for learning [Django](https://docs.djangoproject.com/en/5.0/)

### Acknowledgments

- My mentor for valuable feedback! [Iuliia Konovalova](https://github.com/IuliiaKonovalova)
- The tutors at Code Institute for debugging.