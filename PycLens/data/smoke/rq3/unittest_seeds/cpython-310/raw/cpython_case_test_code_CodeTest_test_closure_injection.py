# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CodeTest_test_closure_injection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from types import FunctionType

    def create_closure(__class__):
        return (lambda : __class__).__closure__

    def new_code(c):
        """A new code object with a __class__ cell added to freevars"""
        return c.replace(co_freevars=c.co_freevars + ('__class__',))

    def add_foreign_method(cls, name, f):
        code = new_code(f.__code__)
        assert not f.__closure__
        closure = create_closure(cls)
        defaults = f.__defaults__
        setattr(cls, name, FunctionType(code, globals(), name, defaults, closure))

    class List(list):
        pass
    add_foreign_method(List, '__getitem__', external_getitem)
    function = List.__getitem__
    class_ref = function.__closure__[0].cell_contents
    self.assertIs(class_ref, List)
    self.assertFalse(function.__code__.co_flags & inspect.CO_NOFREE, hex(function.__code__.co_flags))
    obj = List([1, 2, 3])
    self.assertEqual(obj[0], 'Foreign getitem: 1')
