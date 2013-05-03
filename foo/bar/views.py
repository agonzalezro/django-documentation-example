from django import http


def index(request):
    # This view will not be shown on the sphinx HTML because have no
    # documentation
    return http.HttpResponse(
        'Hi {name}, how are you?'.format(name=get_capitalized_name('juan'))
    )


def this_is_just_for_show_a_reference():
    """This is a dumb function just to show how the references work.

    Since I am here, I will show you some tricks, `just use this link to see
    the source code <../../../bar/views.py>`_ and you will know how I made it.

    - Write ``strong`` with `**`: *bold text*.
    - Write ``em`` with `*`: *em text*.

        <b>You can even write some block of code</b>

    - Or just ``inline code``.

    1. Of course
    2. You can write
    3. enumeration too

    But c'mmon, those are just normal `reStructuredText elements
    <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.

    """


def get_capitalized_name(name='Alex', does_not_matter=None):
    """Capitalize the name and return it.

    I just want to make a reference to the other function documented in this
    module :py:func:`this_is_just_for_show_a_reference`.

    :param name: a string with the name that you want to capitalize.
    :param does_not_matter: just an example second argument.

    :type name: basestring
    :type does_not_matter: basestring or None

    :returns: a string with the name capitalized.

    :rtype: string or None

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
