# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_punct_hyphens

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_split("the 'wibble-wobble' widget", ['the', ' ', "'wibble-", "wobble'", ' ', 'widget'])
    self.check_split('the "wibble-wobble" widget', ['the', ' ', '"wibble-', 'wobble"', ' ', 'widget'])
    self.check_split('the (wibble-wobble) widget', ['the', ' ', '(wibble-', 'wobble)', ' ', 'widget'])
    self.check_split("the ['wibble-wobble'] widget", ['the', ' ', "['wibble-", "wobble']", ' ', 'widget'])
    self.check_split("what-d'you-call-it.", "what-d'you-|call-|it.".split('|'))
