# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ProgramPriorityTests_test_set_get_priority

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = os.getpriority(os.PRIO_PROCESS, os.getpid())
    os.setpriority(os.PRIO_PROCESS, os.getpid(), base + 1)
    try:
        new_prio = os.getpriority(os.PRIO_PROCESS, os.getpid())
        if base >= 19 and new_prio <= 19:
            raise unittest.SkipTest('unable to reliably test setpriority at current nice level of %s' % base)
        else:
            self.assertEqual(new_prio, base + 1)
    finally:
        try:
            os.setpriority(os.PRIO_PROCESS, os.getpid(), base)
        except OSError as err:
            if err.errno != errno.EACCES:
                raise
