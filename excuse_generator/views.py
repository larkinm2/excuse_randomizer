from pyramid.view import view_config


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'excuse_generator'}

@view_config(route_name='home', renderer='home.jinja2')
def my_view(request):
    return {}

@view_config(route_name='out', renderer='out.jinja2')
def out(request):
    return {}

@view_config(route_name='cancel', renderer='cancel.jinja2')
def cancel(request):
    return {}

@view_config(route_name='something', renderer='something.jinja2')
def something(request):
    return {}

@view_config(route_name='late', renderer='late.jinja2')
def late(request):
    return {}

@view_config(route_name='no', renderer='no.jinja2')
def no(request):
    return {}

@view_config(route_name='no', request_method='POST')
def form(request):
    return {}
