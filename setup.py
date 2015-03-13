#  -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='superuser',
    version='0.1',
    description='Create super user with fixtures or migrations',
    author='Michal Klich',
    author_email='michal.klich@imagination.com',
    include_package_data=True,
    packages=['superuser'],
    url='https://bitbucket.org/inirudebwoy/superuser',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
