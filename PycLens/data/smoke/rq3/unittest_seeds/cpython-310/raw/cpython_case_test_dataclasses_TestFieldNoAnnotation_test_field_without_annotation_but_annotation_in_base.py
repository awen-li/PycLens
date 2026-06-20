# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFieldNoAnnotation_test_field_without_annotation_but_annotation_in_base

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class B:
        f: int
    with self.assertRaisesRegex(TypeError, "'f' is a field but has no type annotation"):

        @dataclass
        class C(B):
            f = field()
