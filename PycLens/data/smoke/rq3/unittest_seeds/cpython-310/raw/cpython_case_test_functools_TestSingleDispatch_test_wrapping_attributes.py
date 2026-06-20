# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_wrapping_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def g(obj):
        """Simple test"""
        return 'Test'
    self.assertEqual(g.__name__, 'g')
    if sys.flags.optimize < 2:
        self.assertEqual(g.__doc__, 'Simple test')
