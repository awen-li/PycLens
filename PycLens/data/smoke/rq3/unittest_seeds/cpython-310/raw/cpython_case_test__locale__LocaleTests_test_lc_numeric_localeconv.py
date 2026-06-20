# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__locale.py
# case: _LocaleTests_test_lc_numeric_localeconv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tested = False
    for loc in candidate_locales:
        try:
            setlocale(LC_NUMERIC, loc)
            setlocale(LC_CTYPE, loc)
        except Error:
            continue
        formatting = localeconv()
        for lc in ('decimal_point', 'thousands_sep'):
            if self.numeric_tester('localeconv', formatting[lc], lc, loc):
                tested = True
    if not tested:
        self.skipTest('no suitable locales')
