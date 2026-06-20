# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: MiscTracebackCases_test_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def outer():
        middle()

    def middle():
        inner()

    def inner():
        i = 1
        1 / 0
    try:
        outer()
    except:
        (type_, value, tb) = sys.exc_info()
    inner_frame = tb.tb_next.tb_next.tb_next.tb_frame
    self.assertEqual(len(inner_frame.f_locals), 1)
    traceback.clear_frames(tb)
    self.assertEqual(len(inner_frame.f_locals), 0)
