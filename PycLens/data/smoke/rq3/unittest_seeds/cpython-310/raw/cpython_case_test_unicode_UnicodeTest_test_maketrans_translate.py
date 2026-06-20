# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_maketrans_translate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkequalnofix('bbbc', 'abababc', 'translate', {ord('a'): None})
    self.checkequalnofix('iiic', 'abababc', 'translate', {ord('a'): None, ord('b'): ord('i')})
    self.checkequalnofix('iiix', 'abababc', 'translate', {ord('a'): None, ord('b'): ord('i'), ord('c'): 'x'})
    self.checkequalnofix('c', 'abababc', 'translate', {ord('a'): None, ord('b'): ''})
    self.checkequalnofix('xyyx', 'xzx', 'translate', {ord('z'): 'yy'})
    self.checkequalnofix('abababc', 'abababc', 'translate', {'b': '<i>'})
    tbl = self.type2test.maketrans({'a': None, 'b': '<i>'})
    self.checkequalnofix('<i><i><i>c', 'abababc', 'translate', tbl)
    tbl = self.type2test.maketrans('abc', 'xyz', 'd')
    self.checkequalnofix('xyzzy', 'abdcdcbdddd', 'translate', tbl)
    self.assertEqual('[a]'.translate(str.maketrans('a', 'X')), '[X]')
    self.assertEqual('[a]'.translate(str.maketrans({'a': 'X'})), '[X]')
    self.assertEqual('[a]'.translate(str.maketrans({'a': None})), '[]')
    self.assertEqual('[a]'.translate(str.maketrans({'a': 'XXX'})), '[XXX]')
    self.assertEqual('[a]'.translate(str.maketrans({'a': 'é'})), '[é]')
    self.assertEqual('axb'.translate(str.maketrans({'a': None, 'b': '123'})), 'x123')
    self.assertEqual('axb'.translate(str.maketrans({'a': None, 'b': 'é'})), 'xé')
    self.assertEqual('[a]'.translate(str.maketrans({'a': '<é>'})), '[<é>]')
    self.assertEqual('[é]'.translate(str.maketrans({'é': 'a'})), '[a]')
    self.assertEqual('[é]'.translate(str.maketrans({'é': None})), '[]')
    self.assertEqual('[é]'.translate(str.maketrans({'é': '123'})), '[123]')
    self.assertEqual('[aé]'.translate(str.maketrans({'a': '<€>'})), '[<€>é]')
    invalid_char = 1114111 + 1
    for before in 'aé€\U0010ffff':
        mapping = str.maketrans({before: invalid_char})
        text = '[%s]' % before
        self.assertRaises(ValueError, text.translate, mapping)
    self.assertRaises(TypeError, self.type2test.maketrans)
    self.assertRaises(ValueError, self.type2test.maketrans, 'abc', 'defg')
    self.assertRaises(TypeError, self.type2test.maketrans, 2, 'def')
    self.assertRaises(TypeError, self.type2test.maketrans, 'abc', 2)
    self.assertRaises(TypeError, self.type2test.maketrans, 'abc', 'def', 2)
    self.assertRaises(ValueError, self.type2test.maketrans, {'xy': 2})
    self.assertRaises(TypeError, self.type2test.maketrans, {(1,): 2})
    self.assertRaises(TypeError, 'hello'.translate)
    self.assertRaises(TypeError, 'abababc'.translate, 'abc', 'xyz')
