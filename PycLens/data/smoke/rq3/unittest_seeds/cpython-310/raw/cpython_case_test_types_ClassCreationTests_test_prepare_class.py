# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_prepare_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_ns = {}

    class A(type):

        def __new__(*args, **kwargs):
            return type.__new__(*args, **kwargs)

        def __prepare__(*args):
            return expected_ns
    B = types.new_class('B', (object,))
    C = types.new_class('C', (object,), {'metaclass': A})
    (meta, ns, kwds) = types.prepare_class('D', (B, C), {'metaclass': type})
    self.assertIs(meta, A)
    self.assertIs(ns, expected_ns)
    self.assertEqual(len(kwds), 0)
