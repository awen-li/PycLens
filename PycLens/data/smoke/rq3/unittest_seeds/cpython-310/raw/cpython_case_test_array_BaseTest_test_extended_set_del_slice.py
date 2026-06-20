# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_extended_set_del_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    indices = (0, None, 1, 3, 19, 100, sys.maxsize, -1, -2, -31, -100)
    for start in indices:
        for stop in indices:
            for step in indices[1:]:
                a = array.array(self.typecode, self.example)
                L = list(a)
                data = L[start:stop:step]
                data.reverse()
                L[start:stop:step] = data
                a[start:stop:step] = array.array(self.typecode, data)
                self.assertEqual(a, array.array(self.typecode, L))
                del L[start:stop:step]
                del a[start:stop:step]
                self.assertEqual(a, array.array(self.typecode, L))
