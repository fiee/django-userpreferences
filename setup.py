#!/usr/bin/env python3
from setuptools import setup, find_packages


METADATA = dict(
    name='django-userpreferences',
    version='0.2.0',
    author='Nicolas Patry et al.',
    author_email='nicolas.patry@centraliens.net',

    description="""Django application that allows you to easily store
    preferences for your users to choose from. Sending emails but want to let
    the user choose the frequency? Do it by adding a preferences.py file in
    your email app.""",
    long_description=open('README.rst').read(),

    url='http://github.com/fiee/django-userpreferences',
    download_url='http://github.com/fiee/django-userpreferences/downloads/',

    include_package_data=True,

    keywords='django preferences user settings profile',

    install_requires=['django>=2.2', 'django_picklefield>=0.1.9', ],
    packages=find_packages(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public \
License (LGPL)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python3',
        'Framework :: Django',
    ],
)

if __name__ == '__main__':
    setup(requires=['django'], **METADATA)
