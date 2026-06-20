# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_text_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (result, doc_loc) = get_pydoc_text(pydoc_mod)
    expected_text = expected_text_pattern % ((doc_loc,) + expected_text_data_docstrings + (inspect.getabsfile(pydoc_mod),))
    self.assertEqual(expected_text, result)
