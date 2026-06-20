# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_items_in_dicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        a: int
        b: list = field(default_factory=list, init=False)
        c: list = field(default_factory=list)
        d: int = field(default=4, init=False)
        e: int = 0
    c = C(0)
    self.assertNotIn('a', C.__dict__)
    self.assertNotIn('b', C.__dict__)
    self.assertNotIn('c', C.__dict__)
    self.assertIn('d', C.__dict__)
    self.assertEqual(C.d, 4)
    self.assertIn('e', C.__dict__)
    self.assertEqual(C.e, 0)
    self.assertIn('a', c.__dict__)
    self.assertEqual(c.a, 0)
    self.assertIn('b', c.__dict__)
    self.assertEqual(c.b, [])
    self.assertIn('c', c.__dict__)
    self.assertEqual(c.c, [])
    self.assertNotIn('d', c.__dict__)
    self.assertIn('e', c.__dict__)
    self.assertEqual(c.e, 0)
