# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(copy.deepcopy(global_foo), global_foo)

    def foo(x, y):
        return x + y
    self.assertEqual(copy.deepcopy(foo), foo)
    bar = lambda : None
    self.assertEqual(copy.deepcopy(bar), bar)
