# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_width

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = "[[[[[[1, 2, 3],\n     '1 2']]]],\n {1: [1, 2, 3],\n  2: [12, 34]},\n 'abc def ghi',\n ('ab cd ef',),\n set2({1, 23}),\n [[[[[1, 2, 3],\n     '1 2']]]]]"
    o = eval(expected)
    self.assertEqual(pprint.pformat(o, width=15), expected)
    self.assertEqual(pprint.pformat(o, width=16), expected)
    self.assertEqual(pprint.pformat(o, width=25), expected)
    self.assertEqual(pprint.pformat(o, width=14), "[[[[[[1,\n      2,\n      3],\n     '1 '\n     '2']]]],\n {1: [1,\n      2,\n      3],\n  2: [12,\n      34]},\n 'abc def '\n 'ghi',\n ('ab cd '\n  'ef',),\n set2({1,\n       23}),\n [[[[[1,\n      2,\n      3],\n     '1 '\n     '2']]]]]")
