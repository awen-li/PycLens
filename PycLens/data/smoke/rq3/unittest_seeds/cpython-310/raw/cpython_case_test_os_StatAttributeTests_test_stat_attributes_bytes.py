# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: StatAttributeTests_test_stat_attributes_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        fname = self.fname.encode(sys.getfilesystemencoding())
    except UnicodeEncodeError:
        self.skipTest('cannot encode %a for the filesystem' % self.fname)
    self.check_stat_attributes(fname)
