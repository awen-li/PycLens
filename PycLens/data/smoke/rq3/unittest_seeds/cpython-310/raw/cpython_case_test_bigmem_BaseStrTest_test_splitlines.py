# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_splitlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    chunksize = int(size ** 0.5 + 2) // 2
    SUBSTR = _(' ') * chunksize + _('\n') + _(' ') * chunksize + _('\r\n')
    s = SUBSTR * (chunksize * 2)
    l = s.splitlines()
    self.assertEqual(len(l), chunksize * 4)
    expected = _(' ') * chunksize
    for item in l:
        self.assertEqual(item, expected)
