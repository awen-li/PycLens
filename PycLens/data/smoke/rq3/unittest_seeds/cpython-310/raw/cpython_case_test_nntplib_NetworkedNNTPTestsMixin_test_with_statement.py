# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_with_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def is_connected():
        if not hasattr(server, 'file'):
            return False
        try:
            server.help()
        except (OSError, EOFError):
            return False
        return True
    kwargs = dict(timeout=support.INTERNET_TIMEOUT, usenetrc=False)
    if self.ssl_context is not None:
        kwargs['ssl_context'] = self.ssl_context
    try:
        server = self.NNTP_CLASS(self.NNTP_HOST, **kwargs)
        with server:
            self.assertTrue(is_connected())
            self.assertTrue(server.help())
        self.assertFalse(is_connected())
        server = self.NNTP_CLASS(self.NNTP_HOST, **kwargs)
        with server:
            server.quit()
        self.assertFalse(is_connected())
    except SSLError as ssl_err:
        if re.search('(?i)KEY.TOO.SMALL', ssl_err.reason):
            raise unittest.SkipTest(f'Got {ssl_err} connecting to {self.NNTP_HOST!r}')
        raise
