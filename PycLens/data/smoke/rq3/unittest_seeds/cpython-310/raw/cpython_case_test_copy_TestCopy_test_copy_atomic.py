# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_atomic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Classic:
        pass

    class NewStyle(object):
        pass

    def f():
        pass

    class WithMetaclass(metaclass=abc.ABCMeta):
        pass
    tests = [None, ..., NotImplemented, 42, 2 ** 100, 3.14, True, False, 1j, 'hello', 'helloሴ', f.__code__, b'world', bytes(range(256)), range(10), slice(1, 10, 2), NewStyle, Classic, max, WithMetaclass, property()]
    for x in tests:
        self.assertIs(copy.copy(x), x)
