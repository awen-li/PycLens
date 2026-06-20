# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_zlogin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    baduser = 'notarealuser'
    badpw = 'notarealpassword'
    self.assertRaises(nntplib.NNTPError, self.server.login, user=baduser, password=badpw, usenetrc=False)
