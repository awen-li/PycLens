# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_hash_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class mydict(dict):
        pass
    d = mydict()
    try:
        hash(d)
    except TypeError:
        pass
    else:
        self.fail('hash() of dict subclass should fail')

    class mylist(list):
        pass
    d = mylist()
    try:
        hash(d)
    except TypeError:
        pass
    else:
        self.fail('hash() of list subclass should fail')
