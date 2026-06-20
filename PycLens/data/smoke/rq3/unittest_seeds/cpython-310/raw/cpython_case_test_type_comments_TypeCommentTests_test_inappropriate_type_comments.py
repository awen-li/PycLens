# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_type_comments.py
# case: TypeCommentTests_test_inappropriate_type_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_both_ways(source):
        ast.parse(source, type_comments=False)
        for tree in self.parse_all(source, maxver=0):
            pass
    check_both_ways('pass  # type: int\n')
    check_both_ways('foo()  # type: int\n')
    check_both_ways('x += 1  # type: int\n')
    check_both_ways('while True:  # type: int\n  continue\n')
    check_both_ways('while True:\n  continue  # type: int\n')
    check_both_ways('try:  # type: int\n  pass\nfinally:\n  pass\n')
    check_both_ways('try:\n  pass\nfinally:  # type: int\n  pass\n')
    check_both_ways('pass  # type: ignorewhatever\n')
    check_both_ways('pass  # type: ignoreé\n')
