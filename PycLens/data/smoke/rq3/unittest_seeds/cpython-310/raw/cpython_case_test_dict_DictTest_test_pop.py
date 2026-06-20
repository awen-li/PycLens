# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    (k, v) = ('abc', 'def')
    d[k] = v
    self.assertRaises(KeyError, d.pop, 'ghi')
    self.assertEqual(d.pop(k), v)
    self.assertEqual(len(d), 0)
    self.assertRaises(KeyError, d.pop, k)
    self.assertEqual(d.pop(k, v), v)
    d[k] = v
    self.assertEqual(d.pop(k, 1), v)
    self.assertRaises(TypeError, d.pop)

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
    self.assertRaises(Exc, d.pop, x)
