# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_root_unnamed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    alpharep.filename = None
    root = zipfile.Path(alpharep)
    with self.assertRaises(TypeError):
        root.name
    with self.assertRaises(TypeError):
        root.parent
    sub = root / 'b'
    assert sub.name == 'b'
    assert sub.parent
