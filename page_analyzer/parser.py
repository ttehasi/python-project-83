from bs4 import BeautifulSoup


def parser_body(body):
    pars_body = BeautifulSoup(body, 'html.parser')
    title = pars_body.title.string
    h1 = pars_body.h1.string if pars_body.h1 is not None else None
    description = ''
    if pars_body.meta is not None:
        metas = pars_body.find_all('meta')
        for i in metas:
            if i.get('name') == 'description':
                description = i['content']
    pars_data = {'title': title, 'h1': h1, 'description': description}
    return pars_data
