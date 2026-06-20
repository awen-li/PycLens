# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestDescriptors_test_no_default_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class D:

        def __get__(self, instance: Any, owner: object) -> int:
            if instance is None:
                raise AttributeError()
            return instance._x

        def __set__(self, instance: Any, value: int) -> None:
            instance._x = value

    @dataclass
    class C:
        i: D = D()
    with self.assertRaisesRegex(TypeError, 'missing 1 required positional argument'):
        c = C()
