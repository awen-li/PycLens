# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_setsid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rfd, wfd) = os.pipe()
    self.addCleanup(os.close, rfd)
    try:
        os.set_inheritable(wfd, True)
        code = textwrap.dedent(f'\n                import os\n                fd = {wfd}\n                sid = os.getsid(0)\n                os.write(fd, str(sid).encode())\n            ')
        try:
            pid = self.spawn_func(sys.executable, [sys.executable, '-c', code], os.environ, setsid=True)
        except NotImplementedError as exc:
            self.skipTest(f'setsid is not supported: {exc!r}')
        except PermissionError as exc:
            self.skipTest(f'setsid failed with: {exc!r}')
    finally:
        os.close(wfd)
    support.wait_process(pid, exitcode=0)
    output = os.read(rfd, 100)
    child_sid = int(output)
    parent_sid = os.getsid(os.getpid())
    self.assertNotEqual(parent_sid, child_sid)
