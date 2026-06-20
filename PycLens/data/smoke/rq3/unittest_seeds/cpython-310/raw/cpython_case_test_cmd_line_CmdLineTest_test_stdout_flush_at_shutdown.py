# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_stdout_flush_at_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "if 1:\n            import os, sys, test.support\n            test.support.SuppressCrashReport().__enter__()\n            sys.stdout.write('x')\n            os.close(sys.stdout.fileno())"
    (rc, out, err) = assert_python_failure('-c', code)
    self.assertEqual(b'', out)
    self.assertEqual(120, rc)
    self.assertRegex(err.decode('ascii', 'ignore'), 'Exception ignored in.*\nOSError: .*')
