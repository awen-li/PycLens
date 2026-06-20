# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocImportTest_test_modules_search

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = 'pydoc - '
    output = StringIO()
    helper = pydoc.Helper(output=output)
    with captured_stdout() as help_io:
        helper('modules pydoc')
    result = help_io.getvalue()
    self.assertIn(expected, result)
