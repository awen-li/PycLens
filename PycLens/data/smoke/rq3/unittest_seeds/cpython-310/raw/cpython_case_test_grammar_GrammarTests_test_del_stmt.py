# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_del_stmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    abc = [1, 2, 3]
    (x, y, z) = abc
    xyz = (x, y, z)
    del abc
    del x, y, (z, xyz)
    (x, y, z) = 'xyz'
    del x
    del y
    del z
    del ()
    (a, b, c, d, e, f, g) = 'abcdefg'
    del a, (b, c), (d, (e, f))
    (a, b, c, d, e, f, g) = 'abcdefg'
    del a, [b, c], (d, [e, f])
    abcd = list('abcd')
    del abcd[1:2]
    compile('del a, (b[0].c, (d.e, f.g[1:2])), [h.i.j], ()', '<testcase>', 'exec')
