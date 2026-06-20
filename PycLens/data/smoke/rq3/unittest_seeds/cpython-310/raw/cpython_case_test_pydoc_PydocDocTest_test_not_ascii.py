# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_not_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = run_pydoc('test.test_pydoc.nonascii', PYTHONIOENCODING='ascii')
    encoded = nonascii.__doc__.encode('ascii', 'backslashreplace')
    self.assertIn(encoded, result)
