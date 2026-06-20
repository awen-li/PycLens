# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: ScalableSelectorMixIn_test_above_fd_setsize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (soft, hard) = resource.getrlimit(resource.RLIMIT_NOFILE)
    try:
        resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
        self.addCleanup(resource.setrlimit, resource.RLIMIT_NOFILE, (soft, hard))
        NUM_FDS = min(hard, 2 ** 16)
    except (OSError, ValueError):
        NUM_FDS = soft
    NUM_FDS -= 32
    s = self.SELECTOR()
    self.addCleanup(s.close)
    for i in range(NUM_FDS // 2):
        try:
            (rd, wr) = self.make_socketpair()
        except OSError:
            self.skipTest('FD limit reached')
        try:
            s.register(rd, selectors.EVENT_READ)
            s.register(wr, selectors.EVENT_WRITE)
        except OSError as e:
            if e.errno == errno.ENOSPC:
                self.skipTest('FD limit reached')
            raise
    try:
        fds = s.select()
    except OSError as e:
        if e.errno == errno.EINVAL and sys.platform == 'darwin':
            self.skipTest('Invalid argument error calling poll()')
        raise
    self.assertEqual(NUM_FDS // 2, len(fds))
