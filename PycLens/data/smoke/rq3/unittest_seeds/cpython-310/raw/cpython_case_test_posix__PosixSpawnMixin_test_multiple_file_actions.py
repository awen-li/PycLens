# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_multiple_file_actions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    file_actions = [(os.POSIX_SPAWN_OPEN, 3, os.path.realpath(__file__), os.O_RDONLY, 0), (os.POSIX_SPAWN_CLOSE, 0), (os.POSIX_SPAWN_DUP2, 1, 4)]
    pid = self.spawn_func(self.NOOP_PROGRAM[0], self.NOOP_PROGRAM, os.environ, file_actions=file_actions)
    support.wait_process(pid, exitcode=0)
