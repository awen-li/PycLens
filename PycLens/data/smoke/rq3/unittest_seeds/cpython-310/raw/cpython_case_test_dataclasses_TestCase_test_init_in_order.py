# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_init_in_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        a: int
        b: int = field()
        c: list = field(default_factory=list, init=False)
        d: list = field(default_factory=list)
        e: int = field(default=4, init=False)
        f: int = 4
    calls = []

    def setattr(self, name, value):
        calls.append((name, value))
    C.__setattr__ = setattr
    c = C(0, 1)
    self.assertEqual(('a', 0), calls[0])
    self.assertEqual(('b', 1), calls[1])
    self.assertEqual(('c', []), calls[2])
    self.assertEqual(('d', []), calls[3])
    self.assertNotIn(('e', 4), calls)
    self.assertEqual(('f', 4), calls[4])
