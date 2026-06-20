# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_environb

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    value = 'euro€'
    try:
        value_bytes = value.encode(sys.getfilesystemencoding(), 'surrogateescape')
    except UnicodeEncodeError:
        msg = 'U+20AC character is not encodable to %s' % (sys.getfilesystemencoding(),)
        self.skipTest(msg)
    os.environ['unicode'] = value
    self.assertEqual(os.environ['unicode'], value)
    self.assertEqual(os.environb[b'unicode'], value_bytes)
    value = b'\xff'
    os.environb[b'bytes'] = value
    self.assertEqual(os.environb[b'bytes'], value)
    value_str = value.decode(sys.getfilesystemencoding(), 'surrogateescape')
    self.assertEqual(os.environ['bytes'], value_str)
