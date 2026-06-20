# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_stdout_stderr_are_single_inout_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with io.open(os.devnull, 'r+') as inout:
        p = subprocess.Popen(ZERO_RETURN_CMD, stdout=inout, stderr=inout)
        p.wait()
