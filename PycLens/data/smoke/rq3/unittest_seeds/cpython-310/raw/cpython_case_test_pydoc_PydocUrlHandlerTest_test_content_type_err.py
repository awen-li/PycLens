# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocUrlHandlerTest_test_content_type_err

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = pydoc._url_handler
    self.assertRaises(TypeError, f, 'A', '')
    self.assertRaises(TypeError, f, 'B', 'foobar')
