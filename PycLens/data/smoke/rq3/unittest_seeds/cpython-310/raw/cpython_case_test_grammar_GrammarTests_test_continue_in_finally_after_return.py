# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_continue_in_finally_after_return

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g1(x):
        count = 0
        while count < 100:
            count += 1
            try:
                return count
            finally:
                if x:
                    continue
        return ('end', count)
    self.assertEqual(g1(False), 1)
    self.assertEqual(g1(True), ('end', 100))

    def g2(x):
        for count in [0, 1]:
            try:
                return count
            finally:
                if x:
                    continue
        return ('end', count)
    self.assertEqual(g2(False), 0)
    self.assertEqual(g2(True), ('end', 1))
