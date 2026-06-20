# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_2537

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for outer_op in ('{0,}', '*', '+', '{1,187}'):
        for inner_op in ('{0,}', '*', '?'):
            r = re.compile('^((x|y)%s)%s' % (inner_op, outer_op))
            m = r.match('xyyzy')
            self.assertEqual(m.group(0), 'xyy')
            self.assertEqual(m.group(1), '')
            self.assertEqual(m.group(2), 'y')
