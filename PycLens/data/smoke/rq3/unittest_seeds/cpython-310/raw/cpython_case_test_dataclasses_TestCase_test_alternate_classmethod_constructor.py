# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_alternate_classmethod_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int

        @classmethod
        def from_file(cls, filename):
            value_in_file = 20
            return cls(value_in_file)
    self.assertEqual(C.from_file('filename').x, 20)
