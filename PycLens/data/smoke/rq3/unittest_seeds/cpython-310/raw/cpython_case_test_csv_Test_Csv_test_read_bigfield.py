# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_read_bigfield

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    limit = csv.field_size_limit()
    try:
        size = 50000
        bigstring = 'X' * size
        bigline = '%s,%s' % (bigstring, bigstring)
        self._read_test([bigline], [[bigstring, bigstring]])
        csv.field_size_limit(size)
        self._read_test([bigline], [[bigstring, bigstring]])
        self.assertEqual(csv.field_size_limit(), size)
        csv.field_size_limit(size - 1)
        self.assertRaises(csv.Error, self._read_test, [bigline], [])
        self.assertRaises(TypeError, csv.field_size_limit, None)
        self.assertRaises(TypeError, csv.field_size_limit, 1, None)
    finally:
        csv.field_size_limit(limit)
