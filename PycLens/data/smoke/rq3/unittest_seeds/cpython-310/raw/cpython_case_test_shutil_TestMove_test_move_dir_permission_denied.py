# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_dir_permission_denied

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.mkdir(TESTFN_SRC)
        os.lchflags(TESTFN_SRC, stat.SF_IMMUTABLE)
        self.assertRaises(PermissionError, shutil.move, TESTFN_SRC, TESTFN_DST)
        self.assertFalse(TESTFN_DST in os.listdir())
        os.lchflags(TESTFN_SRC, stat.UF_OPAQUE)
        os_helper.create_empty_file(os.path.join(TESTFN_SRC, 'child'))
        os.lchflags(TESTFN_SRC, stat.SF_IMMUTABLE)
        self.assertRaises(PermissionError, shutil.move, TESTFN_SRC, TESTFN_DST)
        self.assertFalse(TESTFN_DST in os.listdir())
    finally:
        if os.path.exists(TESTFN_SRC):
            os.lchflags(TESTFN_SRC, stat.UF_OPAQUE)
            os_helper.rmtree(TESTFN_SRC)
        if os.path.exists(TESTFN_DST):
            os.lchflags(TESTFN_DST, stat.UF_OPAQUE)
            os_helper.rmtree(TESTFN_DST)
