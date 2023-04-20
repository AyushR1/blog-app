Blogging Platform - README
==========================

This project is a Blogging Platform API built using Django REST Framework and PostgreSQL.

Installation
------------

Clone this repository and run the following command to build the Docker container:

bashCopy code

`sudo docker-compose up -d --build`

This will create a container running the application at `http://127.0.0.1:8000/`.

API Endpoints
-------------

-   `/api/register/` - Register a new user
-   `/api/login/` - Login a user
-   `/api/logout/` - Logout a user
-   `/api/posts/` - List all blog posts
-   `/api/posts/<id>/` - Retrieve, update, or delete a specific blog post

Usage
-----

After running the Docker container, you can interact with the API endpoints using your preferred HTTP client, such as `curl` or `Postman`.

### User Authentication

To create a new user, make a `POST` request to `/api/register/` with the following fields in the request body:

-   `username`
-   `password`

To login a user, make a `POST` request to `/api/login/` with the following fields in the request body:

-   `username`
-   `password`

You will get refresh and access tokens as response

### Blog Posts

To list all blog posts, make a `GET` request to `/api/posts/`.

To create a new blog post, make a authenticated `POST` request to `/api/posts/` with the following fields in the request body:

-   `title`
-   `description`
-   `image`

and with Authorization Header having the access tokens

To retrieve, update, or delete a specific blog post, make a `GET`, `PUT`, or `DELETE` request to `/api/posts/<id>/`, where `<id>` is the ID of the blog post along with Authorization Header having the access tokens

### Pagination

To implement pagination for the blog posts endpoint, add the `?page=<page_number>` query parameter to the `/api/posts/` endpoint.

Tests
-----

To run the tests for the API endpoints, run the following command:

`sudo docker-compose run app sh -c "python manage.py test && flake8"`

This will run the unit tests and check the code for PEP 8 compliance.

Bonus Features
--------------

-   To allow users to upload images to their blog posts we can upload images on post blog.
-   To implement password reset functionality for registered users, use the `django-all-auth` library.

Deployment
----------
The project is deployed on repl
you can have a look here

https://blog-app.ayushr1.repl.co/


Credits
-------

This project was created by Ayush