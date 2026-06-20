# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_close_fds_after_preexec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd_status = support.findfile('fd_status.py', subdir='subprocessdata')
    fd = os.dup(1)
    self.addCleanup(os.close, fd)
    p = subprocess.Popen([sys.executable, fd_status], stdout=subprocess.PIPE, close_fds=True, preexec_fn=lambda : os.dup2(1, fd))
    (output, ignored) = p.communicate()
    remaining_fds = set(map(int, output.split(b',')))
    self.assertNotIn(fd, remaining_fds)
