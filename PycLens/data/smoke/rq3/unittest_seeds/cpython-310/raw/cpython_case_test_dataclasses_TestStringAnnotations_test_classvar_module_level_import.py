# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestStringAnnotations_test_classvar_module_level_import

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test import dataclass_module_1
    from test import dataclass_module_1_str
    from test import dataclass_module_2
    from test import dataclass_module_2_str
    for m in (dataclass_module_1, dataclass_module_1_str, dataclass_module_2, dataclass_module_2_str):
        with self.subTest(m=m):
            if m.USING_STRINGS:
                c = m.CV(10)
            else:
                c = m.CV()
            self.assertEqual(c.cv0, 20)
            c = m.IV(0, 1, 2, 3, 4)
            for field_name in ('iv0', 'iv1', 'iv2', 'iv3'):
                with self.subTest(field_name=field_name):
                    with self.assertRaisesRegex(AttributeError, f"object has no attribute '{field_name}'"):
                        getattr(c, field_name)
            if m.USING_STRINGS:
                self.assertIn('not_iv4', c.__dict__)
                self.assertEqual(c.not_iv4, 4)
            else:
                self.assertNotIn('not_iv4', c.__dict__)
