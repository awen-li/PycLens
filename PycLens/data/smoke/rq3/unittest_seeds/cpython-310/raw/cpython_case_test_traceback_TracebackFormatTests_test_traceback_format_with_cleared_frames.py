# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackFormatTests_test_traceback_format_with_cleared_frames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cleanup_tb(tb):
        tb.tb_frame.clear()
    self.check_traceback_format(cleanup_tb)
