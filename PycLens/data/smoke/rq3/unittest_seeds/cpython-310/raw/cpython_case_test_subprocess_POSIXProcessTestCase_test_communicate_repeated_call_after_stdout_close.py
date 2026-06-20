# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_communicate_repeated_call_after_stdout_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    proc = subprocess.Popen([sys.executable, '-c', 'import os, time; os.close(1), time.sleep(2)'], stdout=subprocess.PIPE)
    while True:
        try:
            proc.communicate(timeout=0.1)
            return
        except subprocess.TimeoutExpired:
            pass
