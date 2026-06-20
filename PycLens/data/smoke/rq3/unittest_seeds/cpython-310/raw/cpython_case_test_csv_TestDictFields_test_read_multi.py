# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_read_multi

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sample = ['2147483648,43.0e12,17,abc,def\r\n', '147483648,43.0e2,17,abc,def\r\n', '47483648,43.0,170,abc,def\r\n']
    reader = csv.DictReader(sample, fieldnames='i1 float i2 s1 s2'.split())
    self.assertEqual(next(reader), {'i1': '2147483648', 'float': '43.0e12', 'i2': '17', 's1': 'abc', 's2': 'def'})
