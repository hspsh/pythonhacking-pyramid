from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from pyramid_hs.models.mymodel import Todo
from pyramid_hs.validators import ValidationException, todo_validator


@view_config(route_name="index", renderer="../templates/to_do/list.jinja2")
def index(request):
    todo_list = [
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.desc,
            "date_added": todo.created_at,
        }
        for todo in Todo.select().order_by(Todo.created_at.desc())
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

@view_config(route_name="display_todo", renderer="../templates/to_do/display.jinja2")
def display_todo(request):
    pk = int(request.matchdict['pk'])
    try:
        todo = Todo.get(id=pk)
    except Todo.DoesNotExist:
        raise HTTPNotFound
    return {
        "site_header": "Todo {}".format(pk),
        "title": todo.title,
        "description": todo.desc,
        "date_added": todo.created_at,
    }
