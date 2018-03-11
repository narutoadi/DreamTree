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

Setting Project Locally ( one time setup)
-----------------------------------------
* Create a python3 virtual environment

.. code-block::

 mkvirtualenv dldEnv

* Clone the git repo

.. code-block::

 git clone https://github.com/narutoadi/DreamListDashboard.git

* Open the project in virtual environment and install the requirements

.. code-block::

 workon dldEnv
 cd DreamListDashboard/dreamListDashboard
 pip install -r requirements/base.txt
 pip install -r requirements/local.txt

* Database setup

.. code-block::

  TBD postgres setup and python migration


Running Project Locally
-----------------------
* Enter the virtualenv

.. code-block::

  workon dldEnv

* Enter the manage.py

.. code-block::

  cd DreamListDashboard/dreamListDashboard

* Run server

.. code-block::

 python manage.py runserver


Find the latest documentation at
--------------------------------
`<http://dreamlistdashboard.readthedocs.io/en/latest/>`_
