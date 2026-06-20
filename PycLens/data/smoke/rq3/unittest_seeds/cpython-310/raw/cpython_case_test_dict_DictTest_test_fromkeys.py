# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_fromkeys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(dict.fromkeys('abc'), {'a': None, 'b': None, 'c': None})
    d = {}
    self.assertIsNot(d.fromkeys('abc'), d)
    self.assertEqual(d.fromkeys('abc'), {'a': None, 'b': None, 'c': None})
    self.assertEqual(d.fromkeys((4, 5), 0), {4: 0, 5: 0})
    self.assertEqual(d.fromkeys([]), {})

    def g():
        yield 1
    self.assertEqual(d.fromkeys(g()), {1: None})
    self.assertRaises(TypeError, {}.fromkeys, 3)

    class dictlike(dict):
        pass
    self.assertEqual(dictlike.fromkeys('a'), {'a': None})
    self.assertEqual(dictlike().fromkeys('a'), {'a': None})
    self.assertIsInstance(dictlike.fromkeys('a'), dictlike)
    self.assertIsInstance(dictlike().fromkeys('a'), dictlike)

    class mydict(dict):

        def __new__(cls):
            return collections.UserDict()
    ud = mydict.fromkeys('ab')
    self.assertEqual(ud, {'a': None, 'b': None})
    self.assertIsInstance(ud, collections.UserDict)
    self.assertRaises(TypeError, dict.fromkeys)

    class Exc(Exception):
        pass

    class baddict1(dict):

        def __init__(self):
            raise Exc()
    self.assertRaises(Exc, baddict1.fromkeys, [1])

    class BadSeq(object):

        def __iter__(self):
            return self

        def __next__(self):
            raise Exc()
    self.assertRaises(Exc, dict.fromkeys, BadSeq())

    class baddict2(dict):

        def __setitem__(self, key, value):
            raise Exc()
    self.assertRaises(Exc, baddict2.fromkeys, [1])
    d = dict(zip(range(6), range(6)))
    self.assertEqual(dict.fromkeys(d, 0), dict(zip(range(6), [0] * 6)))

    class baddict3(dict):

        def __new__(cls):
            return d
    d = {i: i for i in range(10)}
    res = d.copy()
    res.update(a=None, b=None, c=None)
    self.assertEqual(baddict3.fromkeys({'a', 'b', 'c'}), res)
