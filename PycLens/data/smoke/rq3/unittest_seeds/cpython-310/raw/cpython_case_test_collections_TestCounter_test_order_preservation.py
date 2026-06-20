# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_order_preservation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(Counter('abracadabra').items()), [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])
    self.assertEqual(list(Counter('xyzpdqqdpzyx').items()), [('x', 2), ('y', 2), ('z', 2), ('p', 2), ('d', 2), ('q', 2)])
    self.assertEqual(list(Counter('abracadabra simsalabim').elements()), ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'r', 'r', 'c', 'd', ' ', 's', 's', 'i', 'i', 'm', 'm', 'l'])
    ps = 'aaabbcdddeefggghhijjjkkl'
    qs = 'abbcccdeefffhkkllllmmnno'
    order = {letter: i for (i, letter) in enumerate(dict.fromkeys(ps + qs))}

    def correctly_ordered(seq):
        """Return true if the letters occur in the expected order"""
        positions = [order[letter] for letter in seq]
        return positions == sorted(positions)
    (p, q) = (Counter(ps), Counter(qs))
    self.assertTrue(correctly_ordered(+p))
    self.assertTrue(correctly_ordered(-p))
    self.assertTrue(correctly_ordered(p + q))
    self.assertTrue(correctly_ordered(p - q))
    self.assertTrue(correctly_ordered(p | q))
    self.assertTrue(correctly_ordered(p & q))
    (p, q) = (Counter(ps), Counter(qs))
    p += q
    self.assertTrue(correctly_ordered(p))
    (p, q) = (Counter(ps), Counter(qs))
    p -= q
    self.assertTrue(correctly_ordered(p))
    (p, q) = (Counter(ps), Counter(qs))
    p |= q
    self.assertTrue(correctly_ordered(p))
    (p, q) = (Counter(ps), Counter(qs))
    p &= q
    self.assertTrue(correctly_ordered(p))
    (p, q) = (Counter(ps), Counter(qs))
    p.update(q)
    self.assertTrue(correctly_ordered(p))
    (p, q) = (Counter(ps), Counter(qs))
    p.subtract(q)
    self.assertTrue(correctly_ordered(p))
