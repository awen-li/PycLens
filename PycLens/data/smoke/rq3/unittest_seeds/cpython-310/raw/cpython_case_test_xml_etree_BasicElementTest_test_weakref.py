# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BasicElementTest_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    flag = False

    def wref_cb(w):
        nonlocal flag
        flag = True
    e = ET.Element('e')
    wref = weakref.ref(e, wref_cb)
    self.assertEqual(wref().tag, 'e')
    del e
    gc_collect()
    self.assertEqual(flag, True)
    self.assertEqual(wref(), None)
