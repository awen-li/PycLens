# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_read_quoting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._read_test(['1,",3,",5'], [['1', ',3,', '5']])
    self._read_test(['1,",3,",5'], [['1', '"', '3', '"', '5']], quotechar=None, escapechar='\\')
    self._read_test(['1,",3,",5'], [['1', '"', '3', '"', '5']], quoting=csv.QUOTE_NONE, escapechar='\\')
    self._read_test([',3,"5",7.3, 9'], [['', 3, '5', 7.3, 9]], quoting=csv.QUOTE_NONNUMERIC)
    self._read_test(['"a\nb", 7'], [['a\nb', ' 7']])
    self.assertRaises(ValueError, self._read_test, ['abc,3'], [[]], quoting=csv.QUOTE_NONNUMERIC)
