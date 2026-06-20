# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_run_abort

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.SuppressCrashReport():
        p = subprocess.Popen([sys.executable, '-c', 'import os; os.abort()'])
        p.wait()
    self.assertEqual(-p.returncode, signal.SIGABRT)
