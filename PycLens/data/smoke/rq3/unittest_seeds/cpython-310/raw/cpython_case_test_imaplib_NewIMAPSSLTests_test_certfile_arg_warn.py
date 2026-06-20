# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPSSLTests_test_certfile_arg_warn

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        with mock.patch.object(self.imap_class, 'open'):
            with mock.patch.object(self.imap_class, '_connect'):
                self.imap_class('localhost', 143, certfile=CERTFILE)
