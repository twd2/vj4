import re

from er import error


MAIL_RE = re.compile(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*')


def is_mail(s):
  return bool(MAIL_RE.fullmatch(s))


def check_mail(s):
  if not is_mail(s):
    raise error.ValidationError('mail')


def is_title(s):
  return 0 < len(s.strip()) <= 64


def check_title(s):
  if not is_title(s):
    raise error.ValidationError('title')


def is_content(s):
  return isinstance(s, str) and 0 < len(s.strip()) < 65536


def check_content(s):
  if not is_content(s):
    raise error.ValidationError('content')


def is_intro(s):
  return isinstance(s, str) and 0 < len(s.strip()) < 500


def check_intro(s):
  if not is_intro(s):
    raise error.ValidationError('intro')


def is_lang(i):
  return i == 'zh_CN' # TODO(twd2)


def check_lang(i):
  if not is_lang(i):
    raise error.ValidationError('lang')
