# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlopenNetworkTests_test_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.urlopen(self.url) as open_url:
        info_obj = open_url.info()
        self.assertIsInstance(info_obj, email.message.Message, "object returned by 'info' is not an instance of email.message.Message")
        self.assertEqual(info_obj.get_content_subtype(), 'html')
