from django import template
from django.http import HttpResponse

register = template.Library()

@register.simple_tag(takes_context=True)
def text_upper_case(context: str, text: str):
    try:
        return str(text).upper() + " user"
    except Exception as error:
        print("error simple_tag text_upper_case: ", error)
        return HttpResponse(error)

@register.filter(name="format_string")
def format_string(source: str):
    if len(source) < 10:
        return source+"☃"
    else:
        return source