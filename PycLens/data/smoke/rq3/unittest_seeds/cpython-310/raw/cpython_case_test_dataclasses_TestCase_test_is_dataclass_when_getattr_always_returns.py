# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_is_dataclass_when_getattr_always_returns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __getattr__(self, key):
            return 0
    self.assertFalse(is_dataclass(A))
    a = A()

    class B:
        pass
    b = B()
    b.__dataclass_fields__ = []
    for obj in (a, b):
        with self.subTest(obj=obj):
            self.assertFalse(is_dataclass(obj))
            with self.assertRaisesRegex(TypeError, 'should be called on dataclass instances'):
                asdict(obj)
            with self.assertRaisesRegex(TypeError, 'should be called on dataclass instances'):
                astuple(obj)
            with self.assertRaisesRegex(TypeError, 'should be called on dataclass instances'):
                replace(obj, x=0)
