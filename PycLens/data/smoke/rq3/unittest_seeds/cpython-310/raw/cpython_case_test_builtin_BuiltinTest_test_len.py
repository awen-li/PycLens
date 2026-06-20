# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(len('123'), 3)
    self.assertEqual(len(()), 0)
    self.assertEqual(len((1, 2, 3, 4)), 4)
    self.assertEqual(len([1, 2, 3, 4]), 4)
    self.assertEqual(len({}), 0)
    self.assertEqual(len({'a': 1, 'b': 2}), 2)

    class BadSeq:

        def __len__(self):
            raise ValueError
    self.assertRaises(ValueError, len, BadSeq())

    class InvalidLen:

        def __len__(self):
            return None
    self.assertRaises(TypeError, len, InvalidLen())

    class FloatLen:

        def __len__(self):
            return 4.5
    self.assertRaises(TypeError, len, FloatLen())

    class NegativeLen:

        def __len__(self):
            return -10
    self.assertRaises(ValueError, len, NegativeLen())

    class HugeLen:

        def __len__(self):
            return sys.maxsize + 1
    self.assertRaises(OverflowError, len, HugeLen())

    class HugeNegativeLen:

        def __len__(self):
            return -sys.maxsize - 10
    self.assertRaises(ValueError, len, HugeNegativeLen())

    class NoLenMethod(object):
        pass
    self.assertRaises(TypeError, len, NoLenMethod())
