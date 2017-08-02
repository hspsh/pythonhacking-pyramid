from pyramid.events import subscriber, BeforeRender


@subscriber(BeforeRender)
def update_context(event):
    """
    Event handler to show that we can add something to payload outside of view controller
    """
    event['project_name'] = "Test"
