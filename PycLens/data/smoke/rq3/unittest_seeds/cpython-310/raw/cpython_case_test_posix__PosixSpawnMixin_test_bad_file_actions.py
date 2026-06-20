# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_bad_file_actions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = self.NOOP_PROGRAM
    with self.assertRaises(TypeError):
        self.spawn_func(args[0], args, os.environ, file_actions=[None])
    with self.assertRaises(TypeError):
        self.spawn_func(args[0], args, os.environ, file_actions=[()])
    with self.assertRaises(TypeError):
        self.spawn_func(args[0], args, os.environ, file_actions=[(None,)])
    with self.assertRaises(TypeError):
        self.spawn_func(args[0], args, os.environ, file_actions=[(12345,)])
    with self.assertRaises(TypeError):
        self.spawn_func(args[0], args, os.environ, file_actions=[(os.POSIX_SPAWN_CLOSE,)])
    with self.assertRaises(TypeError):
        self.spawn_func(args[0], args, os.environ, file_actions=[(os.POSIX_SPAWN_CLOSE, 1, 2)])
    with self.assertRaises(TypeError):
        self.spawn_func(args[0], args, os.environ, file_actions=[(os.POSIX_SPAWN_CLOSE, None)])
    with self.assertRaises(ValueError):
        self.spawn_func(args[0], args, os.environ, file_actions=[(os.POSIX_SPAWN_OPEN, 3, __file__ + '\x00', os.O_RDONLY, 0)])
