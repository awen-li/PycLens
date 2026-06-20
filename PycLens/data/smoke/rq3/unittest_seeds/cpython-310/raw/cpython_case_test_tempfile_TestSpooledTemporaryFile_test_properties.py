# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_properties

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = tempfile.SpooledTemporaryFile(max_size=10)
    f.write(b'x' * 10)
    self.assertFalse(f._rolled)
    self.assertEqual(f.mode, 'w+b')
    self.assertIsNone(f.name)
    with self.assertRaises(AttributeError):
        f.newlines
    with self.assertRaises(AttributeError):
        f.encoding
    with self.assertRaises(AttributeError):
        f.errors
    f.write(b'x')
    self.assertTrue(f._rolled)
    self.assertEqual(f.mode, 'rb+')
    self.assertIsNotNone(f.name)
    with self.assertRaises(AttributeError):
        f.newlines
    with self.assertRaises(AttributeError):
        f.encoding
    with self.assertRaises(AttributeError):
        f.errors
