# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_class_marker

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: str = field(init=False, default=None)
        z: str = field(repr=False)
    the_fields = fields(C)
    self.assertIsInstance(the_fields, tuple)
    for f in the_fields:
        self.assertIs(type(f), Field)
        self.assertIn(f.name, C.__annotations__)
    self.assertEqual(len(the_fields), 3)
    self.assertEqual(the_fields[0].name, 'x')
    self.assertEqual(the_fields[0].type, int)
    self.assertFalse(hasattr(C, 'x'))
    self.assertTrue(the_fields[0].init)
    self.assertTrue(the_fields[0].repr)
    self.assertEqual(the_fields[1].name, 'y')
    self.assertEqual(the_fields[1].type, str)
    self.assertIsNone(getattr(C, 'y'))
    self.assertFalse(the_fields[1].init)
    self.assertTrue(the_fields[1].repr)
    self.assertEqual(the_fields[2].name, 'z')
    self.assertEqual(the_fields[2].type, str)
    self.assertFalse(hasattr(C, 'z'))
    self.assertTrue(the_fields[2].init)
    self.assertFalse(the_fields[2].repr)
