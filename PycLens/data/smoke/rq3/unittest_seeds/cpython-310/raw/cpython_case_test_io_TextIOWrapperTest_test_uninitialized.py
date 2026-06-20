# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_uninitialized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.TextIOWrapper.__new__(self.TextIOWrapper)
    del t
    t = self.TextIOWrapper.__new__(self.TextIOWrapper)
    self.assertRaises(Exception, repr, t)
    self.assertRaisesRegex((ValueError, AttributeError), 'uninitialized|has no attribute', t.read, 0)
    t.__init__(self.MockRawIO(), encoding='utf-8')
    self.assertEqual(t.read(0), '')
