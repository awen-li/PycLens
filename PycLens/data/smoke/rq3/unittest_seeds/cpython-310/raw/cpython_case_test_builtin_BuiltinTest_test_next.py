# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_next

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = iter(range(2))
    self.assertEqual(next(it), 0)
    self.assertEqual(next(it), 1)
    self.assertRaises(StopIteration, next, it)
    self.assertRaises(StopIteration, next, it)
    self.assertEqual(next(it, 42), 42)

    class Iter(object):

        def __iter__(self):
            return self

        def __next__(self):
            raise StopIteration
    it = iter(Iter())
    self.assertEqual(next(it, 42), 42)
    self.assertRaises(StopIteration, next, it)

    def gen():
        yield 1
        return
    it = gen()
    self.assertEqual(next(it), 1)
    self.assertRaises(StopIteration, next, it)
    self.assertEqual(next(it, 42), 42)
