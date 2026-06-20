# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestPEP590_test_vectorcall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    calls = [(len, (range(42),), {}, 42), (list.append, ([], 0), {}, None), ([].append, (0,), {}, None), (sum, ([36],), {'start': 6}, 42), (testfunction, (42,), {}, 42), (testfunction_kw, (42,), {'kw': None}, 42), (_testcapi.MethodDescriptorBase(), (0,), {}, True), (_testcapi.MethodDescriptorDerived(), (0,), {}, True), (_testcapi.MethodDescriptor2(), (0,), {}, False)]
    from _testcapi import pyobject_vectorcall, pyvectorcall_call
    from types import MethodType
    from functools import partial

    def vectorcall(func, args, kwargs):
        args = (*args, *kwargs.values())
        kwnames = tuple(kwargs)
        return pyobject_vectorcall(func, args, kwnames)
    for (func, args, kwargs, expected) in calls:
        with self.subTest(str(func)):
            if not kwargs:
                self.assertEqual(expected, pyvectorcall_call(func, args))
            self.assertEqual(expected, pyvectorcall_call(func, args, kwargs))

    class MethodDescriptorHeap(_testcapi.MethodDescriptorBase):
        pass

    class MethodDescriptorOverridden(_testcapi.MethodDescriptorBase):

        def __call__(self, n):
            return 'new'

    class SuperBase:

        def __call__(self, *args):
            return super().__call__(*args)

    class MethodDescriptorSuper(SuperBase, _testcapi.MethodDescriptorBase):

        def __call__(self, *args):
            return super().__call__(*args)
    calls += [(dict.update, ({},), {'key': True}, None), ({}.update, ({},), {'key': True}, None), (MethodDescriptorHeap(), (0,), {}, True), (MethodDescriptorOverridden(), (0,), {}, 'new'), (MethodDescriptorSuper(), (0,), {}, True)]
    for (func, args, kwargs, expected) in calls:
        with self.subTest(str(func)):
            args1 = args[1:]
            meth = MethodType(func, args[0])
            wrapped = partial(func)
            if not kwargs:
                self.assertEqual(expected, func(*args))
                self.assertEqual(expected, pyobject_vectorcall(func, args, None))
                self.assertEqual(expected, meth(*args1))
                self.assertEqual(expected, wrapped(*args))
            self.assertEqual(expected, func(*args, **kwargs))
            self.assertEqual(expected, vectorcall(func, args, kwargs))
            self.assertEqual(expected, meth(*args1, **kwargs))
            self.assertEqual(expected, wrapped(*args, **kwargs))
