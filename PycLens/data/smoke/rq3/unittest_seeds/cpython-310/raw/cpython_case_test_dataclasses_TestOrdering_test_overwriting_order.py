# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestOrdering_test_overwriting_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __lt__.*using functools.total_ordering'):

        @dataclass(order=True)
        class C:
            x: int

            def __lt__(self):
                pass
    with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __le__.*using functools.total_ordering'):

        @dataclass(order=True)
        class C:
            x: int

            def __le__(self):
                pass
    with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __gt__.*using functools.total_ordering'):

        @dataclass(order=True)
        class C:
            x: int

            def __gt__(self):
                pass
    with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __ge__.*using functools.total_ordering'):

        @dataclass(order=True)
        class C:
            x: int

            def __ge__(self):
                pass
