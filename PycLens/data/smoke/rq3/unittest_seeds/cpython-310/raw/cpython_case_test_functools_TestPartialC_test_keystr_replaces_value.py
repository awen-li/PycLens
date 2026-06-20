# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialC_test_keystr_replaces_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.partial(capture)

    class MutatesYourDict(object):

        def __str__(self):
            p.keywords[self] = ['sth2']
            return 'astr'
    p.keywords[MutatesYourDict()] = ['sth']
    r = repr(p)
    self.assertIn('astr', r)
    self.assertIn("['sth']", r)
