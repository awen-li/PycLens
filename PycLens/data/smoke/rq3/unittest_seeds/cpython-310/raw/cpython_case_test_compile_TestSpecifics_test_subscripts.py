# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_subscripts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class str_map(object):

        def __init__(self):
            self.data = {}

        def __getitem__(self, key):
            return self.data[str(key)]

        def __setitem__(self, key, value):
            self.data[str(key)] = value

        def __delitem__(self, key):
            del self.data[str(key)]

        def __contains__(self, key):
            return str(key) in self.data
    d = str_map()
    d[1] = 1
    self.assertEqual(d[1], 1)
    d[1] += 1
    self.assertEqual(d[1], 2)
    del d[1]
    self.assertNotIn(1, d)
    d[1, 1] = 1
    self.assertEqual(d[1, 1], 1)
    d[1, 1] += 1
    self.assertEqual(d[1, 1], 2)
    del d[1, 1]
    self.assertNotIn((1, 1), d)
    d[1:2] = 1
    self.assertEqual(d[1:2], 1)
    d[1:2] += 1
    self.assertEqual(d[1:2], 2)
    del d[1:2]
    self.assertNotIn(slice(1, 2), d)
    d[1:2, 1:2] = 1
    self.assertEqual(d[1:2, 1:2], 1)
    d[1:2, 1:2] += 1
    self.assertEqual(d[1:2, 1:2], 2)
    del d[1:2, 1:2]
    self.assertNotIn((slice(1, 2), slice(1, 2)), d)
    d[1:2:3] = 1
    self.assertEqual(d[1:2:3], 1)
    d[1:2:3] += 1
    self.assertEqual(d[1:2:3], 2)
    del d[1:2:3]
    self.assertNotIn(slice(1, 2, 3), d)
    d[1:2:3, 1:2:3] = 1
    self.assertEqual(d[1:2:3, 1:2:3], 1)
    d[1:2:3, 1:2:3] += 1
    self.assertEqual(d[1:2:3, 1:2:3], 2)
    del d[1:2:3, 1:2:3]
    self.assertNotIn((slice(1, 2, 3), slice(1, 2, 3)), d)
    d[...] = 1
    self.assertEqual(d[...], 1)
    d[...] += 1
    self.assertEqual(d[...], 2)
    del d[...]
    self.assertNotIn(Ellipsis, d)
    d[..., ...] = 1
    self.assertEqual(d[..., ...], 1)
    d[..., ...] += 1
    self.assertEqual(d[..., ...], 2)
    del d[..., ...]
    self.assertNotIn((Ellipsis, Ellipsis), d)
