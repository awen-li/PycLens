# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_empty_namedtuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NT = NamedTuple('NT')

    class CNT(NamedTuple):
        pass
    for struct in [NT, CNT]:
        with self.subTest(struct=struct):
            self.assertEqual(struct._fields, ())
            self.assertEqual(struct._field_defaults, {})
            self.assertEqual(struct.__annotations__, {})
            self.assertIsInstance(struct(), struct)
