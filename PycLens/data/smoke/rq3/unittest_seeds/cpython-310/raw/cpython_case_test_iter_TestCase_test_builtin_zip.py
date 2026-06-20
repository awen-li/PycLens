# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_builtin_zip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(zip()), [])
    self.assertEqual(list(zip(*[])), [])
    self.assertEqual(list(zip(*[(1, 2), 'ab'])), [(1, 'a'), (2, 'b')])
    self.assertRaises(TypeError, zip, None)
    self.assertRaises(TypeError, zip, range(10), 42)
    self.assertRaises(TypeError, zip, range(10), zip)
    self.assertEqual(list(zip(IteratingSequenceClass(3))), [(0,), (1,), (2,)])
    self.assertEqual(list(zip(SequenceClass(3))), [(0,), (1,), (2,)])
    d = {'one': 1, 'two': 2, 'three': 3}
    self.assertEqual(list(d.items()), list(zip(d, d.values())))

    class IntsFrom:

        def __init__(self, start):
            self.i = start

        def __iter__(self):
            return self

        def __next__(self):
            i = self.i
            self.i = i + 1
            return i
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        f.write('a\nbbb\ncc\n')
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        self.assertEqual(list(zip(IntsFrom(0), f, IntsFrom(-100))), [(0, 'a\n', -100), (1, 'bbb\n', -99), (2, 'cc\n', -98)])
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
    self.assertEqual(list(zip(range(5))), [(i,) for i in range(5)])

    class NoGuessLen5:

        def __getitem__(self, i):
            if i >= 5:
                raise IndexError
            return i

    class Guess3Len5(NoGuessLen5):

        def __len__(self):
            return 3

    class Guess30Len5(NoGuessLen5):

        def __len__(self):
            return 30

    def lzip(*args):
        return list(zip(*args))
    self.assertEqual(len(Guess3Len5()), 3)
    self.assertEqual(len(Guess30Len5()), 30)
    self.assertEqual(lzip(NoGuessLen5()), lzip(range(5)))
    self.assertEqual(lzip(Guess3Len5()), lzip(range(5)))
    self.assertEqual(lzip(Guess30Len5()), lzip(range(5)))
    expected = [(i, i) for i in range(5)]
    for x in (NoGuessLen5(), Guess3Len5(), Guess30Len5()):
        for y in (NoGuessLen5(), Guess3Len5(), Guess30Len5()):
            self.assertEqual(lzip(x, y), expected)
