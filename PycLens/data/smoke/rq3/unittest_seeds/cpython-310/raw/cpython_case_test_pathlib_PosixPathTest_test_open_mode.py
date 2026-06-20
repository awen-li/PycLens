# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PosixPathTest_test_open_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_mask = os.umask(0)
    self.addCleanup(os.umask, old_mask)
    p = self.cls(BASE)
    with (p / 'new_file').open('wb'):
        pass
    st = os.stat(join('new_file'))
    self.assertEqual(stat.S_IMODE(st.st_mode), 438)
    os.umask(18)
    with (p / 'other_new_file').open('wb'):
        pass
    st = os.stat(join('other_new_file'))
    self.assertEqual(stat.S_IMODE(st.st_mode), 420)
