# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_rawio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO([b'abc', b'def', b'ghi\njkl\nopq\n'])
    txt = self.TextIOWrapper(raw, encoding='ascii', newline='\n')
    self.assertEqual(txt.read(4), 'abcd')
    self.assertEqual(txt.readline(), 'efghi\n')
    self.assertEqual(list(txt), ['jkl\n', 'opq\n'])
