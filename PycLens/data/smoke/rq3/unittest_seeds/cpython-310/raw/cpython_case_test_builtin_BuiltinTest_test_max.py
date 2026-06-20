# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_max

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(max('123123'), '3')
    self.assertEqual(max(1, 2, 3), 3)
    self.assertEqual(max((1, 2, 3, 1, 2, 3)), 3)
    self.assertEqual(max([1, 2, 3, 1, 2, 3]), 3)
    self.assertEqual(max(1, 2, 3.0), 3.0)
    self.assertEqual(max(1, 2.0, 3), 3)
    self.assertEqual(max(1.0, 2, 3), 3)
    with self.assertRaisesRegex(TypeError, 'max expected at least 1 argument, got 0'):
        max()
    self.assertRaises(TypeError, max, 42)
    self.assertRaises(ValueError, max, ())

    class BadSeq:

        def __getitem__(self, index):
            raise ValueError
    self.assertRaises(ValueError, max, BadSeq())
    for stmt in ('max(key=int)', 'max(default=None)', 'max(1, 2, default=None)', 'max(default=None, key=int)', 'max(1, key=int)', 'max(1, 2, keystone=int)', 'max(1, 2, key=int, abc=int)', 'max(1, 2, key=1)'):
        try:
            exec(stmt, globals())
        except TypeError:
            pass
        else:
            self.fail(stmt)
    self.assertEqual(max((1,), key=neg), 1)
    self.assertEqual(max((1, 2), key=neg), 1)
    self.assertEqual(max(1, 2, key=neg), 1)
    self.assertEqual(max((), default=None), None)
    self.assertEqual(max((1,), default=None), 1)
    self.assertEqual(max((1, 2), default=None), 2)
    self.assertEqual(max((), default=1, key=neg), 1)
    self.assertEqual(max((1, 2), default=3, key=neg), 1)
    self.assertEqual(max((1, 2), key=None), 2)
    data = [random.randrange(200) for i in range(100)]
    keys = dict(((elem, random.randrange(50)) for elem in data))
    f = keys.__getitem__
    self.assertEqual(max(data, key=f), sorted(reversed(data), key=f)[-1])
