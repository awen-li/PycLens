# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_break_continue_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test_inner(extra_burning_oil=1, count=0):
        big_hippo = 2
        while big_hippo:
            count += 1
            try:
                if extra_burning_oil and big_hippo == 1:
                    extra_burning_oil -= 1
                    break
                big_hippo -= 1
                continue
            except:
                raise
        if count > 2 or big_hippo != 1:
            self.fail('continue then break in try/except in loop broken!')
    test_inner()
