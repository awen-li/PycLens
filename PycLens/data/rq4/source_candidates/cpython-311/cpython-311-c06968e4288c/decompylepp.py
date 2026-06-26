# Source Generated with Decompyle++
# File: cpython-311-c06968e4288c.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tested = False
    for loc in candidate_locales:
        setlocale(LC_NUMERIC, loc)
        setlocale(LC_CTYPE, loc)
    if None or Error:
        continue
    for li, lc in ((RADIXCHAR, 'decimal_point'), (THOUSEP, 'thousands_sep')):
        if self.numeric_tester('nl_langinfo', nl_langinfo(li), lc, loc):
            tested = True
    continue
    if not tested:
        self.skipTest('no suitable locales')
        return None

# WARNING: Decompyle incomplete
