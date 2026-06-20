# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestDescriptors_test_getting_field_calls_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class D:
        pass
    D.__set__ = Mock()
    D.__get__ = Mock()

    @dataclass
    class C:
        i: D = D()
    c = C(5)
    D.__get__.reset_mock()
    value = c.i
    self.assertEqual(D.__get__.call_count, 1)
