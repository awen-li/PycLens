# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_setdefault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    self.assertIs(d.setdefault('key0'), None)
    d.setdefault('key0', [])
    self.assertIs(d.setdefault('key0'), None)
    d.setdefault('key', []).append(3)
    self.assertEqual(d['key'][0], 3)
    d.setdefault('key', []).append(4)
    self.assertEqual(len(d['key']), 2)
    self.assertRaises(TypeError, d.setdefault)

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
    self.assertRaises(Exc, d.setdefault, x, [])
