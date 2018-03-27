DreamListDashboard
==================

**For people with a lot of dreams, it is important to track their dreams' transitioning into reality.**

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT

Feature List
------------
 * Break down your dreams into a hierarchical structure of traceable tasks (version 1.0)
 * Out of all dreams select the one you should work on right now, based on availability of time. (version 2.0)
 * Get awarded on making a dream into reality (version 3.0)
 * Show dream analytics page (version 4.0)

Project Structure
-----------------
 * There is one frontend and two backends.
 * Frontend uses React-framework.
 * The two backends (one in django and other in spring-boot) provide similar rest-apis on different ports.
 * You can set port in frontend to choose anyone backend.

Setting Project Locally ( one time setup)
-----------------------------------------
* Create a python3 virtual environment

.. code-block::

 mkvirtualenv --python=python3 <virtual env name>

* Clone the git repo

.. code-block::

 git clone https://github.com/narutoadi/DreamListDashboard.git

* Open the project in virtual environment and install the requirements

.. code-block::

 workon <virtual env name>
 cd DreamListDashboard/backendDjango/dreamlist
 pip install -r requirements/local.txt

* Database setup

.. code-block::

 install postgres sql
 create db 'dreamlist'
 set database url in environment variable
 Windows - set DATABASE_URL=postgres://username:password@127.0.0.1:5432/dreamlist
 Linus/osx - export DATABASE_URL=postgres://username:password@127.0.0.1:5432/dreamlist


Running Project Locally
-----------------------
*. Running Django Backend Locally

* Enter the virtualenv

.. code-block::

  workon <virtual env name>

* Enter the manage.py

.. code-block::

  cd DreamListDashboard/backendDjango

* Migrate the database

.. code-block::

    python manage.py migrate

* Create superuser

.. code-block::

    python manage.py createsuperuser

* Run server

.. code-block::

 python manage.py runserver


Find the latest documentation at
--------------------------------
`<http://dreamlistdashboard.readthedocs.io/en/latest/>`_
