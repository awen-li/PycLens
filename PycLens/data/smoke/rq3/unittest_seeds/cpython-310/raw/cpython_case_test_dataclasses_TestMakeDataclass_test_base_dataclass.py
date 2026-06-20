# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_base_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class Base1:
        x: int

    class Base2:
        pass
    C = make_dataclass('C', [('y', int)], bases=(Base1, Base2))
    with self.assertRaisesRegex(TypeError, 'required positional'):
        c = C(2)
    c = C(1, 2)
    self.assertIsInstance(c, C)
    self.assertIsInstance(c, Base1)
    self.assertIsInstance(c, Base2)
    self.assertEqual((c.x, c.y), (1, 2))
