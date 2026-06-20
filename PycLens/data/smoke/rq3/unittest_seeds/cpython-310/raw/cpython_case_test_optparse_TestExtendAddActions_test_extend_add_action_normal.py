# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestExtendAddActions_test_extend_add_action_normal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-a', 'foo', '-abar', '--apple=x,y'], {'apple': ['foo', 'bar', 'x', 'y']}, [])
