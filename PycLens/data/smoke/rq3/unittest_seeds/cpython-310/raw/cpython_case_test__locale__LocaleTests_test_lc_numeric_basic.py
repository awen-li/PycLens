# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__locale.py
# case: _LocaleTests_test_lc_numeric_basic

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
        for (li, lc) in ((RADIXCHAR, 'decimal_point'), (THOUSEP, 'thousands_sep')):
            nl_radixchar = nl_langinfo(li)
            li_radixchar = localeconv()[lc]
            try:
                set_locale = setlocale(LC_NUMERIC)
            except Error:
                set_locale = '<not able to determine>'
            self.assertEqual(nl_radixchar, li_radixchar, '%s (nl_langinfo) != %s (localeconv) (set to %s, using %s)' % (nl_radixchar, li_radixchar, loc, set_locale))
            tested = True
    if not tested:
        self.skipTest('no suitable locales')
