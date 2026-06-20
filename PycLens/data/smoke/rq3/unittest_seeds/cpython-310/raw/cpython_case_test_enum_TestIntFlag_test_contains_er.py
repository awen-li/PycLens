# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_contains_er

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Open = self.Open
    Color = self.Color
    self.assertTrue(Color.GREEN in Color)
    self.assertTrue(Open.RW in Open)
    self.assertFalse(Color.GREEN in Open)
    self.assertFalse(Open.RW in Color)
    with self.assertRaises(TypeError):
        with self.assertWarns(DeprecationWarning):
            'GREEN' in Color
    with self.assertRaises(TypeError):
        with self.assertWarns(DeprecationWarning):
            'RW' in Open
    with self.assertRaises(TypeError):
        with self.assertWarns(DeprecationWarning):
            2 in Color
    with self.assertRaises(TypeError):
        with self.assertWarns(DeprecationWarning):
            2 in Open
