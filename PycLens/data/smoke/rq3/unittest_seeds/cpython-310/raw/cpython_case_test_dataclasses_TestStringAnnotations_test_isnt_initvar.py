# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestStringAnnotations_test_isnt_initvar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for typestr in ('IV', 'dc.InitVar', 'xdataclasses.xInitVar', 'typing.xInitVar[int]'):
        with self.subTest(typestr=typestr):

            @dataclass
            class C:
                x: typestr
            self.assertEqual(C(10).x, 10)
