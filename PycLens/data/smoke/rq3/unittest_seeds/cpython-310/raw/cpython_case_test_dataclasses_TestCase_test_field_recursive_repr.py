# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rec_field = field()
    rec_field.type = rec_field
    rec_field.name = 'id'
    repr_output = repr(rec_field)
    self.assertIn(',type=...,', repr_output)
