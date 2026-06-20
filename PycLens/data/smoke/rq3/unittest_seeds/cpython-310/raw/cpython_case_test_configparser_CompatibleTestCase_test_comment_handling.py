# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: CompatibleTestCase_test_comment_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config_string = textwrap.dedent('        [Commented Bar]\n        baz=qwe ; a comment\n        foo: bar # not a comment!\n        # but this is a comment\n        ; another comment\n        quirk: this;is not a comment\n        ; a space must precede an inline comment\n        ')
    cf = self.fromstring(config_string)
    self.assertEqual(cf.get('Commented Bar', 'foo'), 'bar # not a comment!')
    self.assertEqual(cf.get('Commented Bar', 'baz'), 'qwe')
    self.assertEqual(cf.get('Commented Bar', 'quirk'), 'this;is not a comment')
