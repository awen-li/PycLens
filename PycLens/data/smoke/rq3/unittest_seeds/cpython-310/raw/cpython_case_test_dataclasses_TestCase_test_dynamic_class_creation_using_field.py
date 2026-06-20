# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_dynamic_class_creation_using_field

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cls_dict = {'__annotations__': {'x': int, 'y': int}, 'y': field(default=5)}
    cls = type('C', (), cls_dict)
    cls1 = dataclass(cls)
    self.assertEqual(cls1, cls)
    self.assertEqual(asdict(cls1(1)), {'x': 1, 'y': 5})
