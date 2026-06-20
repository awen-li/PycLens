# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NonGen1:

        def __iter__(self):
            return self

        def __next__(self):
            return None

        def close(self):
            pass

        def throw(self, typ, val=None, tb=None):
            pass

    class NonGen2:

        def __iter__(self):
            return self

        def __next__(self):
            return None

        def close(self):
            pass

        def send(self, value):
            return value

    class NonGen3:

        def close(self):
            pass

        def send(self, value):
            return value

        def throw(self, typ, val=None, tb=None):
            pass
    non_samples = [None, 42, 3.14, 1j, b'', '', (), [], {}, set(), iter(()), iter([]), NonGen1(), NonGen2(), NonGen3()]
    for x in non_samples:
        self.assertNotIsInstance(x, Generator)
        self.assertFalse(issubclass(type(x), Generator), repr(type(x)))

    class Gen:

        def __iter__(self):
            return self

        def __next__(self):
            return None

        def close(self):
            pass

        def send(self, value):
            return value

        def throw(self, typ, val=None, tb=None):
            pass

    class MinimalGen(Generator):

        def send(self, value):
            return value

        def throw(self, typ, val=None, tb=None):
            super().throw(typ, val, tb)

    def gen():
        yield 1
    samples = [gen(), (lambda : (yield))(), Gen(), MinimalGen()]
    for x in samples:
        self.assertIsInstance(x, Iterator)
        self.assertIsInstance(x, Generator)
        self.assertTrue(issubclass(type(x), Generator), repr(type(x)))
    self.validate_abstract_methods(Generator, 'send', 'throw')
    mgen = MinimalGen()
    self.assertIs(mgen, iter(mgen))
    self.assertIs(mgen.send(None), next(mgen))
    self.assertEqual(2, mgen.send(2))
    self.assertIsNone(mgen.close())
    self.assertRaises(ValueError, mgen.throw, ValueError)
    self.assertRaisesRegex(ValueError, '^huhu$', mgen.throw, ValueError, ValueError('huhu'))
    self.assertRaises(StopIteration, mgen.throw, StopIteration())

    class FailOnClose(Generator):

        def send(self, value):
            return value

        def throw(self, *args):
            raise ValueError
    self.assertRaises(ValueError, FailOnClose().close)

    class IgnoreGeneratorExit(Generator):

        def send(self, value):
            return value

        def throw(self, *args):
            pass
    self.assertRaises(RuntimeError, IgnoreGeneratorExit().close)
