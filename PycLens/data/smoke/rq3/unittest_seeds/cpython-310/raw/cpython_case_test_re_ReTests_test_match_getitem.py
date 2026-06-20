# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_match_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pat = re.compile('(?:(?P<a1>a)|(?P<b2>b))(?P<c3>c)?')
    m = pat.match('a')
    self.assertEqual(m['a1'], 'a')
    self.assertEqual(m['b2'], None)
    self.assertEqual(m['c3'], None)
    self.assertEqual('a1={a1} b2={b2} c3={c3}'.format_map(m), 'a1=a b2=None c3=None')
    self.assertEqual(m[0], 'a')
    self.assertEqual(m[1], 'a')
    self.assertEqual(m[2], None)
    self.assertEqual(m[3], None)
    with self.assertRaisesRegex(IndexError, 'no such group'):
        m['X']
    with self.assertRaisesRegex(IndexError, 'no such group'):
        m[-1]
    with self.assertRaisesRegex(IndexError, 'no such group'):
        m[4]
    with self.assertRaisesRegex(IndexError, 'no such group'):
        m[0, 1]
    with self.assertRaisesRegex(IndexError, 'no such group'):
        m[0,]
    with self.assertRaisesRegex(IndexError, 'no such group'):
        m[0, 1]
    with self.assertRaisesRegex(IndexError, 'no such group'):
        'a1={a2}'.format_map(m)
    m = pat.match('ac')
    self.assertEqual(m['a1'], 'a')
    self.assertEqual(m['b2'], None)
    self.assertEqual(m['c3'], 'c')
    self.assertEqual('a1={a1} b2={b2} c3={c3}'.format_map(m), 'a1=a b2=None c3=c')
    self.assertEqual(m[0], 'ac')
    self.assertEqual(m[1], 'a')
    self.assertEqual(m[2], None)
    self.assertEqual(m[3], 'c')
    with self.assertRaises(TypeError):
        m[0] = 1
    self.assertRaises(TypeError, len, m)
