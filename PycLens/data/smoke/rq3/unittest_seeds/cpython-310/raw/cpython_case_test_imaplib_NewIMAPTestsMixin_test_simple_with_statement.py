# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_simple_with_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (_, server) = self._setup(SimpleIMAPHandler, connect=False)
    with self.imap_class(*server.server_address):
        pass
