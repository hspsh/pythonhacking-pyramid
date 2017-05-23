def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('hello_json', '/hello_j/', request_method='GET')
    config.add_route('hello_html', '/hello_h/', request_method='GET')
    config.add_route('simple_form', '/form/', request_method='GET')
    config.add_route('form_resp', '/form/', request_method='POST')
    config.add_route('example_view', '/example_view/', request_method='GET')
