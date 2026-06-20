# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_contains_er

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Open = self.Open
    Color = self.Color
    self.assertFalse(Color.BLACK in Open)
    self.assertFalse(Open.RO in Color)
    with self.assertRaises(TypeError):
        with self.assertWarns(DeprecationWarning):
            'BLACK' in Color
    with self.assertRaises(TypeError):
        with self.assertWarns(DeprecationWarning):
            'RO' in Open
    with self.assertRaises(TypeError):
        with self.assertWarns(DeprecationWarning):
            1 in Color
    with self.assertRaises(TypeError):
        with self.assertWarns(DeprecationWarning):
            1 in Open
