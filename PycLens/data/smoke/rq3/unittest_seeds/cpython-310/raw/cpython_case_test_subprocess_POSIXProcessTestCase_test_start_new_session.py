# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_start_new_session

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        output = subprocess.check_output([sys.executable, '-c', 'import os; print(os.getsid(0))'], start_new_session=True)
    except OSError as e:
        if e.errno != errno.EPERM:
            raise
    else:
        parent_sid = os.getsid(0)
        child_sid = int(output)
        self.assertNotEqual(parent_sid, child_sid)
