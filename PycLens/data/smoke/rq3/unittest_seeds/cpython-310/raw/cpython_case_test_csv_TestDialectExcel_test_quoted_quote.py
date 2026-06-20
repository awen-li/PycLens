# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectExcel_test_quoted_quote

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.readerAssertEqual('1,2,3,"""I see,"" said the blind man","as he picked up his hammer and saw"', [['1', '2', '3', '"I see," said the blind man', 'as he picked up his hammer and saw']])
