# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestDescriptors_test_lookup_on_instance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class D:
        pass
    d = D()
    d.__set_name__ = Mock()

    @dataclass
    class C:
        i: int = field(default=d, init=False)
    self.assertEqual(d.__set_name__.call_count, 0)
