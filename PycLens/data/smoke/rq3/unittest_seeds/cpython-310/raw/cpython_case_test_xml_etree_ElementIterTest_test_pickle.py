# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementIterTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ET.Element('a')
    it = a.iter()
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.assertRaises((TypeError, pickle.PicklingError)):
            pickle.dumps(it, proto)
