# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: test_wrap_socket

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    if not kwargs.get('server_side'):
        kwargs['server_hostname'] = SIGNED_CERTFILE_HOSTNAME
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    else:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    if cert_reqs is not None:
        if cert_reqs == ssl.CERT_NONE:
            context.check_hostname = False
        context.verify_mode = cert_reqs
    if ca_certs is not None:
        context.load_verify_locations(ca_certs)
    if certfile is not None or keyfile is not None:
        context.load_cert_chain(certfile, keyfile)
    if ciphers is not None:
        context.set_ciphers(ciphers)
    return context.wrap_socket(sock, **kwargs)
