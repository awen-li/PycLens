# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_list_resize_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lst = [0] * 65
    del lst[1:]
    self.assertEqual(len(lst), 1)
    size = (2 ** (tuple.__itemsize__ * 8) - 1) // 2
    with self.assertRaises((MemoryError, OverflowError)):
        lst * size
    with self.assertRaises((MemoryError, OverflowError)):
        lst *= size
