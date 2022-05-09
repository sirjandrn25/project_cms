from django import template

register = template.Library()


@register.filter(name="active_filter")
def active_filter(request,filter_name):
    status = request.GET.get('status')
    if status is None:
        status = "all"
    if status == filter_name:
        return "active text-light bg-warning"
    return ''