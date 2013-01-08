from markitup.fields import MarkupField
import widgets

class MarkupFilebrowserFiled(MarkupField):
    def formfield(self, **kwargs):
        defaults = {'widget': widgets.MarkitUpFilebrowserWiget}
        defaults.update(kwargs)
        return super(MarkupFilebrowserFiled, self).formfield(**defaults)


from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
FORMFIELD_FOR_DBFIELD_DEFAULTS[MarkupFilebrowserFiled] = {'widget': widgets.AdminMarkitUpFilebrowserWiget}