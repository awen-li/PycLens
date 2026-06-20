# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_fcntl_f_pipesize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (test_pipe_r, test_pipe_w) = os.pipe()
    try:
        pipesize_default = fcntl.fcntl(test_pipe_w, fcntl.F_GETPIPE_SZ)
        pipesize = pipesize_default // 2
        if pipesize < 512:
            raise unittest.SkipTest('default pipesize too small to perform test.')
        fcntl.fcntl(test_pipe_w, fcntl.F_SETPIPE_SZ, pipesize)
        self.assertEqual(fcntl.fcntl(test_pipe_w, fcntl.F_GETPIPE_SZ), pipesize)
    finally:
        os.close(test_pipe_r)
        os.close(test_pipe_w)
