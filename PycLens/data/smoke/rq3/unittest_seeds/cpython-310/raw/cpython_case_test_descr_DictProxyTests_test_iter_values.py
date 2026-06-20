# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: DictProxyTests_test_iter_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = self.C.__dict__.values()
    self.assertNotIsInstance(it, list)
    values = list(it)
    self.assertEqual(len(values), 5)
