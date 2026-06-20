# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: HexFloatTestCase_test_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class F(float):

        def __new__(cls, value):
            return float.__new__(cls, value + 1)
    f = F.fromhex(1.5.hex())
    self.assertIs(type(f), F)
    self.assertEqual(f, 2.5)

    class F2(float):

        def __init__(self, value):
            self.foo = 'bar'
    f = F2.fromhex(1.5.hex())
    self.assertIs(type(f), F2)
    self.assertEqual(f, 1.5)
    self.assertEqual(getattr(f, 'foo', 'none'), 'bar')
