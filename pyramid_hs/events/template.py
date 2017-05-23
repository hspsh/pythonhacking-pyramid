from pyramid.events import subscriber, BeforeRender


@subscriber(BeforeRender)
def update_context(event):
    event['project_name'] = "Test"