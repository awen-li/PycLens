# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: SpawnTests_test_spawnv_noargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = self.create_args()
    self.assertRaises(ValueError, os.spawnv, os.P_NOWAIT, args[0], ())
    self.assertRaises(ValueError, os.spawnv, os.P_NOWAIT, args[0], [])
    self.assertRaises(ValueError, os.spawnv, os.P_NOWAIT, args[0], ('',))
    self.assertRaises(ValueError, os.spawnv, os.P_NOWAIT, args[0], [''])
