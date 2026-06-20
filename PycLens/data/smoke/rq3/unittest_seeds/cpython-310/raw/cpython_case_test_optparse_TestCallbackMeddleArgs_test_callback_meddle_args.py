# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestCallbackMeddleArgs_test_callback_meddle_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-1', 'foo', '-3', 'bar', 'baz', 'qux'], {'things': [('foo',), ('bar', 'baz', 'qux')]}, [1, 3])
