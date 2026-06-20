# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_reconfigure_write_through

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO([])
    t = self.TextIOWrapper(raw, encoding='ascii', newline='\n')
    t.write('1')
    t.reconfigure(write_through=True)
    self.assertEqual(t.write_through, True)
    self.assertEqual(b''.join(raw._write_stack), b'1')
    t.write('23')
    self.assertEqual(b''.join(raw._write_stack), b'123')
    t.reconfigure(write_through=False)
    self.assertEqual(t.write_through, False)
    t.write('45')
    t.flush()
    self.assertEqual(b''.join(raw._write_stack), b'12345')
    t.reconfigure()
    t.reconfigure(write_through=None)
    self.assertEqual(t.write_through, False)
    t.reconfigure(write_through=True)
    t.reconfigure()
    t.reconfigure(write_through=None)
    self.assertEqual(t.write_through, True)
