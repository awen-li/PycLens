# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_default_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: list = field(default_factory=list)
    c0 = C(3)
    c1 = C(3)
    self.assertEqual(c0.x, 3)
    self.assertEqual(c0.y, [])
    self.assertEqual(c0, c1)
    self.assertIsNot(c0.y, c1.y)
    self.assertEqual(astuple(C(5, [1])), (5, [1]))
    l = []

    @dataclass
    class C:
        x: int
        y: list = field(default_factory=lambda : l)
    c0 = C(3)
    c1 = C(3)
    self.assertEqual(c0.x, 3)
    self.assertEqual(c0.y, [])
    self.assertEqual(c0, c1)
    self.assertIs(c0.y, c1.y)
    self.assertEqual(astuple(C(5, [1])), (5, [1]))

    @dataclass
    class C:
        x: list = field(default_factory=list, repr=False)
    self.assertEqual(repr(C()), 'TestCase.test_default_factory.<locals>.C()')
    self.assertEqual(C().x, [])

    @dataclass(unsafe_hash=True)
    class C:
        x: list = field(default_factory=list, hash=False)
    self.assertEqual(astuple(C()), ([],))
    self.assertEqual(hash(C()), hash(()))

    @dataclass
    class C:
        x: list = field(default_factory=list, init=False)
    self.assertEqual(astuple(C()), ([],))

    @dataclass
    class C:
        x: list = field(default_factory=list, compare=False)
    self.assertEqual(C(), C([1]))
