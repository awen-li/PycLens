# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_symbolic_refs_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkTemplateError('(?P<a>x)', '\\g<a', 'xx', 'missing >, unterminated name', 3)
    self.checkTemplateError('(?P<a>x)', '\\g<', 'xx', 'missing group name', 3)
    self.checkTemplateError('(?P<a>x)', '\\g', 'xx', 'missing <', 2)
    self.checkTemplateError('(?P<a>x)', '\\g<a a>', 'xx', "bad character in group name 'a a'", 3)
    self.checkTemplateError('(?P<a>x)', '\\g<>', 'xx', 'missing group name', 3)
    self.checkTemplateError('(?P<a>x)', '\\g<1a1>', 'xx', "bad character in group name '1a1'", 3)
    self.checkTemplateError('(?P<a>x)', '\\g<2>', 'xx', 'invalid group reference 2', 3)
    self.checkTemplateError('(?P<a>x)', '\\2', 'xx', 'invalid group reference 2', 1)
    with self.assertRaisesRegex(IndexError, "unknown group name 'ab'"):
        re.sub('(?P<a>x)', '\\g<ab>', 'xx')
    self.checkTemplateError('(?P<a>x)', '\\g<-1>', 'xx', "bad character in group name '-1'", 3)
    self.checkTemplateError('(?P<a>x)', '\\g<©>', 'xx', "bad character in group name '©'", 3)
    self.checkTemplateError('(?P<a>x)', '\\g<㊀>', 'xx', "bad character in group name '㊀'", 3)
    self.checkTemplateError('(?P<a>x)', '\\g<¹>', 'xx', "bad character in group name '¹'", 3)
