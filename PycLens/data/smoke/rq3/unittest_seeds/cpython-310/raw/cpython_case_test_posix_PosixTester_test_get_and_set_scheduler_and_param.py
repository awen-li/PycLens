# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_get_and_set_scheduler_and_param

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    possible_schedulers = [sched for (name, sched) in posix.__dict__.items() if name.startswith('SCHED_')]
    mine = posix.sched_getscheduler(0)
    self.assertIn(mine, possible_schedulers)
    try:
        parent = posix.sched_getscheduler(os.getppid())
    except OSError as e:
        if e.errno != errno.EPERM:
            raise
    else:
        self.assertIn(parent, possible_schedulers)
    self.assertRaises(OSError, posix.sched_getscheduler, -1)
    self.assertRaises(OSError, posix.sched_getparam, -1)
    param = posix.sched_getparam(0)
    self.assertIsInstance(param.sched_priority, int)
    if not sys.platform.startswith(('freebsd', 'netbsd')):
        try:
            posix.sched_setscheduler(0, mine, param)
            posix.sched_setparam(0, param)
        except OSError as e:
            if e.errno != errno.EPERM:
                raise
        self.assertRaises(OSError, posix.sched_setparam, -1, param)
    self.assertRaises(OSError, posix.sched_setscheduler, -1, mine, param)
    self.assertRaises(TypeError, posix.sched_setscheduler, 0, mine, None)
    self.assertRaises(TypeError, posix.sched_setparam, 0, 43)
    param = posix.sched_param(None)
    self.assertRaises(TypeError, posix.sched_setparam, 0, param)
    large = 214748364700
    param = posix.sched_param(large)
    self.assertRaises(OverflowError, posix.sched_setparam, 0, param)
    param = posix.sched_param(sched_priority=-large)
    self.assertRaises(OverflowError, posix.sched_setparam, 0, param)
