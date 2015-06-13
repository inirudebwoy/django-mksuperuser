================
django-superuser
================
.. image:: https://travis-ci.org/inirudebwoy/django-superuser.svg?branch=develop
  :target: https://travis-ci.org/inirudebwoy/django-superuser
  
Django app for lazy people.
Creates superuser with no fuss.
  
login
  admin
password
  admin
  
Installation
============
Install from pip::

  pip install django-superuser

Add package to INSTALLED_APPS.::

  INSTALLED_APPS += ('django_superuser',)

When you create new Django project and syncdb or migrate (depending on version)
new admin user is created with login 'admin' and password 'admin'.
For all the lazy people!::

  Django 1.7 > python manage.py migrate
  Django 1.7 < python manage.py syncdb --noinput
