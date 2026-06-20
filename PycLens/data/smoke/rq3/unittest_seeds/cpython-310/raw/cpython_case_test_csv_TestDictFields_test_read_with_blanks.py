# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_read_with_blanks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    reader = csv.DictReader(['1,2,abc,4,5,6\r\n', '\r\n', '1,2,abc,4,5,6\r\n'], fieldnames='1 2 3 4 5 6'.split())
    self.assertEqual(next(reader), {'1': '1', '2': '2', '3': 'abc', '4': '4', '5': '5', '6': '6'})
    self.assertEqual(next(reader), {'1': '1', '2': '2', '3': 'abc', '4': '4', '5': '5', '6': '6'})
