# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('', 'abracadabra', 'simsalabim' * 500 + 'abc'):
        s = list(s)
        d = deque(s)
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(s.count(letter), d.count(letter), (s, d, letter))
    self.assertRaises(TypeError, d.count)
    self.assertRaises(TypeError, d.count, 1, 2)

    class BadCompare:

        def __eq__(self, other):
            raise ArithmeticError
    d = deque([1, 2, BadCompare(), 3])
    self.assertRaises(ArithmeticError, d.count, 2)
    d = deque([1, 2, 3])
    self.assertRaises(ArithmeticError, d.count, BadCompare())

    class MutatingCompare:

        def __eq__(self, other):
            self.d.pop()
            return True
    m = MutatingCompare()
    d = deque([1, 2, 3, m, 4, 5])
    m.d = d
    self.assertRaises(RuntimeError, d.count, 3)
    d = deque([None] * 16)
    for i in range(len(d)):
        d.rotate(-1)
    d.rotate(1)
    self.assertEqual(d.count(1), 0)
    self.assertEqual(d.count(None), 16)
