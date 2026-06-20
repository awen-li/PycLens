# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ModuleTest_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    names = ('xml.etree.ElementTree', '_elementtree')
    support.check__all__(self, ET, names, not_exported=('HTML_EMPTY',))
