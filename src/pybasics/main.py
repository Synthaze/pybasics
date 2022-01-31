#
#
from pygments import highlight, lexers, formatters
import pickle
import glob
import json
import os


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


def write_file(f, c, mode='w', join=False):
    """Write text file.

    :param f: Filename.
    :type f: str

    :param c: Content to write.
    :type c: Object
    """
    if join:
        c = '\n'.join(c)

    with open(f, mode) as m:
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


def write_json(f, c):

    with open(f, 'w') as msg:
        json.dump(c, msg)

    return None


def read_json(f):

    with open(f) as msg:
        data = json.load(msg)

    return data


def list_dir(p):
    """.

    :param p: .
    :type p: str

    :return: .
    :rtype: list
    """
    p = os.path.join(p, '*')

    dirs = glob.glob(p)

    dirs = sorted([x for x in dirs if os.path.isdir(x)])

    return dirs


def last_file(p):
    """.

    :param p: .
    :type p: str

    :return: .
    :rtype: str
    """
    files = glob.glob(p)

    file = max(files, key=os.path.getctime)

    return file


def pretty_json(data):
    """.
    """
    print (highlight(json.dumps(data,sort_keys=True,indent=4), lexers.JsonLexer(), formatters.TerminalFormatter()))

    return data
