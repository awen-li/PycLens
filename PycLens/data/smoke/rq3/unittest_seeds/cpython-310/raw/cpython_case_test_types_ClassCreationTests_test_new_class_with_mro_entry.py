# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_new_class_with_mro_entry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        pass

    class C:

        def __mro_entries__(self, bases):
            return (A,)
    c = C()
    D = types.new_class('D', (c,), {})
    self.assertEqual(D.__bases__, (A,))
    self.assertEqual(D.__orig_bases__, (c,))
    self.assertEqual(D.__mro__, (D, A, object))
