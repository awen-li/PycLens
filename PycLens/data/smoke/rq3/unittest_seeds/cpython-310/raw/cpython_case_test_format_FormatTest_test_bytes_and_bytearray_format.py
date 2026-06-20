# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_bytes_and_bytearray_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testcommon(b'%c', 7, b'\x07')
    testcommon(b'%c', b'Z', b'Z')
    testcommon(b'%c', bytearray(b'Z'), b'Z')
    testcommon(b'%5c', 65, b'    A')
    testcommon(b'%-5c', 65, b'A    ')

    class FakeBytes(object):

        def __bytes__(self):
            return b'123'
    fb = FakeBytes()
    testcommon(b'%b', b'abc', b'abc')
    testcommon(b'%b', bytearray(b'def'), b'def')
    testcommon(b'%b', fb, b'123')
    testcommon(b'%b', memoryview(b'abc'), b'abc')
    testcommon(b'%s', b'abc', b'abc')
    testcommon(b'%s', bytearray(b'def'), b'def')
    testcommon(b'%s', fb, b'123')
    testcommon(b'%s', memoryview(b'abc'), b'abc')
    testcommon(b'%a', 3.14, b'3.14')
    testcommon(b'%a', b'ghi', b"b'ghi'")
    testcommon(b'%a', 'jkl', b"'jkl'")
    testcommon(b'%a', 'Մ', b"'\\u0544'")
    testcommon(b'%r', 3.14, b'3.14')
    testcommon(b'%r', b'ghi', b"b'ghi'")
    testcommon(b'%r', 'jkl', b"'jkl'")
    testcommon(b'%r', 'Մ', b"'\\u0544'")
    if verbose:
        print('Testing exceptions')
    test_exc(b'%g', '1', TypeError, 'float argument required, not str')
    test_exc(b'%g', b'1', TypeError, 'float argument required, not bytes')
    test_exc(b'no format', 7, TypeError, 'not all arguments converted during bytes formatting')
    test_exc(b'no format', b'1', TypeError, 'not all arguments converted during bytes formatting')
    test_exc(b'no format', bytearray(b'1'), TypeError, 'not all arguments converted during bytes formatting')
    test_exc(b'%c', -1, OverflowError, '%c arg not in range(256)')
    test_exc(b'%c', 256, OverflowError, '%c arg not in range(256)')
    test_exc(b'%c', 2 ** 128, OverflowError, '%c arg not in range(256)')
    test_exc(b'%c', b'Za', TypeError, '%c requires an integer in range(256) or a single byte')
    test_exc(b'%c', 'Y', TypeError, '%c requires an integer in range(256) or a single byte')
    test_exc(b'%c', 3.14, TypeError, '%c requires an integer in range(256) or a single byte')
    test_exc(b'%b', 'Xc', TypeError, "%b requires a bytes-like object, or an object that implements __bytes__, not 'str'")
    test_exc(b'%s', 'Wd', TypeError, "%b requires a bytes-like object, or an object that implements __bytes__, not 'str'")
    if maxsize == 2 ** 31 - 1:
        try:
            '%*d' % (maxsize, -127)
        except MemoryError:
            pass
        else:
            raise TestFailed('"%*d"%(maxsize, -127) should fail')
