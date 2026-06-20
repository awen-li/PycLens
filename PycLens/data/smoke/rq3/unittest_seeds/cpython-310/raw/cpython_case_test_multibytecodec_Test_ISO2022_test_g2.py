# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_ISO2022_test_g2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iso2022jp2 = b'\x1b(B:hu4:unit\x1b.A\x1bNi de famille'
    uni = ':hu4:unité de famille'
    self.assertEqual(iso2022jp2.decode('iso2022-jp-2'), uni)
