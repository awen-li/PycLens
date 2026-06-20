# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_zip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = (1, 2, 3)
    b = (4, 5, 6)
    t = [(1, 4), (2, 5), (3, 6)]
    self.assertEqual(list(zip(a, b)), t)
    b = [4, 5, 6]
    self.assertEqual(list(zip(a, b)), t)
    b = (4, 5, 6, 7)
    self.assertEqual(list(zip(a, b)), t)

    class I:

        def __getitem__(self, i):
            if i < 0 or i > 2:
                raise IndexError
            return i + 4
    self.assertEqual(list(zip(a, I())), t)
    self.assertEqual(list(zip()), [])
    self.assertEqual(list(zip(*[])), [])
    self.assertRaises(TypeError, zip, None)

    class G:
        pass
    self.assertRaises(TypeError, zip, a, G())
    self.assertRaises(RuntimeError, zip, a, TestFailingIter())

    class SequenceWithoutALength:

        def __getitem__(self, i):
            if i == 5:
                raise IndexError
            else:
                return i
    self.assertEqual(list(zip(SequenceWithoutALength(), range(2 ** 30))), list(enumerate(range(5))))

    class BadSeq:

        def __getitem__(self, i):
            if i == 5:
                raise ValueError
            else:
                return i
    self.assertRaises(ValueError, list, zip(BadSeq(), BadSeq()))
