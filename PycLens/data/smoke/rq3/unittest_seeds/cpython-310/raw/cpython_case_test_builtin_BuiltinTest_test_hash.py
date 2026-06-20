# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hash(None)
    self.assertEqual(hash(1), hash(1))
    self.assertEqual(hash(1), hash(1.0))
    hash('spam')
    self.assertEqual(hash('spam'), hash(b'spam'))
    hash((0, 1, 2, 3))

    def f():
        pass
    hash(f)
    self.assertRaises(TypeError, hash, [])
    self.assertRaises(TypeError, hash, {})

    class X:

        def __hash__(self):
            return 2 ** 100
    self.assertEqual(type(hash(X())), int)

    class Z(int):

        def __hash__(self):
            return self
    self.assertEqual(hash(Z(42)), hash(42))
