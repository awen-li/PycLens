# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_response_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'HTTP/1.1 200 OK\r\nSet-Cookie: Customer="WILE_E_COYOTE"; Version="1"; Path="/acme"\r\nSet-Cookie: Part_Number="Rocket_Launcher_0001"; Version="1"; Path="/acme"\r\n\r\nNo body\r\n'
    hdr = 'Customer="WILE_E_COYOTE"; Version="1"; Path="/acme", Part_Number="Rocket_Launcher_0001"; Version="1"; Path="/acme"'
    s = FakeSocket(text)
    r = client.HTTPResponse(s)
    r.begin()
    cookies = r.getheader('Set-Cookie')
    self.assertEqual(cookies, hdr)
