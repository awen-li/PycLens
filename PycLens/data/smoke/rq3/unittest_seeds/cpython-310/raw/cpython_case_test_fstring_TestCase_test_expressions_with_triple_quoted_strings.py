# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_expressions_with_triple_quoted_strings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(f"{'x'}", 'x')
    self.assertEqual(f"""{"eric's"}""", "eric's")
    self.assertEqual(f"""{'xeric"sy'}""", 'xeric"sy')
    self.assertEqual(f"""{'xeric"s'}""", 'xeric"s')
    self.assertEqual(f"""{'eric"sy'}""", 'eric"sy')
    self.assertEqual(f"""{'xeric"sy'}""", 'xeric"sy')
    self.assertEqual(f"""{'xeric"sy'}""", 'xeric"sy')
    self.assertEqual(f"""{'xeric"sy'}""", 'xeric"sy')
