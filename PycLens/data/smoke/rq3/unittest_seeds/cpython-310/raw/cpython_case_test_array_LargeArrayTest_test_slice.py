# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    self.assertEqual(list(example[:4]), [0, 1, 2, 3])
    self.assertEqual(list(example[-4:]), [8, 9, 10, 11])
    part = example[1:-1]
    self.assertEqual(len(part), size + 2)
    self.assertEqual(part[0], 1)
    self.assertEqual(part[-1], 10)
    del part
    part = example[::2]
    self.assertEqual(len(part), (size + 5) // 2)
    self.assertEqual(list(part[:4]), [0, 2, 4, 6])
    if size % 2:
        self.assertEqual(list(part[-2:]), [9, 11])
    else:
        self.assertEqual(list(part[-2:]), [8, 10])
