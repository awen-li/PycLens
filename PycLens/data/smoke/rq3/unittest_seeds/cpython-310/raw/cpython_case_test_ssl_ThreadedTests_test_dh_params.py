# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_dh_params

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    client_context.maximum_version = ssl.TLSVersion.TLSv1_2
    server_context.load_dh_params(DHFILE)
    server_context.set_ciphers('kEDH')
    server_context.maximum_version = ssl.TLSVersion.TLSv1_2
    stats = server_params_test(client_context, server_context, chatty=True, connectionchatty=True, sni_name=hostname)
    cipher = stats['cipher'][0]
    parts = cipher.split('-')
    if 'ADH' not in parts and 'EDH' not in parts and ('DHE' not in parts):
        self.fail('Non-DH cipher: ' + cipher[0])
