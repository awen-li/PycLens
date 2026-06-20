# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_consts_in_conditionals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def and_true(x):
        return True and x

    def and_false(x):
        return False and x

    def or_true(x):
        return True or x

    def or_false(x):
        return False or x
    funcs = [and_true, and_false, or_true, or_false]
    for func in funcs:
        with self.subTest(func=func):
            opcodes = list(dis.get_instructions(func))
            self.assertEqual(2, len(opcodes))
            self.assertIn('LOAD_', opcodes[0].opname)
            self.assertEqual('RETURN_VALUE', opcodes[1].opname)
