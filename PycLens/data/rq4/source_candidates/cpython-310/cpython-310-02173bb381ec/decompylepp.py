# Source Generated with Decompyle++
# File: cpython-310-02173bb381ec.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in (None, None, None, None, None, '123', '', range(1000), ('do', 1.2), range(2000, 2200, 5)):
        for g in (G, I, Ig, S, L, R):
            self.assertEqual(list(zip_longest(g(s))), list(zip(g(s))))
            self.assertEqual(list(zip_longest(g(s), g(s))), list(zip(g(s), g(s))))
        self.assertRaises(TypeError, zip_longest, X(s))
        self.assertRaises(TypeError, zip_longest, N(s))
        self.assertRaises(ZeroDivisionError, list, zip_longest(E(s)))

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
