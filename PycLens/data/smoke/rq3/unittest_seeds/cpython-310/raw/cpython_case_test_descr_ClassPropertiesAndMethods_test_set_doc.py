# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_set_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:
        """elephant"""
    X.__doc__ = 'banana'
    self.assertEqual(X.__doc__, 'banana')
    with self.assertRaises(TypeError) as cm:
        type(list).__dict__['__doc__'].__set__(list, 'blah')
    self.assertIn("cannot set '__doc__' attribute of immutable type 'list'", str(cm.exception))
    with self.assertRaises(TypeError) as cm:
        type(X).__dict__['__doc__'].__delete__(X)
    self.assertIn("cannot delete '__doc__' attribute of immutable type 'X'", str(cm.exception))
    self.assertEqual(X.__doc__, 'banana')
