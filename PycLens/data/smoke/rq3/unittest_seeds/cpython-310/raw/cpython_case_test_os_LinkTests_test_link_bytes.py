# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: LinkTests_test_link_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_link(bytes(self.file1, sys.getfilesystemencoding()), bytes(self.file2, sys.getfilesystemencoding()))
