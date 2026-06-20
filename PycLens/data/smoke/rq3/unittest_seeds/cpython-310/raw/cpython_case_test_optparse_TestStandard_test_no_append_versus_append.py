# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestStandard_test_no_append_versus_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-b3', '-b', '5', '--foo=bar', '--foo', 'baz'], {'a': None, 'boo': 5, 'foo': ['bar', 'baz']}, [])
