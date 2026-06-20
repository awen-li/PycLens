# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config_string = '[Long Line]\nfoo{0[0]} this line is much, much longer than my editor\n   likes it.\n[{default_section}]\nfoo{0[1]} another very\n long line\n[Long Line - With Comments!]\ntest {0[1]} we        {comment} can\n            also      {comment} place\n            comments  {comment} in\n            multiline {comment} values\n'.format(self.delimiters, comment=self.comment_prefixes[0], default_section=self.default_section)
    if self.allow_no_value:
        config_string += '[Valueless]\noption-without-value\n'
    cf = self.fromstring(config_string)
    for space_around_delimiters in (True, False):
        output = io.StringIO()
        cf.write(output, space_around_delimiters=space_around_delimiters)
        delimiter = self.delimiters[0]
        if space_around_delimiters:
            delimiter = ' {} '.format(delimiter)
        expect_string = '[{default_section}]\nfoo{equals}another very\n\tlong line\n\n[Long Line]\nfoo{equals}this line is much, much longer than my editor\n\tlikes it.\n\n[Long Line - With Comments!]\ntest{equals}we\n\talso\n\tcomments\n\tmultiline\n\n'.format(equals=delimiter, default_section=self.default_section)
        if self.allow_no_value:
            expect_string += '[Valueless]\noption-without-value\n\n'
        self.assertEqual(output.getvalue(), expect_string)
