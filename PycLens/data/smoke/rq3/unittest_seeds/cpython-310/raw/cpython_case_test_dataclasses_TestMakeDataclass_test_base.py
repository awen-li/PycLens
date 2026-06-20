# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_base

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Base1:
        pass

    class Base2:
        pass
    C = make_dataclass('C', [('x', int)], bases=(Base1, Base2))
    c = C(2)
    self.assertIsInstance(c, C)
    self.assertIsInstance(c, Base1)
    self.assertIsInstance(c, Base2)
