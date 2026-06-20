# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_named_self

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        self: str
    c = C('foo')
    self.assertEqual(c.self, 'foo')
    sig = inspect.signature(C.__init__)
    first = next(iter(sig.parameters))
    self.assertNotEqual('self', first)

    @dataclass
    class C:
        selfx: str
    sig = inspect.signature(C.__init__)
    first = next(iter(sig.parameters))
    self.assertEqual('self', first)
