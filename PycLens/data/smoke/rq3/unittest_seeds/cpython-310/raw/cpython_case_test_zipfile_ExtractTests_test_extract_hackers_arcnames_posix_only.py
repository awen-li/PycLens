# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ExtractTests_test_extract_hackers_arcnames_posix_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    posix_hacknames = [('//foo/bar', 'foo/bar'), ('../../foo../../ba..r', 'foo../ba..r'), ('foo/..\\bar', 'foo/..\\bar')]
    self._test_extract_hackers_arcnames(posix_hacknames)
