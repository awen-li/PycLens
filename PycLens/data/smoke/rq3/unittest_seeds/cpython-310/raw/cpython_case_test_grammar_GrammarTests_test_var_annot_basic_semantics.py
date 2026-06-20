# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_basic_semantics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ZeroDivisionError):
        no_name[does_not_exist]: no_name_again = 1 / 0
    with self.assertRaises(NameError):
        no_name[does_not_exist]: 1 / 0 = 0
    global var_annot_global

    def f():
        st: str = 'Hello'
        a.b: int = (1, 2)
        return st
    self.assertEqual(f.__annotations__, {})

    def f_OK():
        x: 1 / 0
    f_OK()

    def fbad():
        x: int
        print(x)
    with self.assertRaises(UnboundLocalError):
        fbad()

    def f2bad():
        (no_such_global): int
        print(no_such_global)
    try:
        f2bad()
    except Exception as e:
        self.assertIs(type(e), NameError)

    class C:
        __foo: int
        s: str = 'attr'
        z = 2

        def __init__(self, x):
            self.x: int = x
    self.assertEqual(C.__annotations__, {'_C__foo': int, 's': str})
    with self.assertRaises(NameError):

        class CBad:
            no_such_name_defined.attr: int = 0
    with self.assertRaises(NameError):

        class Cbad2(C):
            x: int
            x.y: list = []
