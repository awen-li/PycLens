# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectExcel_test_quoted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.readerAssertEqual('1,2,3,"I think, therefore I am",5,6', [['1', '2', '3', 'I think, therefore I am', '5', '6']])
