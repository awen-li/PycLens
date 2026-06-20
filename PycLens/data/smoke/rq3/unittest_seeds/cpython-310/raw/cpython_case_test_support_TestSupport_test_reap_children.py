# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_reap_children

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.reap_children()
    pid = os.fork()
    if pid == 0:
        os._exit(0)
    t0 = time.monotonic()
    deadline = time.monotonic() + support.SHORT_TIMEOUT
    was_altered = support.environment_altered
    try:
        support.environment_altered = False
        stderr = io.StringIO()
        while True:
            if time.monotonic() > deadline:
                self.fail('timeout')
            old_stderr = sys.__stderr__
            try:
                sys.__stderr__ = stderr
                support.reap_children()
            finally:
                sys.__stderr__ = old_stderr
            if support.environment_altered:
                break
            time.sleep(0.1)
        msg = 'Warning -- reap_children() reaped child process %s' % pid
        self.assertIn(msg, stderr.getvalue())
        self.assertTrue(support.environment_altered)
    finally:
        support.environment_altered = was_altered
    support.reap_children()
