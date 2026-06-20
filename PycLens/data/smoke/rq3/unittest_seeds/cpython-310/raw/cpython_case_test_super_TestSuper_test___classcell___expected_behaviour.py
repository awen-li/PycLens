# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test___classcell___expected_behaviour

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __new__(cls, name, bases, namespace):
            nonlocal namespace_snapshot
            namespace_snapshot = namespace.copy()
            return super().__new__(cls, name, bases, namespace)
    namespace_snapshot = None

    class WithoutClassRef(metaclass=Meta):
        pass
    self.assertNotIn('__classcell__', namespace_snapshot)
    namespace_snapshot = None

    class WithClassRef(metaclass=Meta):

        def f(self):
            return __class__
    class_cell = namespace_snapshot['__classcell__']
    method_closure = WithClassRef.f.__closure__
    self.assertEqual(len(method_closure), 1)
    self.assertIs(class_cell, method_closure[0])
    with self.assertRaises(AttributeError):
        WithClassRef.__classcell__
