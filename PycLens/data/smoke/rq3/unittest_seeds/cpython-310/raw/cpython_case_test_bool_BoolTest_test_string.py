# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs('xyz'.endswith('z'), True)
    self.assertIs('xyz'.endswith('x'), False)
    self.assertIs('xyz0123'.isalnum(), True)
    self.assertIs('@#$%'.isalnum(), False)
    self.assertIs('xyz'.isalpha(), True)
    self.assertIs('@#$%'.isalpha(), False)
    self.assertIs('0123'.isdigit(), True)
    self.assertIs('xyz'.isdigit(), False)
    self.assertIs('xyz'.islower(), True)
    self.assertIs('XYZ'.islower(), False)
    self.assertIs('0123'.isdecimal(), True)
    self.assertIs('xyz'.isdecimal(), False)
    self.assertIs('0123'.isnumeric(), True)
    self.assertIs('xyz'.isnumeric(), False)
    self.assertIs(' '.isspace(), True)
    self.assertIs('\xa0'.isspace(), True)
    self.assertIs('\u3000'.isspace(), True)
    self.assertIs('XYZ'.isspace(), False)
    self.assertIs('X'.istitle(), True)
    self.assertIs('x'.istitle(), False)
    self.assertIs('XYZ'.isupper(), True)
    self.assertIs('xyz'.isupper(), False)
    self.assertIs('xyz'.startswith('x'), True)
    self.assertIs('xyz'.startswith('z'), False)
