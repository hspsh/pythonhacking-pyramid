from pyramid.view import view_config
from pyramid_hs.models.mymodel import Todo


@view_config(route_name="index", renderer="../templates/index.jinja2")
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
        "todo_list": todo_list
    }
