# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_frame_tstate_tracing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def noop_trace(frame, event, arg):
        return noop_trace

    def generator():
        while 1:
            yield 'generator'

    def callback():
        if callback.gen is None:
            callback.gen = generator()
        return next(callback.gen)
    callback.gen = None
    old_trace = sys.gettrace()
    sys.settrace(noop_trace)
    try:
        threading.settrace(noop_trace)
        import _testcapi
        _testcapi.call_in_temporary_c_thread(callback)
        for test in range(3):
            callback()
    finally:
        sys.settrace(old_trace)
