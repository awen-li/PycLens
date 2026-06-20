# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestTracebackType_test_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        self.raiser()
    except Exception as exc:
        tb = exc.__traceback__
    self.assertIsInstance(tb.tb_next, types.TracebackType)
    self.assertIs(tb.tb_frame, sys._getframe())
    self.assertIsInstance(tb.tb_lasti, int)
    self.assertIsInstance(tb.tb_lineno, int)
    self.assertIs(tb.tb_next.tb_next, None)
    with self.assertRaises(TypeError):
        del tb.tb_next
    with self.assertRaises(TypeError):
        tb.tb_next = 'asdf'
    with self.assertRaises(ValueError):
        tb.tb_next = tb
    with self.assertRaises(ValueError):
        tb.tb_next.tb_next = tb
    tb.tb_next = None
    self.assertIs(tb.tb_next, None)
    new_tb = get_tb()
    tb.tb_next = new_tb
    self.assertIs(tb.tb_next, new_tb)
