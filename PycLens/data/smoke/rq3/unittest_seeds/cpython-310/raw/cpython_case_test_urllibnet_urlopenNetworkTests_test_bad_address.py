# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlopenNetworkTests_test_bad_address

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bogus_domain = 'sadflkjsasf.i.nvali.d.'
    try:
        socket.gethostbyname(bogus_domain)
    except OSError:
        pass
    else:
        self.skipTest('%r should not resolve for test to work' % bogus_domain)
    failure_explanation = 'opening an invalid URL did not raise OSError; can be caused by a broken DNS server (e.g. returns 404 or hijacks page)'
    with self.assertRaises(OSError, msg=failure_explanation):
        urllib.request.urlopen('http://{}/'.format(bogus_domain))
