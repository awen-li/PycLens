# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestStringAnnotations_test_classvar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for typestr in ('ClassVar[int]', 'ClassVar [int]', ' ClassVar [int]', 'ClassVar', ' ClassVar ', 'typing.ClassVar[int]', 'typing.ClassVar[str]', ' typing.ClassVar[str]', 'typing .ClassVar[str]', 'typing. ClassVar[str]', 'typing.ClassVar [str]', 'typing.ClassVar [ str]', 'typing.ClassVar.[int]', 'typing.ClassVar+'):
        with self.subTest(typestr=typestr):

            @dataclass
            class C:
                x: typestr
            C()
            self.assertNotIn('x', C.__dict__)
