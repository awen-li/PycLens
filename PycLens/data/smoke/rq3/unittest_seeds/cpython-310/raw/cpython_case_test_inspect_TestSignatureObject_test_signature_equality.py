# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a, *, b: int) -> float:
        pass
    self.assertFalse(inspect.signature(foo) == 42)
    self.assertTrue(inspect.signature(foo) != 42)
    self.assertTrue(inspect.signature(foo) == ALWAYS_EQ)
    self.assertFalse(inspect.signature(foo) != ALWAYS_EQ)

    def bar(a, *, b: int) -> float:
        pass
    self.assertTrue(inspect.signature(foo) == inspect.signature(bar))
    self.assertFalse(inspect.signature(foo) != inspect.signature(bar))
    self.assertEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def bar(a, *, b: int) -> int:
        pass
    self.assertFalse(inspect.signature(foo) == inspect.signature(bar))
    self.assertTrue(inspect.signature(foo) != inspect.signature(bar))
    self.assertNotEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def bar(a, *, b: int):
        pass
    self.assertFalse(inspect.signature(foo) == inspect.signature(bar))
    self.assertTrue(inspect.signature(foo) != inspect.signature(bar))
    self.assertNotEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def bar(a, *, b: int=42) -> float:
        pass
    self.assertFalse(inspect.signature(foo) == inspect.signature(bar))
    self.assertTrue(inspect.signature(foo) != inspect.signature(bar))
    self.assertNotEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def bar(a, *, c) -> float:
        pass
    self.assertFalse(inspect.signature(foo) == inspect.signature(bar))
    self.assertTrue(inspect.signature(foo) != inspect.signature(bar))
    self.assertNotEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def bar(a, b: int) -> float:
        pass
    self.assertFalse(inspect.signature(foo) == inspect.signature(bar))
    self.assertTrue(inspect.signature(foo) != inspect.signature(bar))
    self.assertNotEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def spam(b: int, a) -> float:
        pass
    self.assertFalse(inspect.signature(spam) == inspect.signature(bar))
    self.assertTrue(inspect.signature(spam) != inspect.signature(bar))
    self.assertNotEqual(hash(inspect.signature(spam)), hash(inspect.signature(bar)))

    def foo(*, a, b, c):
        pass

    def bar(*, c, b, a):
        pass
    self.assertTrue(inspect.signature(foo) == inspect.signature(bar))
    self.assertFalse(inspect.signature(foo) != inspect.signature(bar))
    self.assertEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def foo(*, a=1, b, c):
        pass

    def bar(*, c, b, a=1):
        pass
    self.assertTrue(inspect.signature(foo) == inspect.signature(bar))
    self.assertFalse(inspect.signature(foo) != inspect.signature(bar))
    self.assertEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def foo(pos, *, a=1, b, c):
        pass

    def bar(pos, *, c, b, a=1):
        pass
    self.assertTrue(inspect.signature(foo) == inspect.signature(bar))
    self.assertFalse(inspect.signature(foo) != inspect.signature(bar))
    self.assertEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def foo(pos, *, a, b, c):
        pass

    def bar(pos, *, c, b, a=1):
        pass
    self.assertFalse(inspect.signature(foo) == inspect.signature(bar))
    self.assertTrue(inspect.signature(foo) != inspect.signature(bar))
    self.assertNotEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))

    def foo(pos, *args, a=42, b, c, **kwargs: int):
        pass

    def bar(pos, *args, c, b, a=42, **kwargs: int):
        pass
    self.assertTrue(inspect.signature(foo) == inspect.signature(bar))
    self.assertFalse(inspect.signature(foo) != inspect.signature(bar))
    self.assertEqual(hash(inspect.signature(foo)), hash(inspect.signature(bar)))
