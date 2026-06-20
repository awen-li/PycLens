# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_module_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    log = []
    MT = type(sys)

    class MM(MT):

        def __init__(self, name):
            MT.__init__(self, name)

        def __getattribute__(self, name):
            log.append(('getattr', name))
            return MT.__getattribute__(self, name)

        def __setattr__(self, name, value):
            log.append(('setattr', name, value))
            MT.__setattr__(self, name, value)

        def __delattr__(self, name):
            log.append(('delattr', name))
            MT.__delattr__(self, name)
    a = MM('a')
    a.foo = 12
    x = a.foo
    del a.foo
    self.assertEqual(log, [('setattr', 'foo', 12), ('getattr', 'foo'), ('delattr', 'foo')])
    try:

        class Module(types.ModuleType, str):
            pass
    except TypeError:
        pass
    else:
        self.fail('inheriting from ModuleType and str at the same time should fail')

    def random_name():
        return ''.join(random.choices(string.ascii_letters, k=10))

    class A:
        pass
    subclasses = [type(random_name(), (A,), {}) for i in range(100)]
    self.assertEqual(A.__subclasses__(), subclasses)
