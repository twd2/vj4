import unittest

from er.util import validator


class Test(unittest.TestCase):
  def test_mail(self):
    self.assertTrue(validator.is_mail('ex@example.com'))
    self.assertTrue(validator.is_mail('1+e-x@example.com'))
    self.assertTrue(validator.is_mail('example.net@example.com'))
    self.assertFalse(validator.is_mail('example:net@example.com'))
    self.assertFalse(validator.is_mail('ex@examplecom'))
    self.assertFalse(validator.is_mail('example.com'))
    self.assertFalse(validator.is_mail('examplecom'))
    self.assertFalse(validator.is_mail('1+e=x@example.com'))

  def test_content(self):
    self.assertTrue(validator.is_content('dummy_name'))
    self.assertTrue(validator.is_content('x' * 300))
    self.assertFalse(validator.is_content(''))
    self.assertTrue(validator.is_content('c'))
    self.assertFalse(validator.is_content('x' * 700000))

  def test_intro(self):
    self.assertTrue(validator.is_intro('d'))
    self.assertTrue(validator.is_intro('dummy_name'))
    self.assertTrue(validator.is_intro('x' * 300))
    self.assertFalse(validator.is_intro(''))
    self.assertFalse(validator.is_intro('g' * 501))
    self.assertFalse(validator.is_intro('x' * 700000))


if __name__ == '__main__':
  unittest.main()
