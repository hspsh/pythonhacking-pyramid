from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from pyramid_hs.models.mymodel import Todo


@view_config(route_name="index", renderer="../templates/to_do/list.jinja2")
def index(request):
    todo_list = [
        {
            "title": todo.title,
            "description": todo.desc,
            "date_added": todo.created_at,
        }
        for todo in Todo.select()
    ]
    return {
        "site_header": "Todo list",
        "todo_list": todo_list
    }


@view_config(route_name="add_todo", renderer="../templates/to_do/add.jinja2")
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        desc = request.POST.get("description")
        Todo.create(title=title, desc=desc)
        raise HTTPFound("/")
    return {
        "site_header": "Add new todo"
    }
