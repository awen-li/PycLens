# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: LongWordTestCase_test_break_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_wrap(self.text, 30, ['Did you say "supercalifragilis', 'ticexpialidocious?" How *do*', 'you spell that odd word,', 'anyways?'])
    self.check_wrap(self.text, 50, ['Did you say "supercalifragilisticexpialidocious?"', 'How *do* you spell that odd word, anyways?'])
    self.check_wrap('-' * 10 + 'hello', 10, ['----------', '               h', '               e', '               l', '               l', '               o'], subsequent_indent=' ' * 15)
    self.check_wrap(self.text, 12, ['Did you say ', '"supercalifr', 'agilisticexp', 'ialidocious?', '" How *do*', 'you spell', 'that odd', 'word,', 'anyways?'])
