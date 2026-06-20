# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getmembers_VirtualAttribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(type):

        def __getattr__(cls, name):
            if name == 'eggs':
                return 'scrambled'
            return super().__getattr__(name)

    class A(metaclass=M):

        @types.DynamicClassAttribute
        def eggs(self):
            return 'spam'
    self.assertIn(('eggs', 'scrambled'), inspect.getmembers(A))
    self.assertIn(('eggs', 'spam'), inspect.getmembers(A()))
