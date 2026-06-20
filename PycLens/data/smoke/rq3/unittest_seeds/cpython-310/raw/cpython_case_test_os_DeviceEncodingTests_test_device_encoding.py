# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: DeviceEncodingTests_test_device_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoding = os.device_encoding(0)
    self.assertIsNotNone(encoding)
    self.assertTrue(codecs.lookup(encoding))
