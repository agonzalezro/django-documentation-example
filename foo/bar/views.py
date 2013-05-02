from django import http


def index(request):
    return http.HttpResponse('Hi {name}, how are you?'.format(name=name))


def get_capitalized_name(name='Alex'):
    """Capitalize the name and return it.

    >>> get_capitalized_name('Alex')
    'Alex'
    >>> get_capitalized_name('alex')
    'Alex'
    >>> get_capitalized_name('ALEX')
    'Alex'
    >>> get_capitalized_name('A')
    'A'
    >>> get_capitalized_name('')
    >>> get_capitalized_name(123)

    """
    if isinstance(name, basestring) and len(name):
        return name[0].upper() + name[1:].lower()
