# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class dictmissing(dict):

        def __missing__(self, key):
            return 'missing=%s' % key
    view = self.mappingproxy(dictmissing(x=1))
    self.assertEqual(view['x'], 1)
    self.assertEqual(view['y'], 'missing=y')
    self.assertEqual(view.get('x'), 1)
    self.assertEqual(view.get('y'), None)
    self.assertEqual(view.get('y', 42), 42)
    self.assertTrue('x' in view)
    self.assertFalse('y' in view)
