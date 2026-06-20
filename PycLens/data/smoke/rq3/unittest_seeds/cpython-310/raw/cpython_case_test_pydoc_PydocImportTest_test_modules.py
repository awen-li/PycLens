# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocImportTest_test_modules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    num_header_lines = 2
    num_module_lines_min = 5
    num_footer_lines = 3
    expected = num_header_lines + num_module_lines_min + num_footer_lines
    output = StringIO()
    helper = pydoc.Helper(output=output)
    helper('modules')
    result = output.getvalue().strip()
    num_lines = len(result.splitlines())
    self.assertGreaterEqual(num_lines, expected)
