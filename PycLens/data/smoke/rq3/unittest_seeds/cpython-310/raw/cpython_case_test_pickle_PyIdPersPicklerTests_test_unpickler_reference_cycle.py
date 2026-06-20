# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: PyIdPersPicklerTests_test_unpickler_reference_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(Unpickler):
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            unpickler = Unpickler(io.BytesIO(self.dumps('abc', proto)))
            self.assertEqual(unpickler.load(), 'abc')
        unpickler = Unpickler(io.BytesIO())
        self.assertEqual(unpickler.persistent_load('def'), 'def')
        r = weakref.ref(unpickler)
        del unpickler
        self.assertIsNone(r())

    class PersUnpickler(self.unpickler):

        def persistent_load(subself, pid):
            return pid
    check(PersUnpickler)

    class PersUnpickler(self.unpickler):

        @classmethod
        def persistent_load(cls, pid):
            return pid
    check(PersUnpickler)

    class PersUnpickler(self.unpickler):

        @staticmethod
        def persistent_load(pid):
            return pid
    check(PersUnpickler)
