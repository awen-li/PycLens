# Source Generated with Decompyle++
# File: cpython-311-00793480a4f7.pyc (Python 3.11)

(lambda : self = object()__pybcsec_self__ = object()__pybcsec_self__ = selfexpected_schemes = {
'home',
'user',
'prefix'}os.name = 'nt'schemes = None(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, _get_preferred_schemes)self.assertIsInstance(schemes, dict)self.assertEqual(set(schemes), expected_schemes)os.name = 'posix'schemes = _get_preferred_schemes()self.assertIsInstance(schemes, dict)self.assertEqual(set(schemes), expected_schemes)os.name = 'posix'sys.platform = 'darwin'sys._framework = Trueself.assertIsInstance(schemes, dict)self.assertEqual(set(schemes), expected_schemes)).__pybcsec_seed__ = None
if __name__ == '__main__':
    __pybcsec_seed__()
    return None
