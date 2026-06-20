# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_close_fds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd_status = support.findfile('fd_status.py', subdir='subprocessdata')
    fds = os.pipe()
    self.addCleanup(os.close, fds[0])
    self.addCleanup(os.close, fds[1])
    open_fds = set(fds)
    for _ in range(9):
        fd = os.open(os.devnull, os.O_RDONLY)
        self.addCleanup(os.close, fd)
        open_fds.add(fd)
    for fd in open_fds:
        os.set_inheritable(fd, True)
    p = subprocess.Popen([sys.executable, fd_status], stdout=subprocess.PIPE, close_fds=False)
    (output, ignored) = p.communicate()
    remaining_fds = set(map(int, output.split(b',')))
    self.assertEqual(remaining_fds & open_fds, open_fds, 'Some fds were closed')
    p = subprocess.Popen([sys.executable, fd_status], stdout=subprocess.PIPE, close_fds=True)
    (output, ignored) = p.communicate()
    remaining_fds = set(map(int, output.split(b',')))
    self.assertFalse(remaining_fds & open_fds, 'Some fds were left open')
    self.assertIn(1, remaining_fds, 'Subprocess failed')
    fds_to_keep = set((open_fds.pop() for _ in range(8)))
    p = subprocess.Popen([sys.executable, fd_status], stdout=subprocess.PIPE, close_fds=True, pass_fds=fds_to_keep)
    (output, ignored) = p.communicate()
    remaining_fds = set(map(int, output.split(b',')))
    self.assertFalse(remaining_fds - fds_to_keep & open_fds, 'Some fds not in pass_fds were left open')
    self.assertIn(1, remaining_fds, 'Subprocess failed')
