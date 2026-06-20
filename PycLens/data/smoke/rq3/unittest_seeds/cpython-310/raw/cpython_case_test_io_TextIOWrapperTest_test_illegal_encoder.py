# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_illegal_encoder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rot13 = codecs.lookup('rot13')
    with support.swap_attr(rot13, '_is_text_encoding', True):
        t = io.TextIOWrapper(io.BytesIO(b'foo'), encoding='rot13')
    self.assertRaises(TypeError, t.write, 'bar')
