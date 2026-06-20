# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_destinsrc_false_positive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(TESTFN)
    try:
        for (src, dst) in [('srcdir', 'src/dest'), ('srcdir', 'srcdir.new')]:
            src = os.path.join(TESTFN, src)
            dst = os.path.join(TESTFN, dst)
            self.assertFalse(shutil._destinsrc(src, dst), msg='_destinsrc() wrongly concluded that dst (%s) is in src (%s)' % (dst, src))
    finally:
        os_helper.rmtree(TESTFN)
