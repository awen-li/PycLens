# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_views_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mappingproxy = type(type.__dict__)

    class Dict(dict):
        pass
    for cls in [dict, Dict]:
        d = cls()
        m1 = d.keys().mapping
        m2 = d.values().mapping
        m3 = d.items().mapping
        for m in [m1, m2, m3]:
            self.assertIsInstance(m, mappingproxy)
            self.assertEqual(m, d)
        d['foo'] = 'bar'
        for m in [m1, m2, m3]:
            self.assertIsInstance(m, mappingproxy)
            self.assertEqual(m, d)
