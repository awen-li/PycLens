# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_annotations_are_created_correctly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ann_module4 = import_helper.import_fresh_module('test.ann_module4')
    self.assertTrue('__annotations__' in ann_module4.__dict__)
    del ann_module4.__annotations__
    self.assertFalse('__annotations__' in ann_module4.__dict__)
