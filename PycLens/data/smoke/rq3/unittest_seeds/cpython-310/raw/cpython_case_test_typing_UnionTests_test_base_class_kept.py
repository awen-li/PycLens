# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_base_class_kept

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = Union[Employee, Manager]
    self.assertNotEqual(u, Employee)
    self.assertIn(Employee, u.__args__)
    self.assertIn(Manager, u.__args__)
