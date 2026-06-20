# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestDescriptors_test_set_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class D:

        def __set_name__(self, owner, name):
            self.name = name + 'x'

        def __get__(self, instance, owner):
            if instance is not None:
                return 1
            return self

    @dataclass
    class C:
        c: int = D()
    self.assertEqual(C.c.name, 'cx')

    @dataclass
    class C:
        c: int = field(default=D(), init=False)
    self.assertEqual(C.c.name, 'cx')
    self.assertEqual(C().c, 1)
