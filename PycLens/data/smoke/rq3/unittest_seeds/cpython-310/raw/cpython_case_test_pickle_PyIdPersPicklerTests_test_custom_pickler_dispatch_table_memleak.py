# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: PyIdPersPicklerTests_test_custom_pickler_dispatch_table_memleak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Pickler(self.pickler):

        def __init__(self, *args, **kwargs):
            self.dispatch_table = table
            super().__init__(*args, **kwargs)

    class DispatchTable:
        pass
    table = DispatchTable()
    pickler = Pickler(io.BytesIO())
    self.assertIs(pickler.dispatch_table, table)
    table_ref = weakref.ref(table)
    self.assertIsNotNone(table_ref())
    del pickler
    del table
    support.gc_collect()
    self.assertIsNone(table_ref())
