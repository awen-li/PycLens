# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_root_parent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(alpharep)
    assert root.parent == pathlib.Path('.')
    root.root.filename = 'foo/bar.zip'
    assert root.parent == pathlib.Path('foo')
