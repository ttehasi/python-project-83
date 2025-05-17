from urllib.parse import urlparse

import validators


def norm_url(url) -> str:
    pars_url = urlparse(url)
    result = pars_url.scheme + '://' + pars_url.hostname
    return result


def validate_url(url):
    errors = {}
    if not validators.url(url):
        errors['url'] = 'Некорректный формат URL'
        # return errors
    if len(url) > 255:
        errors['url'] = 'Слишком длинный URL (должен быть короче 255 символов)'
    return errors