# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestSubclass_test_bug_31608

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(deque):
        pass
    d = X()

    def bad___new__(cls, *args, **kwargs):
        return [42]
    X.__new__ = bad___new__
    with self.assertRaises(TypeError):
        d * 42
    with self.assertRaises(TypeError):
        d + deque([1, 2, 3])
