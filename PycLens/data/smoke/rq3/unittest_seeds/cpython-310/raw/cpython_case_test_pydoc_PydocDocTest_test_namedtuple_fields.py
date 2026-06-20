# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_namedtuple_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Person = namedtuple('Person', ['nickname', 'firstname'])
    with captured_stdout() as help_io:
        pydoc.help(Person)
    helptext = help_io.getvalue()
    self.assertIn('nickname', helptext)
    self.assertIn('firstname', helptext)
    self.assertIn('Alias for field number 0', helptext)
    self.assertIn('Alias for field number 1', helptext)
