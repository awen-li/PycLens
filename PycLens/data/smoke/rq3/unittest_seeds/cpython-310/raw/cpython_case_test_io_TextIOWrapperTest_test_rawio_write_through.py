# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_rawio_write_through

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO([b'abc', b'def', b'ghi\njkl\nopq\n'])
    txt = self.TextIOWrapper(raw, encoding='ascii', newline='\n', write_through=True)
    txt.write('1')
    txt.write('23\n4')
    txt.write('5')
    self.assertEqual(b''.join(raw._write_stack), b'123\n45')
