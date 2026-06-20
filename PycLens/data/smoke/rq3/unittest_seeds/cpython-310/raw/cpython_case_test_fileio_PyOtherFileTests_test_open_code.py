# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileio.py
# case: PyOtherFileTests_test_open_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.FileIO(__file__, 'rb') as f:
        expected = f.read()
    with check_warnings(quiet=True) as w:
        with _pyio._open_code_with_warning(__file__) as f:
            actual = f.read()
        self.assertEqual(expected, actual)
        self.assertNotEqual(w.warnings, [])
