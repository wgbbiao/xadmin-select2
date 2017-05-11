#-*-coding:utf8;-*-
from xadmin.views import BaseAdminPlugin
from django import forms
from django.utils.html import format_html
from xadmin.util import vendor
from django.utils.encoding import (
    force_text
)
class SelectizeMultipleWidget(forms.SelectMultiple):
    def __init__(self, rel, admin_view, attrs=None, using=None):
        self.rel = rel
        self.admin_view = admin_view
        self.db = using
        super(SelectizeMultipleWidget, self).__init__(attrs)
    @property
    def media(self):
        media = vendor('select.js', 'select.css')
        media.add_js(['js/selectize-multiple.js'])
        return media
    
    def build_attrs(self, attrs={}, **kwargs):
        to_opts = self.rel.to._meta
        attrs['data-search-url'] = self.admin_view.get_admin_url(
            '%s_%s_changelist' % (to_opts.app_label, to_opts.model_name))
        if "class" not in attrs:
            attrs['class'] = 'selectize-multiple'
        else:
            attrs['class'] = attrs['class'] + ' selectize-multiple'
        attrs['data-choices'] = '?'
        return super(SelectizeMultipleWidget,self).build_attrs(attrs,**kwargs)

    def render_options(self, selected_choices):
        # Normalize to strings.
        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        self.choices.queryset = self.choices.queryset.filter(pk__in=selected_choices)
        for option_value, option_label in self.choices:
            if isinstance(option_label, (list, tuple)):
                output.append(format_html('<optgroup label="{}">', force_text(option_value)))
                for option in option_label:
                    output.append(self.render_option(selected_choices, *option))
                output.append('</optgroup>')
            else:
                output.append(self.render_option(selected_choices, option_value, option_label))
        return '\n'.join(output)


class SelectizeMultiplePlugin(BaseAdminPlugin):
    def get_field_style(self, attrs, db_field, style, **kwargs):
        if style == 'select2':
            db = kwargs.get('using')
            return {'widget': SelectizeMultipleWidget(db_field.remote_field, self.admin_view, using=db)}
        return attrs