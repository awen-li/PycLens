# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_writelines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = ['ab', 'cd', 'ef']
    buf = self.BytesIO()
    txt = self.TextIOWrapper(buf, encoding='utf-8')
    txt.writelines(l)
    txt.flush()
    self.assertEqual(buf.getvalue(), b'abcdef')
