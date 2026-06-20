# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_invalid_cmd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cmd = sys.executable + '\x00'
    with self.assertRaises(ValueError):
        subprocess.Popen([cmd, '-c', 'pass'])
    with self.assertRaises(ValueError):
        subprocess.Popen([sys.executable, '-c', 'pass#\x00'])
