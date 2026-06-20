# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frame.py
# case: ClearTest_test_lineno_with_tracing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def record_line():
        f = sys._getframe(1)
        lines.append(f.f_lineno - f.f_code.co_firstlineno)

    def test(trace):
        record_line()
        if trace:
            sys._getframe(0).f_trace = True
        record_line()
        record_line()
    expected_lines = [1, 4, 5]
    lines = []
    test(False)
    self.assertEqual(lines, expected_lines)
    lines = []
    test(True)
    self.assertEqual(lines, expected_lines)
