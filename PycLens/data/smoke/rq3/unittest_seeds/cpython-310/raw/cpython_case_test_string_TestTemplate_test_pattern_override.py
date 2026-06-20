# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_pattern_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyPattern(Template):
        pattern = '\n            (?P<escaped>@{2})                   |\n            @(?P<named>[_a-z][._a-z0-9]*)       |\n            @{(?P<braced>[_a-z][._a-z0-9]*)}    |\n            (?P<invalid>@)\n            '
    m = Mapping()
    m.bag = Bag()
    m.bag.foo = Bag()
    m.bag.foo.who = 'tim'
    m.bag.what = 'ham'
    s = MyPattern('@bag.foo.who likes to eat a bag of @bag.what')
    self.assertEqual(s.substitute(m), 'tim likes to eat a bag of ham')

    class BadPattern(Template):
        pattern = '\n            (?P<badname>.*)                     |\n            (?P<escaped>@{2})                   |\n            @(?P<named>[_a-z][._a-z0-9]*)       |\n            @{(?P<braced>[_a-z][._a-z0-9]*)}    |\n            (?P<invalid>@)                      |\n            '
    s = BadPattern('@bag.foo.who likes to eat a bag of @bag.what')
    self.assertRaises(ValueError, s.substitute, {})
    self.assertRaises(ValueError, s.safe_substitute, {})
