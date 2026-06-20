# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: PyIdPersPicklerTests_test_pickler_reference_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(Pickler):
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            f = io.BytesIO()
            pickler = Pickler(f, proto)
            pickler.dump('abc')
            self.assertEqual(self.loads(f.getvalue()), 'abc')
        pickler = Pickler(io.BytesIO())
        self.assertEqual(pickler.persistent_id('def'), 'def')
        r = weakref.ref(pickler)
        del pickler
        self.assertIsNone(r())

    class PersPickler(self.pickler):

        def persistent_id(subself, obj):
            return obj
    check(PersPickler)

    class PersPickler(self.pickler):

        @classmethod
        def persistent_id(cls, obj):
            return obj
    check(PersPickler)

    class PersPickler(self.pickler):

        @staticmethod
        def persistent_id(obj):
            return obj
    check(PersPickler)
