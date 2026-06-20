# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_format_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(''.format_map({}), '')
    self.assertEqual('a'.format_map({}), 'a')
    self.assertEqual('ab'.format_map({}), 'ab')
    self.assertEqual('a{{'.format_map({}), 'a{')
    self.assertEqual('a}}'.format_map({}), 'a}')
    self.assertEqual('{{b'.format_map({}), '{b')
    self.assertEqual('}}b'.format_map({}), '}b')
    self.assertEqual('a{{b'.format_map({}), 'a{b')

    class Mapping(dict):

        def __missing__(self, key):
            return key
    self.assertEqual('{hello}'.format_map(Mapping()), 'hello')
    self.assertEqual('{a} {world}'.format_map(Mapping(a='hello')), 'hello world')

    class InternalMapping:

        def __init__(self):
            self.mapping = {'a': 'hello'}

        def __getitem__(self, key):
            return self.mapping[key]
    self.assertEqual('{a}'.format_map(InternalMapping()), 'hello')

    class C:

        def __init__(self, x=100):
            self._x = x

        def __format__(self, spec):
            return spec
    self.assertEqual('{foo._x}'.format_map({'foo': C(20)}), '20')
    self.assertRaises(TypeError, ''.format_map)
    self.assertRaises(TypeError, 'a'.format_map)
    self.assertRaises(ValueError, '{'.format_map, {})
    self.assertRaises(ValueError, '}'.format_map, {})
    self.assertRaises(ValueError, 'a{'.format_map, {})
    self.assertRaises(ValueError, 'a}'.format_map, {})
    self.assertRaises(ValueError, '{a'.format_map, {})
    self.assertRaises(ValueError, '}a'.format_map, {})
    self.assertRaises(ValueError, '{}'.format_map, {'a': 2})
    self.assertRaises(ValueError, '{}'.format_map, 'a')
    self.assertRaises(ValueError, '{a} {}'.format_map, {'a': 2, 'b': 1})

    class BadMapping:

        def __getitem__(self, key):
            return 1 / 0
    self.assertRaises(KeyError, '{a}'.format_map, {})
    self.assertRaises(TypeError, '{a}'.format_map, [])
    self.assertRaises(ZeroDivisionError, '{a}'.format_map, BadMapping())
