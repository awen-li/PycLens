# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_non_identifier_field_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for field in ['()', 'x,y', '*', '2@3', '', 'little johnny tables']:
        with self.subTest(field=field):
            with self.assertRaisesRegex(TypeError, 'must be valid identifiers'):
                make_dataclass('C', ['a', field])
            with self.assertRaisesRegex(TypeError, 'must be valid identifiers'):
                make_dataclass('C', [field])
            with self.assertRaisesRegex(TypeError, 'must be valid identifiers'):
                make_dataclass('C', [field, 'a'])
