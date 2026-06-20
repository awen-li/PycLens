# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: DictProxyTests_test_dict_type_with_metaclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B(object):
        pass

    class M(type):
        pass

    class C(metaclass=M):
        pass
    self.assertEqual(type(C.__dict__), type(B.__dict__))
