# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_builtin_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(filter(None, SequenceClass(5))), list(range(1, 5)))
    self.assertEqual(list(filter(None, SequenceClass(0))), [])
    self.assertEqual(list(filter(None, ())), [])
    self.assertEqual(list(filter(None, 'abc')), ['a', 'b', 'c'])
    d = {'one': 1, 'two': 2, 'three': 3}
    self.assertEqual(list(filter(None, d)), list(d.keys()))
    self.assertRaises(TypeError, filter, None, list)
    self.assertRaises(TypeError, filter, None, 42)

    class Boolean:

        def __init__(self, truth):
            self.truth = truth

        def __bool__(self):
            return self.truth
    bTrue = Boolean(True)
    bFalse = Boolean(False)

    class Seq:

        def __init__(self, *args):
            self.vals = args

        def __iter__(self):

            class SeqIter:

                def __init__(self, vals):
                    self.vals = vals
                    self.i = 0

                def __iter__(self):
                    return self

                def __next__(self):
                    i = self.i
                    self.i = i + 1
                    if i < len(self.vals):
                        return self.vals[i]
                    else:
                        raise StopIteration
            return SeqIter(self.vals)
    seq = Seq(*[bTrue, bFalse] * 25)
    self.assertEqual(list(filter(lambda x: not x, seq)), [bFalse] * 25)
    self.assertEqual(list(filter(lambda x: not x, iter(seq))), [bFalse] * 25)
