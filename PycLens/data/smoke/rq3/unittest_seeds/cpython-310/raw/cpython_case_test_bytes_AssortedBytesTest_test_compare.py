# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: AssortedBytesTest_test_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def bytes_warning():
        return warnings_helper.check_warnings(('', BytesWarning))
    with bytes_warning():
        b'' == ''
    with bytes_warning():
        '' == b''
    with bytes_warning():
        b'' != ''
    with bytes_warning():
        '' != b''
    with bytes_warning():
        bytearray(b'') == ''
    with bytes_warning():
        '' == bytearray(b'')
    with bytes_warning():
        bytearray(b'') != ''
    with bytes_warning():
        '' != bytearray(b'')
    with bytes_warning():
        b'\x00' == 0
    with bytes_warning():
        0 == b'\x00'
    with bytes_warning():
        b'\x00' != 0
    with bytes_warning():
        0 != b'\x00'
