# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_lockf_exclusive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.f = open(TESTFN, 'wb+')
    cmd = fcntl.LOCK_EX | fcntl.LOCK_NB
    fcntl.lockf(self.f, cmd)
    p = Process(target=try_lockf_on_other_process_fail, args=(TESTFN, cmd))
    p.start()
    p.join()
    fcntl.lockf(self.f, fcntl.LOCK_UN)
    self.assertEqual(p.exitcode, 0)
