from markitup.fields import MarkupField
import widgets


class MarkupFilebrowserFiled(MarkupField):
    def formfield(self, **kwargs):
        defaults = {'widget': widgets.MarkitUpFilebrowserWiget}
        defaults.update(kwargs)
        return super(MarkupFilebrowserFiled, self).formfield(**defaults)


from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
FORMFIELD_FOR_DBFIELD_DEFAULTS[MarkupFilebrowserFiled] = {'widget': widgets.AdminMarkitUpFilebrowserWiget}


# allow South to handle MarkupField smoothly
try:
    from south.modelsinspector import add_introspection_rules
    # For a normal MarkupField, the add_rendered_field attribute is
    # always True, which means no_rendered_field arg will always be
    # True in a frozen MarkupField, which is what we want.
    add_introspection_rules(
        rules=[((MarkupFilebrowserFiled,),
                [],
                {'no_rendered_field': (
                    'add_rendered_field',
                    {},
                )}
                )],
        patterns=['markitup_filebrowser\.fields\.']
    )
except ImportError:
    pass
