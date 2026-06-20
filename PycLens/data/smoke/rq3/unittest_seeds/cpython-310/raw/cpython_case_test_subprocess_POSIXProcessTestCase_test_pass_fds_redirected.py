# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_pass_fds_redirected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd_status = support.findfile('fd_status.py', subdir='subprocessdata')
    pass_fds = []
    for _ in range(2):
        fd = os.open(os.devnull, os.O_RDWR)
        self.addCleanup(os.close, fd)
        pass_fds.append(fd)
    (stdout_r, stdout_w) = os.pipe()
    self.addCleanup(os.close, stdout_r)
    self.addCleanup(os.close, stdout_w)
    pass_fds.insert(1, stdout_w)
    with subprocess.Popen([sys.executable, fd_status], stdin=pass_fds[0], stdout=pass_fds[1], stderr=pass_fds[2], close_fds=True, pass_fds=pass_fds):
        output = os.read(stdout_r, 1024)
    fds = {int(num) for num in output.split(b',')}
    self.assertEqual(fds, {0, 1, 2} | frozenset(pass_fds), f'output={output!a}')
