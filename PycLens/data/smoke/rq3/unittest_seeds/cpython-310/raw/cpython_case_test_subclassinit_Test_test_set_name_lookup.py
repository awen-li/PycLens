# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_set_name_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    resolved = []

    class NonDescriptor:

        def __getattr__(self, name):
            resolved.append(name)

    class A:
        d = NonDescriptor()
    self.assertNotIn('__set_name__', resolved, '__set_name__ is looked up in instance dict')
