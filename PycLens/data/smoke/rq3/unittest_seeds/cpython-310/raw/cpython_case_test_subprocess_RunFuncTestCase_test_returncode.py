# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_returncode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cp = self.run_python('import sys; sys.exit(47)')
    self.assertEqual(cp.returncode, 47)
    with self.assertRaises(subprocess.CalledProcessError):
        cp.check_returncode()
