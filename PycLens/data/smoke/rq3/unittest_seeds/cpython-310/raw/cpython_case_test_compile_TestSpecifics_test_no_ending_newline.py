# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_no_ending_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    compile('hi', '<test>', 'exec')
    compile('hi\r', '<test>', 'exec')
