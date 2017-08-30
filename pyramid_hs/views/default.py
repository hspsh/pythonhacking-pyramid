import datetime
from peewee import PeeweeException
from pyramid.response import Response
from pyramid.view import view_config

from pyramid_hs.models import Person


# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         one = Person.select().where(Person.name == 'Bob').get()
#     except PeeweeException:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'pyramid_hs'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pyramid_hs_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "peewee.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


@view_config(route_name="hello_html", renderer='../templates/hello.jinja2')
def hello_h(request):
    request.response.status = 200
    return {'message': 'Hello World!'}


@view_config(route_name="hello_json", renderer='json')
def hello(request):
    request.response.status = 200
    return {'message': 'hello world'}


@view_config(route_name="simple_form", renderer="../templates/simple_form.jinja2")
def simple_form(request):
    request.response.status = 200
    return {}


@view_config(route_name="form_resp", renderer="../templates/form_response.jinja2")
def form_resp(request):
    request.response.status = 200
    return {'message': request.params['message']}


@view_config(route_name="example_view", renderer="../templates/example_template.jinja2")
def example_view(request):
    example_dict = {
        'key_a': 'value_a',
        'key_b': 'value_b'
    }
    example_list = [1, 2, 3, "<b>some paragraph</b>", "<b>some bold paragraph</b>"]
    request.response.status = 200
    return {
        'some_dict': example_dict,
        'some_list': example_list
    }


@view_config(route_name="index", renderer="../templates/index.jinja2")
def index(request):
    todo_list = [
        {
            "title": "My first task",
            "description": "blablalblala",
            "date_added": datetime.datetime.now() + datetime.timedelta(days=-1),
            "due_date": datetime.datetime.now() + datetime.timedelta(days=7)
        },
        {
            "title": "My second task",
            "description": "another blablalblala",
            "date_added": datetime.datetime.now(),
            "due_date": datetime.datetime.now() + datetime.timedelta(days=7)
        }
    ]
    return {
        "todo_list": todo_list
    }
