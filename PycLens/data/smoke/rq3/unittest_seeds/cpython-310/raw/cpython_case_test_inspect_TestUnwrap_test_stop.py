# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestUnwrap_test_stop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func1(a, b):
        return a + b

    @functools.wraps(func1)
    def func2():
        pass

    @functools.wraps(func2)
    def wrapper():
        pass
    func2.stop_here = 1
    unwrapped = inspect.unwrap(wrapper, stop=lambda f: hasattr(f, 'stop_here'))
    self.assertIs(unwrapped, func2)
