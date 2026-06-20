# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestTracebackType_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    other_tb = get_tb()
    frame = sys._getframe()
    tb = types.TracebackType(other_tb, frame, 1, 2)
    self.assertEqual(tb.tb_next, other_tb)
    self.assertEqual(tb.tb_frame, frame)
    self.assertEqual(tb.tb_lasti, 1)
    self.assertEqual(tb.tb_lineno, 2)
    tb = types.TracebackType(None, frame, 1, 2)
    self.assertEqual(tb.tb_next, None)
    with self.assertRaises(TypeError):
        types.TracebackType('no', frame, 1, 2)
    with self.assertRaises(TypeError):
        types.TracebackType(other_tb, 'no', 1, 2)
    with self.assertRaises(TypeError):
        types.TracebackType(other_tb, frame, 'no', 2)
    with self.assertRaises(TypeError):
        types.TracebackType(other_tb, frame, 1, 'nuh-uh')
