# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_mutable_bases_with_failing_mro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class WorkOnce(type):

        def __new__(self, name, bases, ns):
            self.flag = 0
            return super(WorkOnce, self).__new__(WorkOnce, name, bases, ns)

        def mro(self):
            if self.flag > 0:
                raise RuntimeError('bozo')
            else:
                self.flag += 1
                return type.mro(self)

    class WorkAlways(type):

        def mro(self):
            return type.mro(self)

    class C(object):
        pass

    class C2(object):
        pass

    class D(C):
        pass

    class E(D):
        pass

    class F(D, metaclass=WorkOnce):
        pass

    class G(D, metaclass=WorkAlways):
        pass
    E_mro_before = E.__mro__
    D_mro_before = D.__mro__
    try:
        D.__bases__ = (C2,)
    except RuntimeError:
        self.assertEqual(E.__mro__, E_mro_before)
        self.assertEqual(D.__mro__, D_mro_before)
    else:
        self.fail('exception not propagated')
