# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestMROEntry_test_mro_entry_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C_too_many:

        def __mro_entries__(self, bases, something, other):
            return ()
    c = C_too_many()
    with self.assertRaises(TypeError):

        class D(c):
            ...

    class C_too_few:

        def __mro_entries__(self):
            return ()
    d = C_too_few()
    with self.assertRaises(TypeError):

        class D(d):
            ...
