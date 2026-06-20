# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_special_method_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def run_context(manager):
        with manager:
            pass

    def iden(self):
        return self

    def hello(self):
        return b'hello'

    def empty_seq(self):
        return []

    def zero(self):
        return 0

    def complex_num(self):
        return 1j

    def stop(self):
        raise StopIteration

    def return_true(self, thing=None):
        return True

    def do_isinstance(obj):
        return isinstance(int, obj)

    def do_issubclass(obj):
        return issubclass(int, obj)

    def do_dict_missing(checker):

        class DictSub(checker.__class__, dict):
            pass
        self.assertEqual(DictSub()['hi'], 4)

    def some_number(self_, key):
        self.assertEqual(key, 'hi')
        return 4

    def swallow(*args):
        pass

    def format_impl(self, spec):
        return 'hello'
    specials = [('__bytes__', bytes, hello, set(), {}), ('__reversed__', reversed, empty_seq, set(), {}), ('__length_hint__', list, zero, set(), {'__iter__': iden, '__next__': stop}), ('__sizeof__', sys.getsizeof, zero, set(), {}), ('__instancecheck__', do_isinstance, return_true, set(), {}), ('__missing__', do_dict_missing, some_number, set(('__class__',)), {}), ('__subclasscheck__', do_issubclass, return_true, set(('__bases__',)), {}), ('__enter__', run_context, iden, set(), {'__exit__': swallow}), ('__exit__', run_context, swallow, set(), {'__enter__': iden}), ('__complex__', complex, complex_num, set(), {}), ('__format__', format, format_impl, set(), {}), ('__floor__', math.floor, zero, set(), {}), ('__trunc__', math.trunc, zero, set(), {}), ('__trunc__', int, zero, set(), {}), ('__ceil__', math.ceil, zero, set(), {}), ('__dir__', dir, empty_seq, set(), {}), ('__round__', round, zero, set(), {})]

    class Checker(object):

        def __getattr__(self, attr, test=self):
            test.fail('__getattr__ called with {0}'.format(attr))

        def __getattribute__(self, attr, test=self):
            if attr not in ok:
                test.fail('__getattribute__ called with {0}'.format(attr))
            return object.__getattribute__(self, attr)

    class SpecialDescr(object):

        def __init__(self, impl):
            self.impl = impl

        def __get__(self, obj, owner):
            record.append(1)
            return self.impl.__get__(obj, owner)

    class MyException(Exception):
        pass

    class ErrDescr(object):

        def __get__(self, obj, owner):
            raise MyException
    for (name, runner, meth_impl, ok, env) in specials:

        class X(Checker):
            pass
        for (attr, obj) in env.items():
            setattr(X, attr, obj)
        setattr(X, name, meth_impl)
        runner(X())
        record = []

        class X(Checker):
            pass
        for (attr, obj) in env.items():
            setattr(X, attr, obj)
        setattr(X, name, SpecialDescr(meth_impl))
        runner(X())
        self.assertEqual(record, [1], name)

        class X(Checker):
            pass
        for (attr, obj) in env.items():
            setattr(X, attr, obj)
        setattr(X, name, ErrDescr())
        self.assertRaises(MyException, runner, X())
