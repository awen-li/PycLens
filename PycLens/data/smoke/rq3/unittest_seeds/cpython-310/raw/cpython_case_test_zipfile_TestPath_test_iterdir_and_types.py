# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_iterdir_and_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(alpharep)
    assert root.is_dir()
    (a, b, g) = root.iterdir()
    assert a.is_file()
    assert b.is_dir()
    assert g.is_dir()
    (c, f, d) = b.iterdir()
    assert c.is_file() and f.is_file()
    (e,) = d.iterdir()
    assert e.is_file()
    (h,) = g.iterdir()
    (i,) = h.iterdir()
    assert i.is_file()
