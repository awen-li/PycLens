# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_writelines_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.BytesIO(), encoding='utf-8')
    self.assertRaises(TypeError, txt.writelines, [1, 2, 3])
    self.assertRaises(TypeError, txt.writelines, None)
    self.assertRaises(TypeError, txt.writelines, b'abc')
