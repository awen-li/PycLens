# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: MiscTests_test_type_lookup_mro_reference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyKey(object):

        def __hash__(self):
            return hash('mykey')

        def __eq__(self, other):
            X.__bases__ = (Base2,)

    class Base(object):
        mykey = 'from Base'
        mykey2 = 'from Base'

    class Base2(object):
        mykey = 'from Base2'
        mykey2 = 'from Base2'
    X = type('X', (Base,), {MyKey(): 5})
    self.assertEqual(X.mykey, 'from Base')
    self.assertEqual(X.mykey2, 'from Base2')
