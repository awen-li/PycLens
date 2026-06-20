# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = TestNT(x=10, y=20, z=30)
    for module in (pickle,):
        loads = getattr(module, 'loads')
        dumps = getattr(module, 'dumps')
        for protocol in range(-1, module.HIGHEST_PROTOCOL + 1):
            q = loads(dumps(p, protocol))
            self.assertEqual(p, q)
            self.assertEqual(p._fields, q._fields)
            self.assertNotIn(b'OrderedDict', dumps(p, protocol))
