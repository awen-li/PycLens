# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestMROEntry_test_mro_entry_metaclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    meta_args = []

    class Meta(type):

        def __new__(mcls, name, bases, ns):
            meta_args.extend([mcls, name, bases, ns])
            return super().__new__(mcls, name, bases, ns)

    class A:
        ...

    class C:

        def __mro_entries__(self, bases):
            return (A,)
    c = C()

    class D(c, metaclass=Meta):
        x = 1
    self.assertEqual(meta_args[0], Meta)
    self.assertEqual(meta_args[1], 'D')
    self.assertEqual(meta_args[2], (A,))
    self.assertEqual(meta_args[3]['x'], 1)
    self.assertEqual(D.__bases__, (A,))
    self.assertEqual(D.__orig_bases__, (c,))
    self.assertEqual(D.__mro__, (D, A, object))
    self.assertEqual(D.__class__, Meta)
