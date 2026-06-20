# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ContextManagerTests_test_returncode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with subprocess.Popen([sys.executable, '-c', 'import sys; sys.exit(100)']) as proc:
        pass
    self.assertEqual(proc.returncode, 100)
