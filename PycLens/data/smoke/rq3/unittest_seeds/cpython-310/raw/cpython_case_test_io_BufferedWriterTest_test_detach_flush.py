# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_detach_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO()
    buf = self.tp(raw)
    buf.write(b'howdy!')
    self.assertFalse(raw._write_stack)
    buf.detach()
    self.assertEqual(raw._write_stack, [b'howdy!'])
