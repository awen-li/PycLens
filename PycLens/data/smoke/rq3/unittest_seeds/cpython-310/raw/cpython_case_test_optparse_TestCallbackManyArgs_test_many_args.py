# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestCallbackManyArgs_test_many_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-a', 'foo', 'bar', '--apple', 'ding', 'dong', '-b', '1', '2', '3', '--bob', '-666', '42', '0'], {'apple': None, 'bob': None}, [])
