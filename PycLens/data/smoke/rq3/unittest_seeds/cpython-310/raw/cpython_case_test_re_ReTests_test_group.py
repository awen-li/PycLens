# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Index:

        def __init__(self, value):
            self.value = value

        def __index__(self):
            return self.value
    m = re.match('(a)(b)', 'ab')
    self.assertEqual(m.group(), 'ab')
    self.assertEqual(m.group(0), 'ab')
    self.assertEqual(m.group(1), 'a')
    self.assertEqual(m.group(Index(1)), 'a')
    self.assertRaises(IndexError, m.group, -1)
    self.assertRaises(IndexError, m.group, 3)
    self.assertRaises(IndexError, m.group, 1 << 1000)
    self.assertRaises(IndexError, m.group, Index(1 << 1000))
    self.assertRaises(IndexError, m.group, 'x')
    self.assertEqual(m.group(2, 1), ('b', 'a'))
    self.assertEqual(m.group(Index(2), Index(1)), ('b', 'a'))
