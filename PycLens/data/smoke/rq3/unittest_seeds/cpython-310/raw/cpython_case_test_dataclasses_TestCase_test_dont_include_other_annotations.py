# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_dont_include_other_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        i: int

        def foo(self) -> int:
            return 4

        @property
        def bar(self) -> int:
            return 5
    self.assertEqual(list(C.__annotations__), ['i'])
    self.assertEqual(C(10).foo(), 4)
    self.assertEqual(C(10).bar, 5)
    self.assertEqual(C(10).i, 10)
