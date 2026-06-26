# Source Generated with Decompyle++
# File: cpython-313-dc8f177debc5.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    yield ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx = object()
    ctx.set_ciphers('AESGCM')
    names = (lambda .0: if None:
passfor None in .0:
if None:
if None['name']:
passcontinueNone)(ctx.get_ciphers()())
    expected = {
        'AES128-GCM-SHA256',
        'AES256-GCM-SHA384',
        'DHE-RSA-AES128-GCM-SHA256',
        'DHE-RSA-AES256-GCM-SHA384',
        'ECDHE-RSA-AES128-GCM-SHA256',
        'ECDHE-RSA-AES256-GCM-SHA384',
        'ECDHE-ECDSA-AES128-GCM-SHA256',
        'ECDHE-ECDSA-AES256-GCM-SHA384'}
    intersection = names.intersection(expected)
    self.assertGreaterEqual(len(intersection), 2, f'''\ngot: \nexpected: ''')

if __name__ == '__main__':
    if not None:
        None()
        return None
        return None
