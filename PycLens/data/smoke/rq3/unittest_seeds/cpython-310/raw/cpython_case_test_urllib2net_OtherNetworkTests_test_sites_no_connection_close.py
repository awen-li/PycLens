# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: OtherNetworkTests_test_sites_no_connection_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    URL = 'http://www.imdb.com'
    with socket_helper.transient_internet(URL):
        try:
            with urllib.request.urlopen(URL) as res:
                pass
        except ValueError:
            self.fail('urlopen failed for site not sending                            Connection:close')
        else:
            self.assertTrue(res)
        req = urllib.request.urlopen(URL)
        res = req.read()
        self.assertTrue(res)
