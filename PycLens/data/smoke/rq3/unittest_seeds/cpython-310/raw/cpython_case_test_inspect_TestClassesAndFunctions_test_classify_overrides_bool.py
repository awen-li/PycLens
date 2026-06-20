# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_classify_overrides_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NoBool(object):

        def __eq__(self, other):
            return NoBool()

        def __bool__(self):
            raise NotImplementedError('This object does not specify a boolean value')

    class HasNB(object):
        dd = NoBool()
    should_find_attr = inspect.Attribute('dd', 'data', HasNB, HasNB.dd)
    self.assertIn(should_find_attr, inspect.classify_class_attrs(HasNB))
