# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestUnwrap_test_recursion_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = NTimesUnwrappable(sys.getrecursionlimit() + 1)
    with self.assertRaisesRegex(ValueError, 'wrapper loop'):
        inspect.unwrap(obj)
