# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_mixed_case_module_names_are_lower_cased

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    doc_link = get_pydoc_link(xml.etree.ElementTree)
    self.assertIn('xml.etree.elementtree', doc_link)
