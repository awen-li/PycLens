# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_getgroups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os.popen('id -G 2>/dev/null') as idg:
        groups = idg.read().strip()
        ret = idg.close()
    try:
        idg_groups = set((int(g) for g in groups.split()))
    except ValueError:
        idg_groups = set()
    if ret is not None or not idg_groups:
        raise unittest.SkipTest("need working 'id -G'")
    if sys.platform == 'darwin':
        import sysconfig
        dt = sysconfig.get_config_var('MACOSX_DEPLOYMENT_TARGET') or '10.3'
        if tuple((int(n) for n in dt.split('.')[0:2])) < (10, 6):
            raise unittest.SkipTest('getgroups(2) is broken prior to 10.6')
    symdiff = idg_groups.symmetric_difference(posix.getgroups())
    self.assertTrue(not symdiff or symdiff == {posix.getegid()})
