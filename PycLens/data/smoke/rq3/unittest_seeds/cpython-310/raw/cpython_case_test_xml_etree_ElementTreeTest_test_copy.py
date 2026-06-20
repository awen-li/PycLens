# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import copy
    e1 = ET.XML('<tag>hello<foo/></tag>')
    e2 = copy.copy(e1)
    e3 = copy.deepcopy(e1)
    e1.find('foo').tag = 'bar'
    self.serialize_check(e1, '<tag>hello<bar /></tag>')
    self.serialize_check(e2, '<tag>hello<bar /></tag>')
    self.serialize_check(e3, '<tag>hello<foo /></tag>')
