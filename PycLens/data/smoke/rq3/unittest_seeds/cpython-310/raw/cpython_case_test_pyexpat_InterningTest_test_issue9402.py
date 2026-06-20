# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: InterningTest_test_issue9402

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ExternalOutputter:

        def __init__(self, parser):
            self.parser = parser
            self.parser_result = None

        def ExternalEntityRefHandler(self, context, base, sysId, pubId):
            external_parser = self.parser.ExternalEntityParserCreate('')
            self.parser_result = external_parser.Parse(b'', True)
            return 1
    parser = expat.ParserCreate(namespace_separator='!')
    parser.buffer_text = 1
    out = ExternalOutputter(parser)
    parser.ExternalEntityRefHandler = out.ExternalEntityRefHandler
    parser.Parse(data, True)
    self.assertEqual(out.parser_result, 1)
