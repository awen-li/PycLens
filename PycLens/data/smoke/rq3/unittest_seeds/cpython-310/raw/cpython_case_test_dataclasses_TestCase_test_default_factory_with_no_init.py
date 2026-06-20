# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_default_factory_with_no_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    factory = Mock()

    @dataclass
    class C:
        x: list = field(default_factory=factory, init=False)
    C().x
    self.assertEqual(factory.call_count, 1)
    C().x
    self.assertEqual(factory.call_count, 2)
