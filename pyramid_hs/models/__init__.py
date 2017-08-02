from .mymodel import MyModel, Person, Pet


def includeme(config):
    """
    Initialize the model for a Pyramid app.
    Activate this setup using ``config.include('pyramid_hs.models')``.
    """
    config.get_settings()
