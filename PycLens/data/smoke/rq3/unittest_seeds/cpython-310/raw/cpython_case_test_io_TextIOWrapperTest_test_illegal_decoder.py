# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_illegal_decoder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _make_illegal_wrapper():
        quopri = codecs.lookup('quopri')
        quopri._is_text_encoding = True
        try:
            t = self.TextIOWrapper(self.BytesIO(b'aaaaaa'), newline='\n', encoding='quopri')
        finally:
            quopri._is_text_encoding = False
        return t
    t = _make_illegal_wrapper()
    self.assertRaises(TypeError, t.read, 1)
    t = _make_illegal_wrapper()
    self.assertRaises(TypeError, t.readline)
    t = _make_illegal_wrapper()
    self.assertRaises(TypeError, t.read)

    def _make_very_illegal_wrapper(getstate_ret_val):

        class BadDecoder:

            def getstate(self):
                return getstate_ret_val

        def _get_bad_decoder(dummy):
            return BadDecoder()
        quopri = codecs.lookup('quopri')
        with support.swap_attr(quopri, 'incrementaldecoder', _get_bad_decoder):
            return _make_illegal_wrapper()
    t = _make_very_illegal_wrapper(42)
    self.assertRaises(TypeError, t.read, 42)
    t = _make_very_illegal_wrapper(())
    self.assertRaises(TypeError, t.read, 42)
    t = _make_very_illegal_wrapper((1, 2))
    self.assertRaises(TypeError, t.read, 42)
