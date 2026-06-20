# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_itemgetter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    a = 'ABCDE'
    f = operator.itemgetter(2)
    self.assertEqual(f(a), 'C')
    self.assertRaises(TypeError, f)
    self.assertRaises(TypeError, f, a, 3)
    self.assertRaises(TypeError, f, a, size=3)
    f = operator.itemgetter(10)
    self.assertRaises(IndexError, f, a)

    class C(object):

        def __getitem__(self, name):
            raise SyntaxError
    self.assertRaises(SyntaxError, operator.itemgetter(42), C())
    f = operator.itemgetter('name')
    self.assertRaises(TypeError, f, a)
    self.assertRaises(TypeError, operator.itemgetter)
    d = dict(key='val')
    f = operator.itemgetter('key')
    self.assertEqual(f(d), 'val')
    f = operator.itemgetter('nonkey')
    self.assertRaises(KeyError, f, d)
    inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
    getcount = operator.itemgetter(1)
    self.assertEqual(list(map(getcount, inventory)), [3, 2, 5, 1])
    self.assertEqual(sorted(inventory, key=getcount), [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)])
    data = list(map(str, range(20)))
    self.assertEqual(operator.itemgetter(2, 10, 5)(data), ('2', '10', '5'))
    self.assertRaises(TypeError, operator.itemgetter(2, 'x', 5), data)
    t = tuple('abcde')
    self.assertEqual(operator.itemgetter(-1)(t), 'e')
    self.assertEqual(operator.itemgetter(slice(2, 4))(t), ('c', 'd'))

    class T(tuple):
        """Tuple subclass"""
        pass
    self.assertEqual(operator.itemgetter(0)(T('abc')), 'a')
    self.assertEqual(operator.itemgetter(0)(['a', 'b', 'c']), 'a')
    self.assertEqual(operator.itemgetter(0)(range(100, 200)), 100)
