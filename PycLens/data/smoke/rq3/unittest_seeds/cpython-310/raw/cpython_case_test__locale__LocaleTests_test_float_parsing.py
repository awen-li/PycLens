# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__locale.py
# case: _LocaleTests_test_float_parsing

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
        if loc == 'eu_ES' and localeconv()['decimal_point'] == "' ":
            continue
        self.assertEqual(int(eval('3.14') * 100), 314, "using eval('3.14') failed for %s" % loc)
        self.assertEqual(int(float('3.14') * 100), 314, "using float('3.14') failed for %s" % loc)
        if localeconv()['decimal_point'] != '.':
            self.assertRaises(ValueError, float, localeconv()['decimal_point'].join(['1', '23']))
        tested = True
    if not tested:
        self.skipTest('no suitable locales')
