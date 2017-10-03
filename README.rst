wagtail-pythonanywhere-quickstart
=================================

.. image:: https://img.shields.io/badge/version-v1.0.0-blue.svg

.. image:: https://img.shields.io/badge/license-ISC%20License%20(ISCL)-blue.svg
    :target: http://en.wikipedia.org/wiki/ISC_license

`Wagtail CMS`_ quickstart for deployment on `PythonAnywhere`_

.. _Wagtail CMS: https://wagtail.io
.. _PythonAnywhere: https://www.pythonanywhere.com

Prerequisites
-------------

* You have an account at `PythonAnywhere`_

.. _PythonAnywhere: https://www.pythonanywhere.com

Recommendations
---------------

* You use `virtualenv`_ for isolated local python development
* You are familiar with the `Django`_ basics, at least visited their great `online tutorial`_

.. _virtualenv: https://virtualenv.pypa.io
.. _Django: https://www.djangoproject.com
.. _online tutorial: https://docs.djangoproject.com/en/dev/intro/tutorial01

Technical requirements
----------------------

Below is the list of currently supported combinations of Wagtail, Django and Python:

+---+---------+-----------+--------------------+
| # | Wagtail | Django    | Python             |
+===+=========+===========+====================+
| 1 | 1.12    | 1.8, 1.10 | 2.7, 3.4, 3.5      |
+---+---------+-----------+--------------------+
| 2 | 1.12    | 1.11      | 2.7, 3.4, 3.5, 3.6 |
+---+---------+-----------+--------------------+

Set up the python application
-----------------------------

* Open a bash console on PythonAnywhere
* Create a virtualenv

  ``mkvirtualenv wagtail-pythonanywhere-quickstart-py36 --python=/usr/bin/python3.6``

* Clone the repository

  ``git clone https://github.com/texperience/wagtail-pythonanywhere-quickstart.git``

* Change into the project directory

  ``cd wagtail-pythonanywhere-quickstart``

* Install the python packages

  ``pip install -r requirements.txt``

* Prepare a local configuration file

  * Create a new file called ``local.py`` under ``wagtail-pythonanywhere-quickstart/settings``
  * Define at least the ``SECRET_KEY`` and ``ALLOWED_HOSTS`` settings
  * Typically you may want to define ``DATABASES`` and point ``MEDIA_ROOT`` as well as ``STATIC_ROOT`` to a persistent directory

* Initialize the database

  ``python manage.py migrate``

* Create a superuser account

  ``python manage.py createsuperuser``

* Collect static files

  ``python manage.py collectstatic``

Set up the web server
---------------------

* Open the PythonAnywhere "Web" tab
* Select ``Add a new web app``
* Choose ``Manual configuration (including virtualenvs)``
* Choose ``Python 3.6``

After your web app is created:

* Set the source code location to your projects home
* Change the WSGI configuration file
* Set the virtualenv path to the environment created above
* Set static and media urls and location
* Restart your application

Code and contribution
---------------------

The code is open source and released under the `ISC License (ISCL)`_. It is available on `GitHub`_ and follows the guidelines about `Semantic Versioning`_ for transparency within the release cycle and backward compatibility whenever possible.

All contributions are welcome, whether bug reports, code contributions and reviews, documentation or feature requests.

.. _ISC License (ISCL): http://en.wikipedia.org/wiki/ISC_license
.. _Semantic Versioning: http://semver.org/
.. _GitHub: https://github.com/texperience/texsite
