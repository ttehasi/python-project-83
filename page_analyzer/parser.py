from bs4 import BeautifulSoup


def parser_body(body):
    pars_body = BeautifulSoup(body, 'html.parser')
    title = pars_body.title.string
    h1 = pars_body.h1.string if pars_body.h1 is not None else None
    description = pars_body.find('meta', {'name': 'description'}). \
        get('content') \
        if pars_body.find('meta', {'name': 'description'}) is not None else ''
    pars_data = {'title': title, 'h1': h1, 'description': description}
    return pars_data
