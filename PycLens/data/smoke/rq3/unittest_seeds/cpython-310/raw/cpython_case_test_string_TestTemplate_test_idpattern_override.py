# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_idpattern_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class PathPattern(Template):
        idpattern = '[_a-z][._a-z0-9]*'
    m = Mapping()
    m.bag = Bag()
    m.bag.foo = Bag()
    m.bag.foo.who = 'tim'
    m.bag.what = 'ham'
    s = PathPattern('$bag.foo.who likes to eat a bag of $bag.what')
    self.assertEqual(s.substitute(m), 'tim likes to eat a bag of ham')
