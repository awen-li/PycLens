# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BasicElementTest_test_cyclic_gc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Dummy:
        pass
    d = Dummy()
    d.dummyref = ET.Element('joe', attr=d)
    wref = weakref.ref(d)
    del d
    gc_collect()
    self.assertIsNone(wref())
    e = ET.Element('joe')
    d = Dummy()
    d.dummyref = e
    wref = weakref.ref(d)
    e2 = ET.SubElement(e, 'foo', attr=d)
    del d, e, e2
    gc_collect()
    self.assertIsNone(wref())
    e1 = ET.Element('e1')
    e2 = ET.Element('e2')
    e3 = ET.Element('e3')
    e3.append(e1)
    e2.append(e3)
    e1.append(e2)
    wref = weakref.ref(e1)
    del e1, e2, e3
    gc_collect()
    self.assertIsNone(wref())
