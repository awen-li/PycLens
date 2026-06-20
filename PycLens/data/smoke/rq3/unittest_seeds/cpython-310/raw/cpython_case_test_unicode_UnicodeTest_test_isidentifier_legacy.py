# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isidentifier_legacy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    u = '𝖀𝖓𝖎𝖈𝖔𝖉𝖊'
    self.assertTrue(u.isidentifier())
    with warnings_helper.check_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        self.assertTrue(_testcapi.unicode_legacy_string(u).isidentifier())
