# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_webbrowser.py
# case: NetscapeCommandTest_test_open_with_autoraise_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test('open', kw=dict(autoraise=False), options=['-noraise', '-remote'], arguments=['openURL({})'.format(URL)])
