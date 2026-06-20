# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_em_dash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'Em-dashes should be written -- thus.'
    self.check_wrap(text, 25, ['Em-dashes should be', 'written -- thus.'])
    self.check_wrap(text, 29, ['Em-dashes should be written', '-- thus.'])
    expect = ['Em-dashes should be written --', 'thus.']
    self.check_wrap(text, 30, expect)
    self.check_wrap(text, 35, expect)
    self.check_wrap(text, 36, ['Em-dashes should be written -- thus.'])
    text = 'You can also do--this or even---this.'
    expect = ['You can also do', '--this or even', '---this.']
    self.check_wrap(text, 15, expect)
    self.check_wrap(text, 16, expect)
    expect = ['You can also do--', 'this or even---', 'this.']
    self.check_wrap(text, 17, expect)
    self.check_wrap(text, 19, expect)
    expect = ['You can also do--this or even', '---this.']
    self.check_wrap(text, 29, expect)
    self.check_wrap(text, 31, expect)
    expect = ['You can also do--this or even---', 'this.']
    self.check_wrap(text, 32, expect)
    self.check_wrap(text, 35, expect)
    text = "Here's an -- em-dash and--here's another---and another!"
    expect = ["Here's", ' ', 'an', ' ', '--', ' ', 'em-', 'dash', ' ', 'and', '--', "here's", ' ', 'another', '---', 'and', ' ', 'another!']
    self.check_split(text, expect)
    text = 'and then--bam!--he was gone'
    expect = ['and', ' ', 'then', '--', 'bam!', '--', 'he', ' ', 'was', ' ', 'gone']
    self.check_split(text, expect)
