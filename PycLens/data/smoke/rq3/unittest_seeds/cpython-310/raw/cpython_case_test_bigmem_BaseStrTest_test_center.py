# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_center

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    SUBSTR = self.from_latin1(' abc def ghi')
    s = SUBSTR.center(size)
    self.assertEqual(len(s), size)
    lpadsize = rpadsize = (len(s) - len(SUBSTR)) // 2
    if len(s) % 2:
        lpadsize += 1
    self.assertEqual(s[lpadsize:-rpadsize], SUBSTR)
    self.assertEqual(s.strip(), SUBSTR.strip())
