from django import forms
from .models import PREFERENCES


class BasePreferencesForm(forms.Form):
    def update_preferences(self, user):
        """
        Update `user' preferences from form's (clean) data.
        'update_<field>' methods are looked up and called if found
        to process values.
        """
        preferences = user.preferences.preferences
        if self.app not in preferences:
            user.preferences.preferences[self.app] = {}

        for key, value in self.cleaned_data.iteritems():
            if key in self.exclude_from_preferences:
                continue
            if hasattr(self, 'update_%s' % key):
                value = getattr(self, 'update_%s' % key)(value)
            user.preferences.preferences[self.app][key] = value

        # Go through preferences not in cleaned_data and try calling its update_<preference> method
        for key in [k for k in preferences.keys() if k not in self.cleaned_data.keys]:
            if hasattr(self, 'update_%s' % key):
                value = getattr(self, 'update_%s' % key)(value)
                user.preferences.preferences[self.app][key] = value

        user.preferences.save()


def preferences_form_factory(
        app, form=BasePreferencesForm,
        fields=None, exclude=None,
        formfield_callback=None, widgets=None):
    preferences = PREFERENCES[app]
    attrs = {}
    if fields is not None:
        attrs['fields'] = fields
    if exclude is not None:
        attrs['exclude'] = exclude
    if widgets is not None:
        attrs['widgets'] = widgets

    # If parent form class already has an inner Meta, the Meta we're
    # creating needs to inherit from the parent's inner meta.
    parent = (object,)
    if hasattr(form, 'Meta'):
        parent = (form.Meta, object)
    Meta = type(str('Meta'), parent, attrs)

    # Give this new form class a reasonable name.
    class_name = '%sPreferencesForm' % app.title()

    # Class attributes for the new form class.
    form_class_attrs = {
        'app': app,
        'Meta': Meta,
        'exclude_from_preferences': [],
        'formfield_callback': formfield_callback
    }
    # Add ChoiceFields for each preference in the app
    form_class_attrs.update(map(
        lambda item: (item[0], forms.ChoiceField(choices=(tuple(reversed(c)) for c in item[1]))),
        preferences.iteritems()))

    # Instatiate type(form) in order to use the same metaclass as form.
    return type(form)(class_name, (form,), form_class_attrs)
