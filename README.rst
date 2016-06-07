===============================================
django-userpreferences (django-userpreferences)
===============================================

Save arbitrary settings per user.

This pluggable Django_ app should integrate easily with other apps, also in existing projects.


Installation 
============

Dependencies  
~~~~~~~~~~~~

* Django_ (of course)
* django-picklefield_


Installing django-userpreferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install into your python path using pip or easy_install::

    pip install django-userpreferences
    easy_install django-userpreferences

(Beware, this fork is only installable from github!)

Add *'preferences'* to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'preferences',
    )

Add *'(r'^preferences/', include('preferences.urls')'* to your urls:: 

    urlpatterns = patterns( '',
        ....
        (r'^preferences/', include('preferences.urls'),
    )

Don't forget to run ::

    ./manage.py makemigrations preferences
    ./manage.py migrate

to create the preferences table.


Using django-userpreferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a *preferences.py* file to your app *test_app*::

    test_app/
     -- preferences.py
     -- models.py
     -- views.py

That looks like this::

    PREFERENCES = (
        'mailing_period':(
            # (u'Preference Display', 'value')
            (u'Weekly', 'week'),  # first item is the default value
            (u'Monthly', 'month'),
            (u'Daily', 'day'),
        )
    )

You can now access user preferences within your views::

    >>> user.preferences['test_app']
    {'mailing_period' : 'week'}

    >>> user.preferences['test_app'] = { 'mailing_period' : 'month' }
    >>> user.preferences.save()
    >>> user.preferences['test_app']
    {'mailing_period' : 'month'}

Note: Though it may have some properties of a dict, ``user.preferences`` is **not** a dict.
It's a Model object; dict behaviour is a shortcut for ``user.preferences.preferences``.

If you use the preferences urls, there’s an url to change preferences::

    <a href="{% url preferences.views.change 'test_app' 'mailing_period' 'month' %}?return_url='/'>Receive monthly newsletter</a>
        
If the value in the database does not match any of the preferences in your 
``preferences.py``, the default value will be returned (this allows to disable 
preferences after people actually used them, without breaking your app).

Since we use pickle_ serialization, you can use only pickle-able settings.
These include strings, integers, floats, booleans, tuples, lists, sets.

Only discrete sets of settings are allowed for now.
Patches are welcome for preferences that accept user input.

Changing the default separator 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
django-userpreferences uses a separator between app name and
preference name in forms. By default the separator is '/'. To override this,
in the weird case you might be needing it in some variable name, you need
to change it in your settings.py file::

    PREFERENCES_SEPARATOR = '/'

Authors and License
===================

Authors
~~~~~~~

* Nicolas Patry, <nicolas.patry@centraliens.net> (main author)
* Henning Hraban Ramm, <hraban@fiee.net> (i18n, fixes)
* Gonzalo Delgado, <mail@gonzalodelgado.com.ar> (form)
* Andrei Kuziakov (adaption to Django 1.7, tests,  migration)

License
~~~~~~~

GNU Lesser/Library Public License (LGPL)

django-picklefield_ is MIT-licensed. Django_ itself is BSD-licensed. Discuss.


.. _Django: https://www.djangoproject.com/
.. _django-picklefield: https://github.com/shrubberysoft/django-picklefield
.. _pickle: http://docs.python.org/library/pickle.html
