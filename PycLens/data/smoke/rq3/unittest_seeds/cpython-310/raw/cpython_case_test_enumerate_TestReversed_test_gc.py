# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: TestReversed_test_gc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Seq:

        def __len__(self):
            return 10

        def __getitem__(self, index):
            return index
    s = Seq()
    r = reversed(s)
    s.r = r
