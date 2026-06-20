# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestMROEntry_test_mro_entry_errors_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C_not_callable:
        __mro_entries__ = 'Surprise!'
    c = C_not_callable()
    with self.assertRaises(TypeError):

        class D(c):
            ...

    class C_not_tuple:

        def __mro_entries__(self):
            return object
    c = C_not_tuple()
    with self.assertRaises(TypeError):

        class D(c):
            ...
