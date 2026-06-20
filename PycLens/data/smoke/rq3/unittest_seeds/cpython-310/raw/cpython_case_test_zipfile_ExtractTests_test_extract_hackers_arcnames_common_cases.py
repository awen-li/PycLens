# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ExtractTests_test_extract_hackers_arcnames_common_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    common_hacknames = [('../foo/bar', 'foo/bar'), ('foo/../bar', 'foo/bar'), ('foo/../../bar', 'foo/bar'), ('foo/bar/..', 'foo/bar'), ('./../foo/bar', 'foo/bar'), ('/foo/bar', 'foo/bar'), ('/foo/../bar', 'foo/bar'), ('/foo/../../bar', 'foo/bar')]
    self._test_extract_hackers_arcnames(common_hacknames)
