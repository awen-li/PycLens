# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_merge_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    a = OrderedDict({0: 0, 1: 1, 2: 1})
    b = OrderedDict({1: 1, 2: 2, 3: 3})
    c = a.copy()
    d = a.copy()
    c |= b
    d |= list(b.items())
    expected = OrderedDict({0: 0, 1: 1, 2: 2, 3: 3})
    self.assertEqual(a | dict(b), expected)
    self.assertEqual(a | b, expected)
    self.assertEqual(c, expected)
    self.assertEqual(d, expected)
    c = b.copy()
    c |= a
    expected = OrderedDict({1: 1, 2: 1, 3: 3, 0: 0})
    self.assertEqual(dict(b) | a, expected)
    self.assertEqual(b | a, expected)
    self.assertEqual(c, expected)
    self.assertIs(type(a | b), OrderedDict)
    self.assertIs(type(dict(a) | b), OrderedDict)
    self.assertIs(type(a | dict(b)), OrderedDict)
    expected = a.copy()
    a |= ()
    a |= ''
    self.assertEqual(a, expected)
    with self.assertRaises(TypeError):
        a | None
    with self.assertRaises(TypeError):
        a | ()
    with self.assertRaises(TypeError):
        a | 'BAD'
    with self.assertRaises(TypeError):
        a | ''
    with self.assertRaises(ValueError):
        a |= 'BAD'
