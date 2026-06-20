# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_readlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.BytesIO(b'AA\nBB\nCC'), encoding='utf-8')
    self.assertEqual(txt.readlines(), ['AA\n', 'BB\n', 'CC'])
    txt.seek(0)
    self.assertEqual(txt.readlines(None), ['AA\n', 'BB\n', 'CC'])
    txt.seek(0)
    self.assertEqual(txt.readlines(5), ['AA\n', 'BB\n'])
