# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_html_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (result, doc_loc) = get_pydoc_html(pydoc_mod)
    mod_file = inspect.getabsfile(pydoc_mod)
    mod_url = urllib.parse.quote(mod_file)
    expected_html = expected_html_pattern % ((mod_url, mod_file, doc_loc) + expected_html_data_docstrings)
    self.assertEqual(result, expected_html)
