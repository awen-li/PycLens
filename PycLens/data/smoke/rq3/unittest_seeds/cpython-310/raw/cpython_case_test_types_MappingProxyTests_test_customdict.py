# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_customdict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class customdict(dict):

        def __contains__(self, key):
            if key == 'magic':
                return True
            else:
                return dict.__contains__(self, key)

        def __iter__(self):
            return iter(('iter',))

        def __len__(self):
            return 500

        def copy(self):
            return 'copy'

        def keys(self):
            return 'keys'

        def items(self):
            return 'items'

        def values(self):
            return 'values'

        def __getitem__(self, key):
            return 'getitem=%s' % dict.__getitem__(self, key)

        def get(self, key, default=None):
            return 'get=%s' % dict.get(self, key, 'default=%r' % default)
    custom = customdict({'key': 'value'})
    view = self.mappingproxy(custom)
    self.assertTrue('key' in view)
    self.assertTrue('magic' in view)
    self.assertFalse('xxx' in view)
    self.assertEqual(view['key'], 'getitem=value')
    self.assertRaises(KeyError, view.__getitem__, 'xxx')
    self.assertEqual(tuple(view), ('iter',))
    self.assertEqual(len(view), 500)
    self.assertEqual(view.copy(), 'copy')
    self.assertEqual(view.get('key'), 'get=value')
    self.assertEqual(view.get('xxx'), 'get=default=None')
    self.assertEqual(view.items(), 'items')
    self.assertEqual(view.keys(), 'keys')
    self.assertEqual(view.values(), 'values')
