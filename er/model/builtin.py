import collections
import datetime
import functools
import itertools

from er.util import version


# Roles.
ROLE_ROOT = 0
ROLE_ADMIN = 100
ROLE_USER = 1000


UID_GUEST = 1
UNAME_GUEST = 'Guest'
USER_GUEST = {
    '_id': UID_GUEST
}

# Footer extra HTMLs.
FOOTER_EXTRA_HTMLS = ['© 2005 - 2019 <a href="https://???.org/">???.org</a>', version.get()]
