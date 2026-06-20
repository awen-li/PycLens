# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: MockSocketTests_test_bad_welcome

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Handler(NNTPv1Handler):
        welcome = 'Bad Welcome'
    self.check_constructor_error_conditions(Handler, nntplib.NNTPProtocolError, Handler.welcome)
