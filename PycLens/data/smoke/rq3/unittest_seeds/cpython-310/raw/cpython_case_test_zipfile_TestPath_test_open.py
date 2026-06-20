# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(alpharep)
    (a, b, g) = root.iterdir()
    with a.open(encoding='utf-8') as strm:
        data = strm.read()
    self.assertEqual(data, 'content of a')
    with a.open('r', 'utf-8') as strm:
        data = strm.read()
    self.assertEqual(data, 'content of a')
