# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_no_mutate_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {}
    C = make_dataclass('C', [('x', int), ('y', int, field(default=5))], namespace=ns)
    self.assertEqual(ns, {})
