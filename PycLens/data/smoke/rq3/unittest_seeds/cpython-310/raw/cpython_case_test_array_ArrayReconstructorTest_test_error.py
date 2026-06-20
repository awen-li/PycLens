# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: ArrayReconstructorTest_test_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, array_reconstructor, '', 'b', 0, b'')
    self.assertRaises(TypeError, array_reconstructor, str, 'b', 0, b'')
    self.assertRaises(TypeError, array_reconstructor, array.array, 'b', '', b'')
    self.assertRaises(TypeError, array_reconstructor, array.array, 'b', 0, '')
    self.assertRaises(ValueError, array_reconstructor, array.array, '?', 0, b'')
    self.assertRaises(ValueError, array_reconstructor, array.array, 'b', UNKNOWN_FORMAT, b'')
    self.assertRaises(ValueError, array_reconstructor, array.array, 'b', 22, b'')
    self.assertRaises(ValueError, array_reconstructor, array.array, 'd', 16, b'a')
