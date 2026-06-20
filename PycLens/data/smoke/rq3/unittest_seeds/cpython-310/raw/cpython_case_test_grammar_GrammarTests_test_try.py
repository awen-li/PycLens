# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_try

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        1 / 0
    except ZeroDivisionError:
        pass
    else:
        pass
    try:
        1 / 0
    except EOFError:
        pass
    except TypeError as msg:
        pass
    except:
        pass
    else:
        pass
    try:
        1 / 0
    except (EOFError, TypeError, ZeroDivisionError):
        pass
    try:
        1 / 0
    except (EOFError, TypeError, ZeroDivisionError) as msg:
        pass
    try:
        pass
    finally:
        pass
    with self.assertRaises(SyntaxError):
        compile('try:\n    pass\nexcept Exception as a.b:\n    pass', '?', 'exec')
        compile('try:\n    pass\nexcept Exception as a[b]:\n    pass', '?', 'exec')
