# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_subdir_is_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(alpharep)
    assert (root / 'b').is_dir()
    assert (root / 'b/').is_dir()
    assert (root / 'g').is_dir()
    assert (root / 'g/').is_dir()
