# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_deliberately_mutable_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Mutable:

        def __init__(self):
            self.l = []

    @dataclass
    class C:
        x: Mutable
    lst = Mutable()
    o1 = C(lst)
    o2 = C(lst)
    self.assertEqual(o1, o2)
    o1.x.l.extend([1, 2])
    self.assertEqual(o1, o2)
    self.assertEqual(o1.x.l, [1, 2])
    self.assertIs(o1.x, o2.x)
