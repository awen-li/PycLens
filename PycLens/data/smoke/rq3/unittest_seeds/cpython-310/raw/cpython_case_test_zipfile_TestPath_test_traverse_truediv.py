# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_traverse_truediv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(alpharep)
    a = root / 'a.txt'
    assert a.is_file()
    e = root / 'b' / 'd' / 'e.txt'
    assert e.read_text(encoding='utf-8') == 'content of e'
