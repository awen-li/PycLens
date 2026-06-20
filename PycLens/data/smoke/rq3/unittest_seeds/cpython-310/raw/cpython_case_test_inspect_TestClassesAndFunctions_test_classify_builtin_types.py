# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_classify_builtin_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in dir(__builtins__):
        builtin = getattr(__builtins__, name)
        if isinstance(builtin, type):
            inspect.classify_class_attrs(builtin)
    attrs = attrs_wo_objs(bool)
    self.assertIn(('__new__', 'static method', bool), attrs, 'missing __new__')
    self.assertIn(('from_bytes', 'class method', int), attrs, 'missing class method')
    self.assertIn(('to_bytes', 'method', int), attrs, 'missing plain method')
    self.assertIn(('__add__', 'method', int), attrs, 'missing plain method')
    self.assertIn(('__and__', 'method', bool), attrs, 'missing plain method')
