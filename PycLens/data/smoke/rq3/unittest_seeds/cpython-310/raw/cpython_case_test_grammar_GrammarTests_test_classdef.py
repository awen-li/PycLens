# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_classdef

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B:
        pass

    class B2:
        pass

    class C1(B):
        pass

    class C2(B):
        pass

    class D(C1, C2, B):
        pass

    class C:

        def meth1(self):
            pass

        def meth2(self, arg):
            pass

        def meth3(self, a1, a2):
            pass

    def class_decorator(x):
        return x

    @class_decorator
    class G:
        pass

    @False or class_decorator
    class H:
        pass

    @(d := class_decorator)
    class I:
        pass

    @lambda c: class_decorator(c)
    class J:
        pass

    @[..., class_decorator, ...][1]
    class K:
        pass

    @class_decorator(class_decorator)(class_decorator)
    class L:
        pass

    @[class_decorator][0].__call__.__call__
    class M:
        pass
