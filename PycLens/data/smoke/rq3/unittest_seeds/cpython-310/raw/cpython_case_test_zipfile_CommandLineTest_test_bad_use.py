# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: CommandLineTest_test_bad_use

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = self.zipfilecmd_failure()
    self.assertEqual(out, b'')
    self.assertIn(b'usage', err.lower())
    self.assertIn(b'error', err.lower())
    self.assertIn(b'required', err.lower())
    (rc, out, err) = self.zipfilecmd_failure('-l', '')
    self.assertEqual(out, b'')
    self.assertNotEqual(err.strip(), b'')
