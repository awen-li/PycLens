# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_warn_missed_comma

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(test):
        self.check_syntax_warning(test, msg)
    msg = 'is not callable; perhaps you missed a comma\\?'
    check('[(1, 2) (3, 4)]')
    check('[(x, y) (3, 4)]')
    check('[[1, 2] (3, 4)]')
    check('[{1, 2} (3, 4)]')
    check('[{1: 2} (3, 4)]')
    check('[[i for i in range(5)] (3, 4)]')
    check('[{i for i in range(5)} (3, 4)]')
    check('[(i for i in range(5)) (3, 4)]')
    check('[{i: i for i in range(5)} (3, 4)]')
    check('[f"{x}" (3, 4)]')
    check('[f"x={x}" (3, 4)]')
    check('["abc" (3, 4)]')
    check('[b"abc" (3, 4)]')
    check('[123 (3, 4)]')
    check('[12.3 (3, 4)]')
    check('[12.3j (3, 4)]')
    check('[None (3, 4)]')
    check('[True (3, 4)]')
    check('[... (3, 4)]')
    msg = 'is not subscriptable; perhaps you missed a comma\\?'
    check('[{1, 2} [i, j]]')
    check('[{i for i in range(5)} [i, j]]')
    check('[(i for i in range(5)) [i, j]]')
    check('[(lambda x, y: x) [i, j]]')
    check('[123 [i, j]]')
    check('[12.3 [i, j]]')
    check('[12.3j [i, j]]')
    check('[None [i, j]]')
    check('[True [i, j]]')
    check('[... [i, j]]')
    msg = 'indices must be integers or slices, not tuple; perhaps you missed a comma\\?'
    check('[(1, 2) [i, j]]')
    check('[(x, y) [i, j]]')
    check('[[1, 2] [i, j]]')
    check('[[i for i in range(5)] [i, j]]')
    check('[f"{x}" [i, j]]')
    check('[f"x={x}" [i, j]]')
    check('["abc" [i, j]]')
    check('[b"abc" [i, j]]')
    msg = 'indices must be integers or slices, not tuple;'
    check('[[1, 2] [3, 4]]')
    msg = 'indices must be integers or slices, not list;'
    check('[[1, 2] [[3, 4]]]')
    check('[[1, 2] [[i for i in range(5)]]]')
    msg = 'indices must be integers or slices, not set;'
    check('[[1, 2] [{3, 4}]]')
    check('[[1, 2] [{i for i in range(5)}]]')
    msg = 'indices must be integers or slices, not dict;'
    check('[[1, 2] [{3: 4}]]')
    check('[[1, 2] [{i: i for i in range(5)}]]')
    msg = 'indices must be integers or slices, not generator;'
    check('[[1, 2] [(i for i in range(5))]]')
    msg = 'indices must be integers or slices, not function;'
    check('[[1, 2] [(lambda x, y: x)]]')
    msg = 'indices must be integers or slices, not str;'
    check('[[1, 2] [f"{x}"]]')
    check('[[1, 2] [f"x={x}"]]')
    check('[[1, 2] ["abc"]]')
    msg = 'indices must be integers or slices, not'
    check('[[1, 2] [b"abc"]]')
    check('[[1, 2] [12.3]]')
    check('[[1, 2] [12.3j]]')
    check('[[1, 2] [None]]')
    check('[[1, 2] [...]]')
    with warnings.catch_warnings():
        warnings.simplefilter('error', SyntaxWarning)
        compile('[(lambda x, y: x) (3, 4)]', '<testcase>', 'exec')
        compile('[[1, 2] [i]]', '<testcase>', 'exec')
        compile('[[1, 2] [0]]', '<testcase>', 'exec')
        compile('[[1, 2] [True]]', '<testcase>', 'exec')
        compile('[[1, 2] [1:2]]', '<testcase>', 'exec')
        compile('[{(1, 2): 3} [i, j]]', '<testcase>', 'exec')
