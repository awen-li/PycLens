# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestStringAnnotations_test_initvar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for typestr in ('InitVar[int]', 'InitVar [int] InitVar [int]', 'InitVar', ' InitVar ', 'dataclasses.InitVar[int]', 'dataclasses.InitVar[str]', ' dataclasses.InitVar[str]', 'dataclasses .InitVar[str]', 'dataclasses. InitVar[str]', 'dataclasses.InitVar [str]', 'dataclasses.InitVar [ str]', 'dataclasses.InitVar.[int]', 'dataclasses.InitVar+'):
        with self.subTest(typestr=typestr):

            @dataclass
            class C:
                x: typestr
            with self.assertRaisesRegex(AttributeError, "object has no attribute 'x'"):
                C(1).x
