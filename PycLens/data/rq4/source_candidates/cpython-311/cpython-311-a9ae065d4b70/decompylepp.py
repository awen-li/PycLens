# Source Generated with Decompyle++
# File: cpython-311-a9ae065d4b70.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [
        'Thu, 03 Feb 1994 00:00:00 GMT',
        'Thursday, 03-Feb-94 00:00:00 GMT',
        'Thursday, 03-Feb-1994 00:00:00 GMT',
        '03 Feb 1994 00:00:00 GMT',
        '03-Feb-94 00:00:00 GMT',
        '03-Feb-1994 00:00:00 GMT',
        '03-Feb-1994 00:00 GMT',
        '03-Feb-1994 00:00',
        '02-Feb-1994 24:00',
        '03-Feb-94',
        '03-Feb-1994',
        '03 Feb 1994',
        '  03   Feb   1994  0:00  ',
        '  03-Feb-1994  ']
    test_t = 760233600
    result = time2isoz(test_t)
    expected = '1994-02-03 00:00:00Z'
    self.assertEqual(result, expected, f'''{test_t!s}  =>  \'{result!s}\' ({expected!s})''')
    for s in tests:
        self.assertEqual(http2time(s), test_t, s)
        self.assertEqual(http2time(s.lower()), test_t, s.lower())
        self.assertEqual(http2time(s.upper()), test_t, s.upper())

if __name__ == '__main__':
    f'''{__pybcsec_seed__}'''
    return None
