# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: SizeofTest_test_element_with_attrib

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = cET.Element('a', href='about:')
    self.check_sizeof(e, self.elementsize + self.extra)
