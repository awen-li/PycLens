# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_set_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        pass
    a = C()
    a.__dict__ = {'b': 1}
    self.assertEqual(a.b, 1)

    def cant(x, dict):
        try:
            x.__dict__ = dict
        except (AttributeError, TypeError):
            pass
        else:
            self.fail("shouldn't allow %r.__dict__ = %r" % (x, dict))
    cant(a, None)
    cant(a, [])
    cant(a, 1)
    del a.__dict__

    class Base(object):
        pass

    def verify_dict_readonly(x):
        """
            x has to be an instance of a class inheriting from Base.
            """
        cant(x, {})
        try:
            del x.__dict__
        except (AttributeError, TypeError):
            pass
        else:
            self.fail("shouldn't allow del %r.__dict__" % x)
        dict_descr = Base.__dict__['__dict__']
        try:
            dict_descr.__set__(x, {})
        except (AttributeError, TypeError):
            pass
        else:
            self.fail("dict_descr allowed access to %r's dict" % x)

    class Meta1(type, Base):
        pass

    class Meta2(Base, type):
        pass

    class D(object, metaclass=Meta1):
        pass

    class E(object, metaclass=Meta2):
        pass
    for cls in (C, D, E):
        verify_dict_readonly(cls)
        class_dict = cls.__dict__
        try:
            class_dict['spam'] = 'eggs'
        except TypeError:
            pass
        else:
            self.fail("%r's __dict__ can be modified" % cls)

    class Module1(types.ModuleType, Base):
        pass

    class Module2(Base, types.ModuleType):
        pass
    for ModuleType in (Module1, Module2):
        mod = ModuleType('spam')
        verify_dict_readonly(mod)
        mod.__dict__['spam'] = 'eggs'

    def can_delete_dict(e):
        try:
            del e.__dict__
        except (TypeError, AttributeError):
            return False
        else:
            return True

    class Exception1(Exception, Base):
        pass

    class Exception2(Base, Exception):
        pass
    for ExceptionType in (Exception, Exception1, Exception2):
        e = ExceptionType()
        e.__dict__ = {'a': 1}
        self.assertEqual(e.a, 1)
        self.assertEqual(can_delete_dict(e), can_delete_dict(ValueError()))
