def testable(message):
    """A function with testable documentation

    >>> testable('Hello you there')
    'This was your message: Hello you there'

    >>> for x in range(3):
    ...       print(x)
    0
    1
    2

    :param message: any string
    :return: the string that was given as a parameter
    """
    return("This was your message: " + message)