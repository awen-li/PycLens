# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: Win32ProcessTestCase_test_creationflags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    CREATE_NEW_CONSOLE = 16
    sys.stderr.write('    a DOS box should flash briefly ...\n')
    subprocess.call(sys.executable + ' -c "import time; time.sleep(0.25)"', creationflags=CREATE_NEW_CONSOLE)
