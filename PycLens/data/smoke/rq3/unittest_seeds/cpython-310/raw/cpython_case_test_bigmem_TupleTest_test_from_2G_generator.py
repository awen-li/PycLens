# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: TupleTest_test_from_2G_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        t = tuple(iter([42] * size))
    except MemoryError:
        pass
    else:
        self.assertEqual(len(t), size)
        self.assertEqual(t[:10], (42,) * 10)
        self.assertEqual(t[-10:], (42,) * 10)
