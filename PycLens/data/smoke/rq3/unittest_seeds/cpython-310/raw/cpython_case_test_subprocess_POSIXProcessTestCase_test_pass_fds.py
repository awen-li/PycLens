# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_pass_fds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd_status = support.findfile('fd_status.py', subdir='subprocessdata')
    open_fds = set()
    for x in range(5):
        fds = os.pipe()
        self.addCleanup(os.close, fds[0])
        self.addCleanup(os.close, fds[1])
        os.set_inheritable(fds[0], True)
        os.set_inheritable(fds[1], True)
        open_fds.update(fds)
    for fd in open_fds:
        p = subprocess.Popen([sys.executable, fd_status], stdout=subprocess.PIPE, close_fds=True, pass_fds=(fd,))
        (output, ignored) = p.communicate()
        remaining_fds = set(map(int, output.split(b',')))
        to_be_closed = open_fds - {fd}
        self.assertIn(fd, remaining_fds, 'fd to be passed not passed')
        self.assertFalse(remaining_fds & to_be_closed, 'fd to be closed passed')
        with self.assertWarns(RuntimeWarning) as context:
            self.assertFalse(subprocess.call(ZERO_RETURN_CMD, close_fds=False, pass_fds=(fd,)))
        self.assertIn('overriding close_fds', str(context.warning))
