# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_bad_single_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertInvalidSingle('1\n2')
    self.assertInvalidSingle('def f(): pass')
    self.assertInvalidSingle('a = 13\nb = 187')
    self.assertInvalidSingle('del x\ndel y')
    self.assertInvalidSingle('f()\ng()')
    self.assertInvalidSingle('f()\n# blah\nblah()')
    self.assertInvalidSingle('f()\nxy # blah\nblah()')
    self.assertInvalidSingle('x = 5 # comment\nx = 6\n')
    self.assertInvalidSingle("c = '''\nd=1\n'''\na = 1\n\nb = 2\n")
