# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_extended_getslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    indices = (0, None, 1, 3, 19, 100, sys.maxsize, -1, -2, -31, -100)
    for start in indices:
        for stop in indices:
            for step in indices[1:]:
                self.assertEqual(list(a[start:stop:step]), list(a)[start:stop:step])
