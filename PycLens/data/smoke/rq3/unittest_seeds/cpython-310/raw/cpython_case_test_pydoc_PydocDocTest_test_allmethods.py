# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_allmethods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestClass(object):

        def method_returning_true(self):
            return True
    expected = dict(vars(object))
    expected['method_returning_true'] = TestClass.method_returning_true
    del expected['__doc__']
    del expected['__class__']
    expected['__subclasshook__'] = TestClass.__subclasshook__
    expected['__init_subclass__'] = TestClass.__init_subclass__
    methods = pydoc.allmethods(TestClass)
    self.assertDictEqual(methods, expected)
