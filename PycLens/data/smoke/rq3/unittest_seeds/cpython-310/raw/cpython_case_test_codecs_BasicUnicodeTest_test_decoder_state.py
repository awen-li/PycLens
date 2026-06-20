# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: BasicUnicodeTest_test_decoder_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = 'abc123'
    for encoding in all_unicode_encodings:
        if encoding not in broken_unicode_with_stateful:
            self.check_state_handling_decode(encoding, u, u.encode(encoding))
            self.check_state_handling_encode(encoding, u, u.encode(encoding))
