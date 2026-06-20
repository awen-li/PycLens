# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_duplicate_field_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for field in ['a', 'ab']:
        with self.subTest(field=field):
            with self.assertRaisesRegex(TypeError, 'Field name duplicated'):
                make_dataclass('C', [field, 'a', field])
