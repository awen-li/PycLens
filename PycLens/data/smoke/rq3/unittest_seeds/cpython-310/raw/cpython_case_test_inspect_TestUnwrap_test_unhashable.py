# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestUnwrap_test_unhashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        pass
    func.__wrapped__ = None

    class C:
        __hash__ = None
        __wrapped__ = func
    self.assertIsNone(inspect.unwrap(C()))
