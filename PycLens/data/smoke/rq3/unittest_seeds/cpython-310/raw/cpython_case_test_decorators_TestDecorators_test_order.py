# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def callnum(num):
        """Decorator factory that returns a decorator that replaces the
            passed-in function with one that returns the value of 'num'"""

        def deco(func):
            return lambda : num
        return deco

    @callnum(2)
    @callnum(1)
    def foo():
        return 42
    self.assertEqual(foo(), 2, 'Application order of decorators is incorrect')
