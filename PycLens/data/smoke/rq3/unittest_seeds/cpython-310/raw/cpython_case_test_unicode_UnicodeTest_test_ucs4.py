# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_ucs4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = '\U00100000'
    y = x.encode('raw-unicode-escape').decode('raw-unicode-escape')
    self.assertEqual(x, y)
    y = b'\\U00100000'
    x = y.decode('raw-unicode-escape').encode('raw-unicode-escape')
    self.assertEqual(x, y)
    y = b'\\U00010000'
    x = y.decode('raw-unicode-escape').encode('raw-unicode-escape')
    self.assertEqual(x, y)
    try:
        b'\\U11111111'.decode('raw-unicode-escape')
    except UnicodeDecodeError as e:
        self.assertEqual(e.start, 0)
        self.assertEqual(e.end, 10)
    else:
        self.fail('Should have raised UnicodeDecodeError')
