# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(alpharep)
    (a, b, g) = root.iterdir()
    assert a.read_text(encoding='utf-8') == 'content of a'
    a.read_text('utf-8')
    assert a.read_bytes() == b'content of a'
