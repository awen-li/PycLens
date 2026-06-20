# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_setscheduler_with_policy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    policy = os.sched_getscheduler(0)
    priority = os.sched_get_priority_min(policy)
    code = textwrap.dedent(f'            import os, sys\n            if os.sched_getscheduler(0) != {policy}:\n                sys.exit(101)\n            if os.sched_getparam(0).sched_priority != {priority}:\n                sys.exit(102)')
    pid = self.spawn_func(sys.executable, [sys.executable, '-c', code], os.environ, scheduler=(policy, os.sched_param(priority)))
    support.wait_process(pid, exitcode=0)
