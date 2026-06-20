# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pty.py
# case: SmallPtyTests_test__restore_tty_mode_normal_return

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pty.fork = self._make_mock_fork(1)
    status_sentinel = object()
    pty.waitpid = lambda _1, _2: [None, status_sentinel]
    pty.close = lambda _: None
    pty._copy = lambda _1, _2, _3: None
    mode_sentinel = object()
    pty.tcgetattr = lambda fd: mode_sentinel
    pty.tcsetattr = self._mock_tcsetattr
    pty.setraw = lambda _: None
    self.assertEqual(pty.spawn([]), status_sentinel, 'pty.waitpid process status not returned by pty.spawn')
    self.assertEqual(self.tcsetattr_mode_setting, mode_sentinel, 'pty.tcsetattr not called with original mode value')
