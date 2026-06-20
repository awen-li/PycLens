# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_assignment_idiom_in_comprehensions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def listcomp():
        return [y for x in a for y in [f(x)]]
    self.assertEqual(count_instr_recursively(listcomp, 'FOR_ITER'), 1)

    def setcomp():
        return {y for x in a for y in [f(x)]}
    self.assertEqual(count_instr_recursively(setcomp, 'FOR_ITER'), 1)

    def dictcomp():
        return {y: y for x in a for y in [f(x)]}
    self.assertEqual(count_instr_recursively(dictcomp, 'FOR_ITER'), 1)

    def genexpr():
        return (y for x in a for y in [f(x)])
    self.assertEqual(count_instr_recursively(genexpr, 'FOR_ITER'), 1)
