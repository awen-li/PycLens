# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_split

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'Hello there -- you goof-ball, use the -b option!'
    result = self.wrapper._split(text)
    self.check(result, ['Hello', ' ', 'there', ' ', '--', ' ', 'you', ' ', 'goof-', 'ball,', ' ', 'use', ' ', 'the', ' ', '-b', ' ', 'option!'])
