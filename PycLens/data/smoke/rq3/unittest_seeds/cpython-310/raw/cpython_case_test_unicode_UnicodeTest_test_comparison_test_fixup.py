# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_comparison_test_fixup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s2 = '\ud800\udc01'
    test_lecmp(s, s2)
    s2 = '\ud900\udc01'
    test_lecmp(s, s2)
    s2 = '\uda00\udc01'
    test_lecmp(s, s2)
    s2 = '\udb00\udc01'
    test_lecmp(s, s2)
    s2 = '\ud800\udd01'
    test_lecmp(s, s2)
    s2 = '\ud900\udd01'
    test_lecmp(s, s2)
    s2 = '\uda00\udd01'
    test_lecmp(s, s2)
    s2 = '\udb00\udd01'
    test_lecmp(s, s2)
    s2 = '\ud800\ude01'
    test_lecmp(s, s2)
    s2 = '\ud900\ude01'
    test_lecmp(s, s2)
    s2 = '\uda00\ude01'
    test_lecmp(s, s2)
    s2 = '\udb00\ude01'
    test_lecmp(s, s2)
    s2 = '\ud800\udfff'
    test_lecmp(s, s2)
    s2 = '\ud900\udfff'
    test_lecmp(s, s2)
    s2 = '\uda00\udfff'
    test_lecmp(s, s2)
    s2 = '\udb00\udfff'
    test_lecmp(s, s2)
    test_fixup('\ue000')
    test_fixup('｡')
