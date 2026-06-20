# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectExcel_test_quoted_nl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input = '1,2,3,"""I see,""\nsaid the blind man","as he picked up his\nhammer and saw"\n9,8,7,6'
    self.readerAssertEqual(input, [['1', '2', '3', '"I see,"\nsaid the blind man', 'as he picked up his\nhammer and saw'], ['9', '8', '7', '6']])
