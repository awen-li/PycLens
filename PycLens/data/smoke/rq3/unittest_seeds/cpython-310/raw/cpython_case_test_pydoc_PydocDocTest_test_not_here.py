# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_not_here

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    missing_module = 'test.i_am_not_here'
    result = str(run_pydoc(missing_module), 'ascii')
    expected = missing_pattern % missing_module
    self.assertEqual(expected, result, 'documentation for missing module found')
