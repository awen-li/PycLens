# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: MakeParserTest_test_make_parser3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    make_parser(['module'])
    make_parser(('module',))
    make_parser({'module'})
    make_parser(frozenset({'module'}))
    make_parser({'module': None})
    make_parser(iter(['module']))
