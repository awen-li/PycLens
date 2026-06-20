# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: DictProxyTests_test_iter_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = self.C.__dict__.keys()
    self.assertNotIsInstance(it, list)
    keys = list(it)
    keys.sort()
    self.assertEqual(keys, ['__dict__', '__doc__', '__module__', '__weakref__', 'meth'])
