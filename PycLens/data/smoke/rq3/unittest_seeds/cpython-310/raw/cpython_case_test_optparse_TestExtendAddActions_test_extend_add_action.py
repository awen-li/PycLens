# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestExtendAddActions_test_extend_add_action

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-afoo,bar', '--apple=blah'], {'apple': ['foo', 'bar', 'blah']}, [])
