# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_uninitialized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pair = self.tp.__new__(self.tp)
    del pair
    pair = self.tp.__new__(self.tp)
    self.assertRaisesRegex((ValueError, AttributeError), 'uninitialized|has no attribute', pair.read, 0)
    self.assertRaisesRegex((ValueError, AttributeError), 'uninitialized|has no attribute', pair.write, b'')
    pair.__init__(self.MockRawIO(), self.MockRawIO())
    self.assertEqual(pair.read(0), b'')
    self.assertEqual(pair.write(b''), 0)
