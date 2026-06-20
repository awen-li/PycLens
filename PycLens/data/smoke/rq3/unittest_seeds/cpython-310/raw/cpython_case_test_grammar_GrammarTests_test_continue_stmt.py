# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_continue_stmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = 1
    while i:
        i = 0
        continue
    msg = ''
    while not msg:
        msg = 'ok'
        try:
            continue
            msg = 'continue failed to continue inside try'
        except:
            msg = 'continue inside try called except block'
    if msg != 'ok':
        self.fail(msg)
    msg = ''
    while not msg:
        msg = 'finally block not called'
        try:
            continue
        finally:
            msg = 'ok'
    if msg != 'ok':
        self.fail(msg)
