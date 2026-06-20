# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_auth_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    supported = {'PLAIN', 'LOGIN'}
    try:
        hashlib.md5()
    except ValueError:
        pass
    else:
        supported.add('CRAM-MD5')
    for mechanism in supported:
        self.serv.add_feature('AUTH {}'.format(mechanism))
    for mechanism in supported:
        with self.subTest(mechanism=mechanism):
            smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
            smtp.ehlo('foo')
            (smtp.user, smtp.password) = (sim_auth[0], sim_auth[1])
            method = 'auth_' + mechanism.lower().replace('-', '_')
            resp = smtp.auth(mechanism, getattr(smtp, method))
            self.assertEqual(resp, (235, b'Authentication Succeeded'))
            smtp.close()
