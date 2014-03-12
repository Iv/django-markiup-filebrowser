from django import template
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
import markdown
from markitup.fields import render_func


register = template.Library()


@register.filter(name="markdown")
def markdown_filter(value):
    """Processes the given value as Markdown, optionally using a particular
    Markdown style/config

    Syntax::

        {{ value|markdown }}            {# uses the "default" style #}
        {{ value|markdown:"mystyle" }}

    Markdown "styles" are defined by the `MARKDOWN_DEUX_STYLES` setting.
    """
    return mark_safe(render_func(value))
markdown_filter.is_safe = True


@register.tag(name="markdown")
def markdown_tag(parser, token):
    nodelist = parser.parse(('endmarkdown',))
    # bits = token.split_contents()
    # if len(bits) == 1:
    #     style = "default"
    # elif len(bits) == 2:
    #     style = bits[1]
    # else:
    #     raise template.TemplateSyntaxError("`markdown` tag requires exactly "
    #         "zero or one arguments")
    parser.delete_first_token() # consume '{% endmarkdown %}'
    return MarkdownNode(nodelist)

class MarkdownNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        value = self.nodelist.render(context)
        return mark_safe(render_func(value))
