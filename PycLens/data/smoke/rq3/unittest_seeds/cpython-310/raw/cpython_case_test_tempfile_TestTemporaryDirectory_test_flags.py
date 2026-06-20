# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    flags = stat.UF_IMMUTABLE | stat.UF_NOUNLINK
    d = self.do_create(recurse=3, dirs=2, files=2)
    with d:
        for (root, dirs, files) in os.walk(d.name, topdown=False):
            for name in files:
                os.chflags(os.path.join(root, name), flags)
            os.chflags(root, flags)
        d.cleanup()
    self.assertFalse(os.path.exists(d.name))
