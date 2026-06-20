# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: MockSocketTests_test_login_aborted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    login = 't@e.com'
    password = 'python'

    class Handler(NNTPv1Handler):

        def handle_AUTHINFO(self, *args):
            self.push_lit(authinfo_response)
    authinfo_response = '503 Mechanism not recognized'
    self.check_constructor_error_conditions(Handler, nntplib.NNTPPermanentError, authinfo_response, login, password)
