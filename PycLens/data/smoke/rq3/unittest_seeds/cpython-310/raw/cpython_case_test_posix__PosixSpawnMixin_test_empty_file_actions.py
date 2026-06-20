# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_empty_file_actions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pid = self.spawn_func(self.NOOP_PROGRAM[0], self.NOOP_PROGRAM, os.environ, file_actions=[])
    support.wait_process(pid, exitcode=0)
