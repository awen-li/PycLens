# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlopenNetworkTests_test_getcode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    URL = self.url + 'XXXinvalidXXX'
    with socket_helper.transient_internet(URL):
        with self.assertWarns(DeprecationWarning):
            open_url = urllib.request.FancyURLopener().open(URL)
        try:
            code = open_url.getcode()
        finally:
            open_url.close()
        self.assertEqual(code, 404)
