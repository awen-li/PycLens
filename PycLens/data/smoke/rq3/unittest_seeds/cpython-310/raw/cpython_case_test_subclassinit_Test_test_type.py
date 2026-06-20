# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = type('NewClass', (object,), {})
    self.assertIsInstance(t, type)
    self.assertEqual(t.__name__, 'NewClass')
    with self.assertRaises(TypeError):
        type(name='NewClass', bases=(object,), dict={})
