# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_unknown_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_failure('-E', '-z')
    self.assertIn(b'Unknown option: -z', err)
    self.assertEqual(err.splitlines().count(b'Unknown option: -z'), 1)
    self.assertEqual(b'', out)
    (rc, out, err) = assert_python_failure('-z', without='-E')
    self.assertIn(b'Unknown option: -z', err)
    self.assertEqual(err.splitlines().count(b'Unknown option: -z'), 1)
    self.assertEqual(b'', out)
    (rc, out, err) = assert_python_failure('-a', '-z', without='-E')
    self.assertIn(b'Unknown option: -a', err)
    self.assertNotIn(b'Unknown option: -z', err)
    self.assertEqual(err.splitlines().count(b'Unknown option: -a'), 1)
    self.assertEqual(b'', out)
