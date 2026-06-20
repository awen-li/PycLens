# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_remapping_std_fds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    temps = [tempfile.mkstemp() for i in range(3)]
    try:
        temp_fds = [fd for (fd, fname) in temps]
        for (fd, fname) in temps:
            os.unlink(fname)
        os.write(temp_fds[1], b'STDIN')
        os.lseek(temp_fds[1], 0, 0)
        saved_fds = self._save_fds(range(3))
        try:
            for (fd, temp_fd) in enumerate(temp_fds):
                os.dup2(temp_fd, fd)
            p = subprocess.Popen([sys.executable, '-c', 'import sys; got = sys.stdin.read();sys.stdout.write("got %s"%got); sys.stderr.write("err")'], stdin=temp_fds[1], stdout=temp_fds[2], stderr=temp_fds[0])
            p.wait()
        finally:
            self._restore_fds(saved_fds)
        for fd in temp_fds:
            os.lseek(fd, 0, 0)
        out = os.read(temp_fds[2], 1024)
        err = os.read(temp_fds[0], 1024).strip()
        self.assertEqual(out, b'got STDIN')
        self.assertEqual(err, b'err')
    finally:
        for fd in temp_fds:
            os.close(fd)
