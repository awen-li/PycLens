# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_break_in_finally_after_return

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g1(x):
        for count in [0, 1]:
            count2 = 0
            while count2 < 20:
                count2 += 10
                try:
                    return count + count2
                finally:
                    if x:
                        break
        return ('end', count, count2)
    self.assertEqual(g1(False), 10)
    self.assertEqual(g1(True), ('end', 1, 10))

    def g2(x):
        for count in [0, 1]:
            for count2 in [10, 20]:
                try:
                    return count + count2
                finally:
                    if x:
                        break
        return ('end', count, count2)
    self.assertEqual(g2(False), 10)
    self.assertEqual(g2(True), ('end', 1, 10))
