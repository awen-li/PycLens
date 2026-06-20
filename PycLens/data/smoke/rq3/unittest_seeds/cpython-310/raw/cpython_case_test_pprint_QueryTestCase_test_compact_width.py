# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_compact_width

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    levels = 20
    number = 10
    o = [0] * number
    for i in range(levels - 1):
        o = [o]
    for w in range(levels * 2 + 1, levels + 3 * number - 1):
        lines = pprint.pformat(o, width=w, compact=True).splitlines()
        maxwidth = max(map(len, lines))
        self.assertLessEqual(maxwidth, w)
        self.assertGreater(maxwidth, w - 3)
