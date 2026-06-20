# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestUnwrap_test_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func1():
        pass
    func1.__wrapped__ = func1
    with self.assertRaisesRegex(ValueError, 'wrapper loop'):
        inspect.unwrap(func1)

    def func2():
        pass
    func2.__wrapped__ = func1
    func1.__wrapped__ = func2
    with self.assertRaisesRegex(ValueError, 'wrapper loop'):
        inspect.unwrap(func1)
    with self.assertRaisesRegex(ValueError, 'wrapper loop'):
        inspect.unwrap(func2)
