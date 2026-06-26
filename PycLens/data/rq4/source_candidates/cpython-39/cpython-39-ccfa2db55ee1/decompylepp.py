# Source Generated with Decompyle++
# File: cpython-39-ccfa2db55ee1.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = None in None()
    __pybcsec_self__ = self
    realm = 'realm2@example.com'
    realm2 = 'realm2@example.com'
    basic = f'''Basic realm="{realm}"'''
    basic2 = f'''Basic realm="{realm2}"'''
    other_no_realm = 'Otherscheme xxx'
    digest = f'''Digest realm="{realm2}", qop="auth, auth-int", nonce="dcd98b7102found.\x00\x00\x00\x00\x00\x00\xe3\x00\x00\x00\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00 opaque="5ccc069c403ebaf9f0171e9517f40e41"'''
    for realm_str in (f'''Basic realm="{realm}"''', f'''Basic realm=\'{realm}\'''', f'''Basic realm="{realm}", charset="UTF-8"''', f'''{basic}, {basic2}''', f'''{basic}, {other_no_realm}''', f'''{other_no_realm}, {basic}''', f'''{basic}, {digest}''', f'''{digest}, {basic}'''):
        headers = [
            f'''WWW-Authenticate: {realm_str}''']
        self.check_basic_auth(headers, realm)
    with support.check_warnings(('Basic Auth Realm was unquoted', UserWarning)):
        headers = [
            f'''WWW-Authenticate: Basic realm={realm}''']
        self.check_basic_auth(headers, realm)
        None(None, None, None)
    with None:
        if not None:
            pass
    for challenges in ([
        basic,
        basic2], [
        basic,
        digest], [
        digest,
        basic]):
        headers = (lambda .0: [ f'''WWW-Authenticate: {challenge}''' for challenge in .0 ])(challenges)
        self.check_basic_auth(headers, realm)

if __name__ == '__main__':
    __pybcsec_seed__()
