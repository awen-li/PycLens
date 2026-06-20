# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class anon_mmap(mmap.mmap):

        def __new__(klass, *args, **kwargs):
            return mmap.mmap.__new__(klass, -1, *args, **kwargs)
    anon_mmap(PAGESIZE)
