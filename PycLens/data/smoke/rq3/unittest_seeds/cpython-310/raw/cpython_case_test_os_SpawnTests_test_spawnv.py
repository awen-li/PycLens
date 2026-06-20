# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: SpawnTests_test_spawnv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = self.create_args()
    exitcode = os.spawnv(os.P_WAIT, args[0], args)
    self.assertEqual(exitcode, self.exitcode)
    exitcode = os.spawnv(os.P_WAIT, FakePath(args[0]), args)
    self.assertEqual(exitcode, self.exitcode)
