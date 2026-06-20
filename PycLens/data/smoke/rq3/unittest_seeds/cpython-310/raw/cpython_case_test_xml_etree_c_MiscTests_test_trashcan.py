# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_trashcan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = root = cET.Element('root')
    for i in range(200000):
        e = cET.SubElement(e, 'x')
    del e
    del root
    support.gc_collect()
