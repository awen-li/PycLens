# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: GetpassRawinputTest_test_trims_trailing_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input = StringIO('test\n')
    self.assertEqual('test', getpass._raw_input(input=input))
