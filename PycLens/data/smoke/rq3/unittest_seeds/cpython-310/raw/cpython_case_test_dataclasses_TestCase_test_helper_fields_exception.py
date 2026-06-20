# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_fields_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'dataclass type or instance'):
        fields(0)

    class C:
        pass
    with self.assertRaisesRegex(TypeError, 'dataclass type or instance'):
        fields(C)
    with self.assertRaisesRegex(TypeError, 'dataclass type or instance'):
        fields(C())
