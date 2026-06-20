# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_min

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(min('123123'), '1')
    self.assertEqual(min(1, 2, 3), 1)
    self.assertEqual(min((1, 2, 3, 1, 2, 3)), 1)
    self.assertEqual(min([1, 2, 3, 1, 2, 3]), 1)
    self.assertEqual(min(1, 2, 3.0), 1)
    self.assertEqual(min(1, 2.0, 3), 1)
    self.assertEqual(min(1.0, 2, 3), 1.0)
    with self.assertRaisesRegex(TypeError, 'min expected at least 1 argument, got 0'):
        min()
    self.assertRaises(TypeError, min, 42)
    self.assertRaises(ValueError, min, ())

    class BadSeq:

        def __getitem__(self, index):
            raise ValueError
    self.assertRaises(ValueError, min, BadSeq())
    for stmt in ('min(key=int)', 'min(default=None)', 'min(1, 2, default=None)', 'min(default=None, key=int)', 'min(1, key=int)', 'min(1, 2, keystone=int)', 'min(1, 2, key=int, abc=int)', 'min(1, 2, key=1)'):
        try:
            exec(stmt, globals())
        except TypeError:
            pass
        else:
            self.fail(stmt)
    self.assertEqual(min((1,), key=neg), 1)
    self.assertEqual(min((1, 2), key=neg), 2)
    self.assertEqual(min(1, 2, key=neg), 2)
    self.assertEqual(min((), default=None), None)
    self.assertEqual(min((1,), default=None), 1)
    self.assertEqual(min((1, 2), default=None), 1)
    self.assertEqual(min((), default=1, key=neg), 1)
    self.assertEqual(min((1, 2), default=1, key=neg), 2)
    self.assertEqual(min((1, 2), key=None), 1)
    data = [random.randrange(200) for i in range(100)]
    keys = dict(((elem, random.randrange(50)) for elem in data))
    f = keys.__getitem__
    self.assertEqual(min(data, key=f), sorted(data, key=f)[0])
