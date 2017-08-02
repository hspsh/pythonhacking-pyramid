from playhouse.shortcuts import model_to_dict
from pyramid.view import view_config

from pyramid_hs.models import MyModel


@view_config(route_name="save_model", renderer="json")
def save_model(request):
    my_model = MyModel(name=request.json['name'], value=request.json['value'])
    my_model.save()
    request.response.status = 200
    return {
        'id': my_model.id
    }


@view_config(route_name="get_model", renderer="json")
def get_model(request):
    my_model = MyModel.get(id=request.params['id'])
    request.response.status = 200
    return model_to_dict(my_model)
