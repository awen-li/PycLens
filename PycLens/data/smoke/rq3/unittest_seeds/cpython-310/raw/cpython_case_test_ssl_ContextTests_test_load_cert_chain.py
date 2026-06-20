# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_load_cert_chain

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(CERTFILE, keyfile=None)
    ctx.load_cert_chain(CERTFILE, keyfile=CERTFILE)
    self.assertRaises(TypeError, ctx.load_cert_chain, keyfile=CERTFILE)
    with self.assertRaises(OSError) as cm:
        ctx.load_cert_chain(NONEXISTINGCERT)
    self.assertEqual(cm.exception.errno, errno.ENOENT)
    with self.assertRaisesRegex(ssl.SSLError, 'PEM lib'):
        ctx.load_cert_chain(BADCERT)
    with self.assertRaisesRegex(ssl.SSLError, 'PEM lib'):
        ctx.load_cert_chain(EMPTYCERT)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(ONLYCERT, ONLYKEY)
    ctx.load_cert_chain(certfile=ONLYCERT, keyfile=ONLYKEY)
    ctx.load_cert_chain(certfile=BYTES_ONLYCERT, keyfile=BYTES_ONLYKEY)
    with self.assertRaisesRegex(ssl.SSLError, 'PEM lib'):
        ctx.load_cert_chain(ONLYCERT)
    with self.assertRaisesRegex(ssl.SSLError, 'PEM lib'):
        ctx.load_cert_chain(ONLYKEY)
    with self.assertRaisesRegex(ssl.SSLError, 'PEM lib'):
        ctx.load_cert_chain(certfile=ONLYKEY, keyfile=ONLYCERT)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    with self.assertRaisesRegex(ssl.SSLError, 'key values mismatch'):
        ctx.load_cert_chain(CAFILE_CACERT, ONLYKEY)
    ctx.load_cert_chain(CERTFILE_PROTECTED, password=KEY_PASSWORD)
    ctx.load_cert_chain(CERTFILE_PROTECTED, password=KEY_PASSWORD.encode())
    ctx.load_cert_chain(CERTFILE_PROTECTED, password=bytearray(KEY_PASSWORD.encode()))
    ctx.load_cert_chain(ONLYCERT, ONLYKEY_PROTECTED, KEY_PASSWORD)
    ctx.load_cert_chain(ONLYCERT, ONLYKEY_PROTECTED, KEY_PASSWORD.encode())
    ctx.load_cert_chain(ONLYCERT, ONLYKEY_PROTECTED, bytearray(KEY_PASSWORD.encode()))
    with self.assertRaisesRegex(TypeError, 'should be a string'):
        ctx.load_cert_chain(CERTFILE_PROTECTED, password=True)
    with self.assertRaises(ssl.SSLError):
        ctx.load_cert_chain(CERTFILE_PROTECTED, password='badpass')
    with self.assertRaisesRegex(ValueError, 'cannot be longer'):
        ctx.load_cert_chain(CERTFILE_PROTECTED, password=b'a' * 102400)

    def getpass_unicode():
        return KEY_PASSWORD

    def getpass_bytes():
        return KEY_PASSWORD.encode()

    def getpass_bytearray():
        return bytearray(KEY_PASSWORD.encode())

    def getpass_badpass():
        return 'badpass'

    def getpass_huge():
        return b'a' * (1024 * 1024)

    def getpass_bad_type():
        return 9

    def getpass_exception():
        raise Exception('getpass error')

    class GetPassCallable:

        def __call__(self):
            return KEY_PASSWORD

        def getpass(self):
            return KEY_PASSWORD
    ctx.load_cert_chain(CERTFILE_PROTECTED, password=getpass_unicode)
    ctx.load_cert_chain(CERTFILE_PROTECTED, password=getpass_bytes)
    ctx.load_cert_chain(CERTFILE_PROTECTED, password=getpass_bytearray)
    ctx.load_cert_chain(CERTFILE_PROTECTED, password=GetPassCallable())
    ctx.load_cert_chain(CERTFILE_PROTECTED, password=GetPassCallable().getpass)
    with self.assertRaises(ssl.SSLError):
        ctx.load_cert_chain(CERTFILE_PROTECTED, password=getpass_badpass)
    with self.assertRaisesRegex(ValueError, 'cannot be longer'):
        ctx.load_cert_chain(CERTFILE_PROTECTED, password=getpass_huge)
    with self.assertRaisesRegex(TypeError, 'must return a string'):
        ctx.load_cert_chain(CERTFILE_PROTECTED, password=getpass_bad_type)
    with self.assertRaisesRegex(Exception, 'getpass error'):
        ctx.load_cert_chain(CERTFILE_PROTECTED, password=getpass_exception)
    ctx.load_cert_chain(CERTFILE, password=getpass_exception)
