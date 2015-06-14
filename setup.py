#  -*- coding: utf-8 -*-
import django_mksuperuser

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='django-mksuperuser',
    version=django_mksuperuser.__version__,
    description='Make super user with fixtures or migrations',
    long_description=open('README.rst').read(),
    author='Michal Klich',
    author_email='michal@michalklich.com',
    include_package_data=True,
    packages=['django_mksuperuser'],
    url='https://github.com/inirudebwoy/django-mksuperuser',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
