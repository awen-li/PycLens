# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_metaclass_semantics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CMeta(type):

        @classmethod
        def __prepare__(metacls, name, bases, **kwds):
            return {'__annotations__': CNS()}

    class CC(metaclass=CMeta):
        XX: 'ANNOT'
    self.assertEqual(CC.__annotations__['xx'], 'ANNOT')
