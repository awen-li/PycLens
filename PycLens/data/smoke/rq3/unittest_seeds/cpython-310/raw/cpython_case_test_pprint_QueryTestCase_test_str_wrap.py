# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_str_wrap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fox = 'the quick brown fox jumped over a lazy dog'
    self.assertEqual(pprint.pformat(fox, width=19), "('the quick brown '\n 'fox jumped over '\n 'a lazy dog')")
    self.assertEqual(pprint.pformat({'a': 1, 'b': fox, 'c': 2}, width=25), "{'a': 1,\n 'b': 'the quick brown '\n      'fox jumped over '\n      'a lazy dog',\n 'c': 2}")
    special = 'Portons dix bons "whiskys"\nà l\'avocat goujat\t qui fumait au zoo'
    self.assertEqual(pprint.pformat(special, width=68), repr(special))
    self.assertEqual(pprint.pformat(special, width=31), '(\'Portons dix bons "whiskys"\\n\'\n "à l\'avocat goujat\\t qui "\n \'fumait au zoo\')')
    self.assertEqual(pprint.pformat(special, width=20), '(\'Portons dix bons \'\n \'"whiskys"\\n\'\n "à l\'avocat "\n \'goujat\\t qui \'\n \'fumait au zoo\')')
    self.assertEqual(pprint.pformat([[[[[special]]]]], width=35), '[[[[[\'Portons dix bons "whiskys"\\n\'\n     "à l\'avocat goujat\\t qui "\n     \'fumait au zoo\']]]]]')
    self.assertEqual(pprint.pformat([[[[[special]]]]], width=25), '[[[[[\'Portons dix bons \'\n     \'"whiskys"\\n\'\n     "à l\'avocat "\n     \'goujat\\t qui \'\n     \'fumait au zoo\']]]]]')
    self.assertEqual(pprint.pformat([[[[[special]]]]], width=23), '[[[[[\'Portons dix \'\n     \'bons "whiskys"\\n\'\n     "à l\'avocat "\n     \'goujat\\t qui \'\n     \'fumait au \'\n     \'zoo\']]]]]')
    unwrappable = 'x' * 100
    self.assertEqual(pprint.pformat(unwrappable, width=80), repr(unwrappable))
    self.assertEqual(pprint.pformat(''), "''")
    special *= 10
    for width in range(3, 40):
        formatted = pprint.pformat(special, width=width)
        self.assertEqual(eval(formatted), special)
        formatted = pprint.pformat([special] * 2, width=width)
        self.assertEqual(eval(formatted), [special] * 2)
