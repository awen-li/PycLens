# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_setsigmask_wrong_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        self.spawn_func(sys.executable, [sys.executable, '-c', 'pass'], os.environ, setsigmask=34)
    with self.assertRaises(TypeError):
        self.spawn_func(sys.executable, [sys.executable, '-c', 'pass'], os.environ, setsigmask=['j'])
    with self.assertRaises(ValueError):
        self.spawn_func(sys.executable, [sys.executable, '-c', 'pass'], os.environ, setsigmask=[signal.NSIG, signal.NSIG + 1])
