# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_metadata_custom_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SimpleNameSpace:

        def __init__(self, **kw):
            self.__dict__.update(kw)

        def __getitem__(self, item):
            if item == 'xyzzy':
                return 'plugh'
            return getattr(self, item)

        def __len__(self):
            return self.__dict__.__len__()

    @dataclass
    class C:
        i: int = field(metadata=SimpleNameSpace(a=10))
    self.assertEqual(len(fields(C)[0].metadata), 1)
    self.assertEqual(fields(C)[0].metadata['a'], 10)
    with self.assertRaises(AttributeError):
        fields(C)[0].metadata['b']
    self.assertEqual(fields(C)[0].metadata['xyzzy'], 'plugh')
