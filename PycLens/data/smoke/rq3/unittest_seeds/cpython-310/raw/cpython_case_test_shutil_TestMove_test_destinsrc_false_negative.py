# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_destinsrc_false_negative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(TESTFN)
    try:
        for (src, dst) in [('srcdir', 'srcdir/dest')]:
            src = os.path.join(TESTFN, src)
            dst = os.path.join(TESTFN, dst)
            self.assertTrue(shutil._destinsrc(src, dst), msg='_destinsrc() wrongly concluded that dst (%s) is not in src (%s)' % (dst, src))
    finally:
        os_helper.rmtree(TESTFN)
