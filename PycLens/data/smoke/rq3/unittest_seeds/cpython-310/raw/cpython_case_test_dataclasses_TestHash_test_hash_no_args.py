# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestHash_test_hash_no_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Base:

        def __hash__(self):
            return 301
    for (frozen, eq, base, expected) in [(None, None, object, 'unhashable'), (None, None, Base, 'unhashable'), (None, False, object, 'object'), (None, False, Base, 'base'), (None, True, object, 'unhashable'), (None, True, Base, 'unhashable'), (False, None, object, 'unhashable'), (False, None, Base, 'unhashable'), (False, False, object, 'object'), (False, False, Base, 'base'), (False, True, object, 'unhashable'), (False, True, Base, 'unhashable'), (True, None, object, 'tuple'), (True, None, Base, 'tuple'), (True, False, object, 'object'), (True, False, Base, 'base'), (True, True, object, 'tuple'), (True, True, Base, 'tuple')]:
        with self.subTest(frozen=frozen, eq=eq, base=base, expected=expected):
            if frozen is None and eq is None:

                @dataclass
                class C(base):
                    i: int
            elif frozen is None:

                @dataclass(eq=eq)
                class C(base):
                    i: int
            elif eq is None:

                @dataclass(frozen=frozen)
                class C(base):
                    i: int
            else:

                @dataclass(frozen=frozen, eq=eq)
                class C(base):
                    i: int
            if expected == 'unhashable':
                c = C(10)
                with self.assertRaisesRegex(TypeError, 'unhashable type'):
                    hash(c)
            elif expected == 'base':
                self.assertEqual(hash(C(10)), 301)
            elif expected == 'object':
                self.assertIs(C.__hash__, object.__hash__)
            elif expected == 'tuple':
                self.assertEqual(hash(C(42)), hash((42,)))
            else:
                assert False, f'unknown value for expected={expected!r}'
