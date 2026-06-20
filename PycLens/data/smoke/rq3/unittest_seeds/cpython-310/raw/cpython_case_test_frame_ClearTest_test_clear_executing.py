# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frame.py
# case: ClearTest_test_clear_executing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        1 / 0
    except ZeroDivisionError as e:
        f = e.__traceback__.tb_frame
    with self.assertRaises(RuntimeError):
        f.clear()
    with self.assertRaises(RuntimeError):
        f.f_back.clear()
