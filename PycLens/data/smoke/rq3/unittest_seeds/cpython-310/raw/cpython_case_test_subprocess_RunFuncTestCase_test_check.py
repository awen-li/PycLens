# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(subprocess.CalledProcessError) as c:
        self.run_python('import sys; sys.exit(47)', check=True)
    self.assertEqual(c.exception.returncode, 47)
