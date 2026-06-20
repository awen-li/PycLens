# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_description

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    desc = self.server.description('comp.lang.python')
    self.assertEqual(desc, 'The Python computer language.')
    desc = self.server.description('comp.lang.pythonx')
    self.assertEqual(desc, '')
