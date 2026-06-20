# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_dict_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(dict):

        def __init__(self, d=None):
            if not d:
                d = {}
            self._keys = list(d.keys())
            super().__init__(d)

        def __setitem__(self, key, item):
            super().__setitem__(key, item)
            if key not in self._keys:
                self._keys.append(key)
    x = C(d={'foo': 0})
    y = copy.deepcopy(x)
    self.assertEqual(x, y)
    self.assertEqual(x._keys, y._keys)
    self.assertIsNot(x, y)
    x['bar'] = 1
    self.assertNotEqual(x, y)
    self.assertNotEqual(x._keys, y._keys)
