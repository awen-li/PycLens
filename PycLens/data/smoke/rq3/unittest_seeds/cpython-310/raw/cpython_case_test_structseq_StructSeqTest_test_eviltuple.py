# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_structseq.py
# case: StructSeqTest_test_eviltuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Exc(Exception):
        pass

    class C:

        def __getitem__(self, i):
            raise Exc

        def __len__(self):
            return 9
    self.assertRaises(Exc, time.struct_time, C())
