import datetime
from pyramid.view import view_config


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
