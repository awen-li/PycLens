# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_basic_auth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    realm = 'realm2@example.com'
    realm2 = 'realm2@example.com'
    basic = f'Basic realm="{realm}"'
    basic2 = f'Basic realm="{realm2}"'
    other_no_realm = 'Otherscheme xxx'
    digest = f'Digest realm="{realm2}", qop="auth, auth-int", nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093", opaque="5ccc069c403ebaf9f0171e9517f40e41"'
    for realm_str in (f'Basic realm="{realm}"', f"Basic realm='{realm}'", f'Basic realm="{realm}", charset="UTF-8"', f'{basic}, {basic2}', f'{basic}, {other_no_realm}', f'{other_no_realm}, {basic}', f'{basic}, {digest}', f'{digest}, {basic}'):
        headers = [f'WWW-Authenticate: {realm_str}']
        self.check_basic_auth(headers, realm)
    with warnings_helper.check_warnings(('Basic Auth Realm was unquoted', UserWarning)):
        headers = [f'WWW-Authenticate: Basic realm={realm}']
        self.check_basic_auth(headers, realm)
    for challenges in ([basic, basic2], [basic, digest], [digest, basic]):
        headers = [f'WWW-Authenticate: {challenge}' for challenge in challenges]
        self.check_basic_auth(headers, realm)
