# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cls = type('PathChild', (zipfile.Path,), {})
    for alpharep in self.zipfile_alpharep():
        file = cls(alpharep).joinpath('some dir').parent
        assert isinstance(file, cls)
