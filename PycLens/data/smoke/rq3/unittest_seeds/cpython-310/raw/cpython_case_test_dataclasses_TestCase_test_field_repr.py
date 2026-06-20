# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    int_field = field(default=1, init=True, repr=False)
    int_field.name = 'id'
    repr_output = repr(int_field)
    expected_output = f"Field(name='id',type=None,default=1,default_factory={MISSING!r},init=True,repr=False,hash=None,compare=True,metadata=mappingproxy({{}}),kw_only={MISSING!r},_field_type=None)"
    self.assertEqual(repr_output, expected_output)
