# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_gettrace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def noop_trace(frame, event, arg):
        return noop_trace
    old_trace = threading.gettrace()
    try:
        threading.settrace(noop_trace)
        trace_func = threading.gettrace()
        self.assertEqual(noop_trace, trace_func)
    finally:
        threading.settrace(old_trace)
