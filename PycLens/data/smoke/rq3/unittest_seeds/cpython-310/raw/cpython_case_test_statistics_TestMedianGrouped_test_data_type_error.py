# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedianGrouped_test_data_type_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = ['', '', '']
    self.assertRaises(TypeError, self.func, data)
    data = [b'', b'', b'']
    self.assertRaises(TypeError, self.func, data)
    data = [1, 2, 3]
    interval = ''
    self.assertRaises(TypeError, self.func, data, interval)
    data = [1, 2, 3]
    interval = b''
    self.assertRaises(TypeError, self.func, data, interval)
