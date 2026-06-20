# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: RaisingTraceFuncTestCase_test_line_event_raises_before_opcode_event

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exception = ValueError('BOOM!')

    def trace(frame, event, arg):
        if event == 'line':
            raise exception
        frame.f_trace_opcodes = True
        return trace

    def f():
        pass
    with self.assertRaises(ValueError) as caught:
        sys.settrace(trace)
        f()
    self.assertIs(caught.exception, exception)
