# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_metadata_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):

        @dataclass
        class C:
            i: int = field(metadata=0)
    d = {}

    @dataclass
    class C:
        i: int = field(metadata=d)
    self.assertFalse(fields(C)[0].metadata)
    self.assertEqual(len(fields(C)[0].metadata), 0)
    d['foo'] = 1
    self.assertEqual(len(fields(C)[0].metadata), 1)
    self.assertEqual(fields(C)[0].metadata['foo'], 1)
    with self.assertRaisesRegex(TypeError, 'does not support item assignment'):
        fields(C)[0].metadata['test'] = 3
    d = {'test': 10, 'bar': '42', 3: 'three'}

    @dataclass
    class C:
        i: int = field(metadata=d)
    self.assertEqual(len(fields(C)[0].metadata), 3)
    self.assertEqual(fields(C)[0].metadata['test'], 10)
    self.assertEqual(fields(C)[0].metadata['bar'], '42')
    self.assertEqual(fields(C)[0].metadata[3], 'three')
    d['foo'] = 1
    self.assertEqual(len(fields(C)[0].metadata), 4)
    self.assertEqual(fields(C)[0].metadata['foo'], 1)
    with self.assertRaises(KeyError):
        fields(C)[0].metadata['baz']
    with self.assertRaisesRegex(TypeError, 'does not support item assignment'):
        fields(C)[0].metadata['test'] = 3
