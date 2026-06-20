# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'a': 1, 'b': 2}
    self.assertEqual(d['a'], 1)
    self.assertEqual(d['b'], 2)
    d['c'] = 3
    d['a'] = 4
    self.assertEqual(d['c'], 3)
    self.assertEqual(d['a'], 4)
    del d['b']
    self.assertEqual(d, {'a': 4, 'c': 3})
    self.assertRaises(TypeError, d.__getitem__)

    class BadEq(object):

        def __eq__(self, other):
            raise Exc()

        def __hash__(self):
            return 24
    d = {}
    d[BadEq()] = 42
    self.assertRaises(KeyError, d.__getitem__, 23)

    class Exc(Exception):
        pass

    class BadHash(object):
        fail = False

        def __hash__(self):
            if self.fail:
                raise Exc()
            else:
                return 42
    x = BadHash()
    d[x] = 42
    x.fail = True
    self.assertRaises(Exc, d.__getitem__, x)
