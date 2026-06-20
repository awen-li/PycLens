# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_dtdhandler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser()
    handler = self.TestDTDHandler()
    parser.setDTDHandler(handler)
    parser.feed('<!DOCTYPE doc [\n')
    parser.feed('  <!ENTITY img SYSTEM "expat.gif" NDATA GIF>\n')
    parser.feed('  <!NOTATION GIF PUBLIC "-//CompuServe//NOTATION Graphics Interchange Format 89a//EN">\n')
    parser.feed(']>\n')
    parser.feed('<doc></doc>')
    parser.close()
    self.assertEqual(handler._notations, [('GIF', '-//CompuServe//NOTATION Graphics Interchange Format 89a//EN', None)])
    self.assertEqual(handler._entities, [('img', None, 'expat.gif', 'GIF')])
