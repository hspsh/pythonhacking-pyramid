from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from pyramid_hs.models.mymodel import Todo
from pyramid_hs.validators import ValidationException, todo_validator


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
    context = {
        "site_header": "Add new todo"
    }
    if request.method == 'POST':
        try:
            validated_data = todo_validator(request.POST)
        except ValidationException as ve:
            context.update(ve.errors)
            context.update(request.POST)
            return context
        title = validated_data.get("title")
        desc = validated_data.get("description")
        Todo.create(title=title, desc=desc)
        raise HTTPFound("/")
    return context
