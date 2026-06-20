# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestStdLib_test_pydoc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if StrEnum.__doc__ is None:
        expected_text = expected_help_output_without_docs % __name__
    else:
        expected_text = expected_help_output_with_docs % __name__
    output = StringIO()
    helper = pydoc.Helper(output=output)
    helper(self.Color)
    result = output.getvalue().strip()
    self.assertEqual(result, expected_text)
