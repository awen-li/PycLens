# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mm = mmap.mmap(-1, 16)
    wr = weakref.ref(mm)
    self.assertIs(wr(), mm)
    del mm
    gc_collect()
    self.assertIs(wr(), None)
