# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_atomic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Classic:
        pass

    class NewStyle(object):
        pass

    def f():
        pass
    tests = [None, ..., NotImplemented, 42, 2 ** 100, 3.14, True, False, 1j, b'bytes', 'hello', 'helloሴ', f.__code__, NewStyle, range(10), Classic, max, property()]
    for x in tests:
        self.assertIs(copy.deepcopy(x), x)
