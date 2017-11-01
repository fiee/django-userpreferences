from __future__ import absolute_import, print_function, unicode_literals
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import django.views.static
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from . import app_settings


@login_required
def index(request):
    if not app_settings.INDEX_VIEW_ENABLED:
        return HttpResponse()

    if request.method == "POST":
        post = request.POST
        for key, value in post.items():
            toks = key.split(app_settings.SEPARATOR)
            if len(toks) != 2:
                continue
            app, pref = toks[0], toks[1]
            # User choice is always in first place [0].
            # Value of preference is always in second place [1]
            preferences = request.user.preferences.all()
            if preferences[app][pref][0][1] != value:
                user_preferences = request.user.preferences.preferences
                if app not in user_preferences:
                    user_preferences[app] = {}
                if pref not in user_preferences[app]:
                    user_preferences[app][pref] = {}
                user_preferences[app][pref] = value
                request.user.preferences.save()
    preferences = request.user.preferences.all()
    # TODO if django version is older
    static_url = reverse('preferences.views.media', args=[''])
    extra = {
            'preferences': preferences,
            'STATIC_URL': static_url,
            'SEPARATOR': app_settings.SEPARATOR
    }
    return render(request, 'preferences.html', extra)


def media(request, path):
    """
    Serve media file directly.
    Useful only for django pre 1.3 which does not use
    django.collectstatic
    """
    parent = os.path.abspath(os.path.dirname(__file__))
    root = os.path.join(parent, 'media')
    return django.views.static.serve(request, path, root)


@login_required
def change(request, app, pref, new_value):
    return_url = request.path
    if request.method == 'GET':
        if request.GET.get('return_url'):
            return_url = request.GET.get('return_url')
    preferences = request.user.preferences.preferences
    if app not in preferences:
        preferences[app] = {pref: new_value}
    request.user.preferences.preferences[app][pref] = new_value
    request.user.preferences.save()
    return HttpResponseRedirect(return_url)
