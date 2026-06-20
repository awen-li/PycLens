# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_metadata_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        i: int
    self.assertFalse(fields(C)[0].metadata)
    self.assertEqual(len(fields(C)[0].metadata), 0)
    with self.assertRaisesRegex(TypeError, 'does not support item assignment'):
        fields(C)[0].metadata['test'] = 3
