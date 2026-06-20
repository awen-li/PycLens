# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_no_return_comment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    url = 'http://foo.bar.com/'
    interact_2965(c, url, 'spam=eggs; Version=1; Comment="does anybody read these?"; CommentURL="http://foo.bar.net/comment.html"')
    h = interact_2965(c, url)
    self.assertNotIn('Comment', h, 'Comment or CommentURL cookie-attributes returned to server')
