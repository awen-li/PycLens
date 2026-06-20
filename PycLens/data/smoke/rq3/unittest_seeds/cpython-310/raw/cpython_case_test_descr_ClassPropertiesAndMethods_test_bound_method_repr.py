# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_bound_method_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:

        def method(self):
            pass
    self.assertRegex(repr(Foo().method), '<bound method .*Foo\\.method of <.*Foo object at .*>>')

    class Base:

        def method(self):
            pass

    class Derived1(Base):
        pass

    class Derived2(Base):

        def method(self):
            pass
    base = Base()
    derived1 = Derived1()
    derived2 = Derived2()
    super_d2 = super(Derived2, derived2)
    self.assertRegex(repr(base.method), '<bound method .*Base\\.method of <.*Base object at .*>>')
    self.assertRegex(repr(derived1.method), '<bound method .*Base\\.method of <.*Derived1 object at .*>>')
    self.assertRegex(repr(derived2.method), '<bound method .*Derived2\\.method of <.*Derived2 object at .*>>')
    self.assertRegex(repr(super_d2.method), '<bound method .*Base\\.method of <.*Derived2 object at .*>>')

    class Foo:

        @classmethod
        def method(cls):
            pass
    foo = Foo()
    self.assertRegex(repr(foo.method), "<bound method .*Foo\\.method of <class '.*Foo'>>")
    self.assertRegex(repr(Foo.method), "<bound method .*Foo\\.method of <class '.*Foo'>>")

    class MyCallable:

        def __call__(self, arg):
            pass
    func = MyCallable()
    instance = object()
    method = types.MethodType(func, instance)
    self.assertRegex(repr(method), '<bound method \\? of <object object at .*>>')
    func.__name__ = 'name'
    self.assertRegex(repr(method), '<bound method name of <object object at .*>>')
    func.__qualname__ = 'qualname'
    self.assertRegex(repr(method), '<bound method qualname of <object object at .*>>')
