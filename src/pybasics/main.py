#
#
import pickle


def read_file(f, split=False):
    """Read text file.

    :param f: Filename.
    :type f: str

    :return: File content.
    :rtype: Object
    """
    with open(f, 'r') as m:
        data = m.read().splitlines() if split else m.read()

    return data


def write_file(f, c, join=False):
    """Write text file.

    :param f: Filename.
    :type f: str

    :param c: Content to write.
    :type c: Object
    """
    if join:
        c = '\n'.join(c)

    with open(f, 'w') as m:
        data = m.write(c)

    return None


def read_pickle(f):
    """Read pickle binary file.

    :param f: Filename.
    :type f: str

    :return: File content.
    :rtype: Object
    """
    with open(f, 'rb') as msg:
        c = pickle.load(msg)

    return c


def write_pickle(f, c):
    """Write pickle binary file.

    :param f: Filename.
    :type f: str

    :param c: Content to write.
    :type c: Object
    """
    with open(f, 'wb') as msg:
        pickle.dump(c, msg)

    return None
