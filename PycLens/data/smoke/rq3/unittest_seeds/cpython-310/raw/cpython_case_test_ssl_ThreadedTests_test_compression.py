# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_compression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    stats = server_params_test(client_context, server_context, chatty=True, connectionchatty=True, sni_name=hostname)
    if support.verbose:
        sys.stdout.write(' got compression: {!r}\n'.format(stats['compression']))
    self.assertIn(stats['compression'], {None, 'ZLIB', 'RLE'})
