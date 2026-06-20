# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: DictProxyTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = repr(self.C.__dict__)
    self.assertTrue(r.startswith('mappingproxy('), r)
    self.assertTrue(r.endswith(')'), r)
    for (k, v) in self.C.__dict__.items():
        self.assertIn('{!r}: {!r}'.format(k, v), r)
