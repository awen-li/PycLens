# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_str_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testformat('%r', '\u0378', "'\\u0378'")
    testformat('%a', '\u0378', "'\\u0378'")
    testformat('%r', 'ʹ', "'ʹ'")
    testformat('%a', 'ʹ', "'\\u0374'")
    if verbose:
        print('Testing exceptions')
    test_exc('abc %b', 1, ValueError, "unsupported format character 'b' (0x62) at index 5")
    test_exc('%g', '1', TypeError, 'must be real number, not str')
    test_exc('no format', '1', TypeError, 'not all arguments converted during string formatting')
    test_exc('%c', -1, OverflowError, '%c arg not in range(0x110000)')
    test_exc('%c', sys.maxunicode + 1, OverflowError, '%c arg not in range(0x110000)')
    test_exc('%c', 3.14, TypeError, '%c requires int or char')
    test_exc('%c', 'ab', TypeError, '%c requires int or char')
    test_exc('%c', b'x', TypeError, '%c requires int or char')
    if maxsize == 2 ** 31 - 1:
        try:
            '%*d' % (maxsize, -127)
        except MemoryError:
            pass
        else:
            raise TestFailed('"%*d"%(maxsize, -127) should fail')
