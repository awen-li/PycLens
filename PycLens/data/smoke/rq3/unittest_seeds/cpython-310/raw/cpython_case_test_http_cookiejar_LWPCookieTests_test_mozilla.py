# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_mozilla

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    year_plus_one = time.localtime()[0] + 1
    filename = os_helper.TESTFN
    c = MozillaCookieJar(filename, policy=DefaultCookiePolicy(rfc2965=True))
    interact_2965(c, 'http://www.acme.com/', 'foo1=bar; max-age=100; Version=1')
    interact_2965(c, 'http://www.acme.com/', 'foo2=bar; port="80"; max-age=100; Discard; Version=1')
    interact_2965(c, 'http://www.acme.com/', 'foo3=bar; secure; Version=1')
    expires = 'expires=09-Nov-%d 23:12:40 GMT' % (year_plus_one,)
    interact_netscape(c, 'http://www.foo.com/', 'fooa=bar; %s' % expires)
    interact_netscape(c, 'http://www.foo.com/', 'foob=bar; Domain=.foo.com; %s' % expires)
    interact_netscape(c, 'http://www.foo.com/', 'fooc=bar; Domain=www.foo.com; %s' % expires)
    for cookie in c:
        if cookie.name == 'foo1':
            cookie.set_nonstandard_attr('HTTPOnly', '')

    def save_and_restore(cj, ignore_discard):
        try:
            cj.save(ignore_discard=ignore_discard)
            new_c = MozillaCookieJar(filename, DefaultCookiePolicy(rfc2965=True))
            new_c.load(ignore_discard=ignore_discard)
        finally:
            try:
                os.unlink(filename)
            except OSError:
                pass
        return new_c
    new_c = save_and_restore(c, True)
    self.assertEqual(len(new_c), 6)
    self.assertIn("name='foo1', value='bar'", repr(new_c))
    self.assertIn("rest={'HTTPOnly': ''}", repr(new_c))
    new_c = save_and_restore(c, False)
    self.assertEqual(len(new_c), 4)
    self.assertIn("name='foo1', value='bar'", repr(new_c))
