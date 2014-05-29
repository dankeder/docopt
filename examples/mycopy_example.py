""" Usage: mycopy <src>... <dest>
"""
from docopt import docopt


if __name__ == '__main__':
    options = docopt(__doc__)
    print options
