# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_builtin_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    builtin_types = [tp for tp in builtins.__dict__.values() if isinstance(tp, type)]
    for tp in builtin_types:
        object.__getattribute__(tp, '__bases__')
        if tp is not object:
            self.assertEqual(len(tp.__bases__), 1, tp)

    class L(list):
        pass

    class C(object):
        pass

    class D(C):
        pass
    try:
        L.__bases__ = (dict,)
    except TypeError:
        pass
    else:
        self.fail("shouldn't turn list subclass into dict subclass")
    try:
        list.__bases__ = (dict,)
    except TypeError:
        pass
    else:
        self.fail("shouldn't be able to assign to list.__bases__")
    try:
        D.__bases__ = (C, list)
    except TypeError:
        pass
    else:
        self.fail('best_base calculation found wanting')
