# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestLowLevelInternals_test_infer_return_type_multiples_and_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(str, tempfile._infer_return_type(None, ''))
    self.assertIs(str, tempfile._infer_return_type('', None))
    self.assertIs(str, tempfile._infer_return_type(None, None))
    self.assertIs(bytes, tempfile._infer_return_type(b'', None))
    self.assertIs(bytes, tempfile._infer_return_type(None, b''))
    with self.assertRaises(TypeError):
        tempfile._infer_return_type('', None, b'')
    with self.assertRaises(TypeError):
        tempfile._infer_return_type(b'', None, '')
