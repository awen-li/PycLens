# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_session_cookies

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    year_plus_one = time.localtime()[0] + 1
    req = urllib.request.Request('http://www.perlmeister.com/scripts')
    headers = []
    headers.append('Set-Cookie: s1=session;Path=/scripts')
    headers.append('Set-Cookie: p1=perm; Domain=.perlmeister.com;Path=/;expires=Fri, 02-Feb-%d 23:24:20 GMT' % year_plus_one)
    headers.append('Set-Cookie: p2=perm;Path=/;expires=Fri, 02-Feb-%d 23:24:20 GMT' % year_plus_one)
    headers.append('Set-Cookie: s2=session;Path=/scripts;Domain=.perlmeister.com')
    headers.append('Set-Cookie2: s3=session;Version=1;Discard;Path="/"')
    res = FakeResponse(headers, 'http://www.perlmeister.com/scripts')
    c = CookieJar()
    c.extract_cookies(res, req)
    counter = {'session_after': 0, 'perm_after': 0, 'session_before': 0, 'perm_before': 0}
    for cookie in c:
        key = '%s_before' % cookie.value
        counter[key] = counter[key] + 1
    c.clear_session_cookies()
    for cookie in c:
        key = '%s_after' % cookie.value
        counter[key] = counter[key] + 1
    self.assertEqual(counter['perm_after'], counter['perm_before'])
    self.assertEqual(counter['session_after'], 0)
    self.assertNotEqual(counter['session_before'], 0)
