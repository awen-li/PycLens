# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_invalid_type_specification

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for bad_field in [(), (1, 2, 3, 4)]:
        with self.subTest(bad_field=bad_field):
            with self.assertRaisesRegex(TypeError, 'Invalid field: '):
                make_dataclass('C', ['a', bad_field])
    for bad_field in [float, lambda x: x]:
        with self.subTest(bad_field=bad_field):
            with self.assertRaisesRegex(TypeError, 'has no len\\(\\)'):
                make_dataclass('C', ['a', bad_field])
