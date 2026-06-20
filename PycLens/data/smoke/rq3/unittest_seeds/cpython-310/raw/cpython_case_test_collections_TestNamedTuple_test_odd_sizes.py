# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_odd_sizes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Zero = namedtuple('Zero', '')
    self.assertEqual(Zero(), ())
    self.assertEqual(Zero._make([]), ())
    self.assertEqual(repr(Zero()), 'Zero()')
    self.assertEqual(Zero()._asdict(), {})
    self.assertEqual(Zero()._fields, ())
    Dot = namedtuple('Dot', 'd')
    self.assertEqual(Dot(1), (1,))
    self.assertEqual(Dot._make([1]), (1,))
    self.assertEqual(Dot(1).d, 1)
    self.assertEqual(repr(Dot(1)), 'Dot(d=1)')
    self.assertEqual(Dot(1)._asdict(), {'d': 1})
    self.assertEqual(Dot(1)._replace(d=999), (999,))
    self.assertEqual(Dot(1)._fields, ('d',))
    n = 5000
    names = list(set((''.join([choice(string.ascii_letters) for j in range(10)]) for i in range(n))))
    n = len(names)
    Big = namedtuple('Big', names)
    b = Big(*range(n))
    self.assertEqual(b, tuple(range(n)))
    self.assertEqual(Big._make(range(n)), tuple(range(n)))
    for (pos, name) in enumerate(names):
        self.assertEqual(getattr(b, name), pos)
    repr(b)
    d = b._asdict()
    d_expected = dict(zip(names, range(n)))
    self.assertEqual(d, d_expected)
    b2 = b._replace(**dict([(names[1], 999), (names[-5], 42)]))
    b2_expected = list(range(n))
    b2_expected[1] = 999
    b2_expected[-5] = 42
    self.assertEqual(b2, tuple(b2_expected))
    self.assertEqual(b._fields, tuple(names))
