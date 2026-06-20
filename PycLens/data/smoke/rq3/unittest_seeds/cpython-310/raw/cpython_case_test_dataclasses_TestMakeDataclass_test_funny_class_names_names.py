# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_funny_class_names_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for classname in ['()', 'x,y', '*', '2@3', '']:
        with self.subTest(classname=classname):
            C = make_dataclass(classname, ['a', 'b'])
            self.assertEqual(C.__name__, classname)
