# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestTypeErrors_test_match_args_must_be_a_tuple_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Class:
        __match_args__ = ['spam', 'eggs']
        spam = 0
        eggs = 1
    x = Class()
    w = y = z = None
    with self.assertRaises(TypeError):
        match x:
            case Class(y, z):
                w = 0
    self.assertIs(w, None)
    self.assertIs(y, None)
    self.assertIs(z, None)
