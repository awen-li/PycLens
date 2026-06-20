# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_former_statements_refer_to_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    keywords = ('print', 'exec')
    cases = ['{} foo', '{} {{1:foo}}', 'if 1: {} foo', 'if 1: {} {{1:foo}}', 'if 1:\n    {} foo', 'if 1:\n    {} {{1:foo}}']
    for keyword in keywords:
        custom_msg = "call to '{}'".format(keyword)
        for case in cases:
            source = case.format(keyword)
            with self.subTest(source=source):
                with self.assertRaisesRegex(SyntaxError, custom_msg):
                    exec(source)
            source = source.replace('foo', '(foo.)')
            with self.subTest(source=source):
                with self.assertRaisesRegex(SyntaxError, 'invalid syntax'):
                    exec(source)
