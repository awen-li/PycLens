# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_run_with_bytes_path_and_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os.fsencode(sys.executable)
    args = [path, '-c', b'import sys; sys.exit(57)']
    res = subprocess.run(args)
    self.assertEqual(res.returncode, 57)
