==============
django-superuser
==============

Code can be found here.
https://bitbucket.org/inirudebwoy/django-superuser

Installation
============
Install from cheeseshop.imagination.net::

  easy_install -ZU -i https://cheeseshop:*****@cheeseshop.imagination.net/ django-superuser

Put package in INSTALLED_APPS.::

  INSTALLED_APPS += ('django-superuser',)

When you create new Django project and syncdb or migrate (depending on version)
new admin user is created with login 'admin' and same password.
For all the lazy people!::

  Django 1.7 > python manage.py migrate
  Django 1.7 < python manage.py syncdb --noinput
