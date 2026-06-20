# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestDescriptors_test_init_calls_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class D:
        pass
    D.__set__ = Mock()

    @dataclass
    class C:
        i: D = D()
    D.__set__.reset_mock()
    c = C(5)
    self.assertEqual(D.__set__.call_count, 1)
