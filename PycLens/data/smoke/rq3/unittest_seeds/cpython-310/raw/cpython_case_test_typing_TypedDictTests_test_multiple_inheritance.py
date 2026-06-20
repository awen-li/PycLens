# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_multiple_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class One(TypedDict):
        one: int

    class Two(TypedDict):
        two: str

    class Untotal(TypedDict, total=False):
        untotal: str
    Inline = TypedDict('Inline', {'inline': bool})

    class Regular:
        pass

    class Child(One, Two):
        child: bool
    self.assertEqual(Child.__required_keys__, frozenset(['one', 'two', 'child']))
    self.assertEqual(Child.__optional_keys__, frozenset([]))
    self.assertEqual(Child.__annotations__, {'one': int, 'two': str, 'child': bool})

    class ChildWithOptional(One, Untotal):
        child: bool
    self.assertEqual(ChildWithOptional.__required_keys__, frozenset(['one', 'child']))
    self.assertEqual(ChildWithOptional.__optional_keys__, frozenset(['untotal']))
    self.assertEqual(ChildWithOptional.__annotations__, {'one': int, 'untotal': str, 'child': bool})

    class ChildWithTotalFalse(One, Untotal, total=False):
        child: bool
    self.assertEqual(ChildWithTotalFalse.__required_keys__, frozenset(['one']))
    self.assertEqual(ChildWithTotalFalse.__optional_keys__, frozenset(['untotal', 'child']))
    self.assertEqual(ChildWithTotalFalse.__annotations__, {'one': int, 'untotal': str, 'child': bool})

    class ChildWithInlineAndOptional(Untotal, Inline):
        child: bool
    self.assertEqual(ChildWithInlineAndOptional.__required_keys__, frozenset(['inline', 'child']))
    self.assertEqual(ChildWithInlineAndOptional.__optional_keys__, frozenset(['untotal']))
    self.assertEqual(ChildWithInlineAndOptional.__annotations__, {'inline': bool, 'untotal': str, 'child': bool})
    wrong_bases = [(One, Regular), (Regular, One), (One, Two, Regular), (Inline, Regular), (Untotal, Regular)]
    for bases in wrong_bases:
        with self.subTest(bases=bases):
            with self.assertRaisesRegex(TypeError, 'cannot inherit from both a TypedDict type and a non-TypedDict'):

                class Wrong(*bases):
                    pass
