# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFrozen_test_overwriting_frozen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __setattr__'):

        @dataclass(frozen=True)
        class C:
            x: int

            def __setattr__(self):
                pass
    with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __delattr__'):

        @dataclass(frozen=True)
        class C:
            x: int

            def __delattr__(self):
                pass

    @dataclass(frozen=False)
    class C:
        x: int

        def __setattr__(self, name, value):
            self.__dict__['x'] = value * 2
    self.assertEqual(C(10).x, 20)
