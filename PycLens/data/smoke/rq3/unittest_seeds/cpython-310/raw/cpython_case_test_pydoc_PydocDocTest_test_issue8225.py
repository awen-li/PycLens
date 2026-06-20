# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_issue8225

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (result, doc_loc) = get_pydoc_text(xml.etree)
    self.assertEqual(doc_loc, '', 'MODULE DOCS incorrectly includes a link')
