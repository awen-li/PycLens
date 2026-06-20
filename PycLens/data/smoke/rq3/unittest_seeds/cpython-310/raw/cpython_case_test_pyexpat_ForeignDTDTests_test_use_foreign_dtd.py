# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: ForeignDTDTests_test_use_foreign_dtd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler_call_args = []

    def resolve_entity(context, base, system_id, public_id):
        handler_call_args.append((public_id, system_id))
        return 1
    parser = expat.ParserCreate()
    parser.UseForeignDTD(True)
    parser.SetParamEntityParsing(expat.XML_PARAM_ENTITY_PARSING_ALWAYS)
    parser.ExternalEntityRefHandler = resolve_entity
    parser.Parse(b"<?xml version='1.0'?><element/>")
    self.assertEqual(handler_call_args, [(None, None)])
    handler_call_args[:] = []
    parser = expat.ParserCreate()
    parser.UseForeignDTD()
    parser.SetParamEntityParsing(expat.XML_PARAM_ENTITY_PARSING_ALWAYS)
    parser.ExternalEntityRefHandler = resolve_entity
    parser.Parse(b"<?xml version='1.0'?><element/>")
    self.assertEqual(handler_call_args, [(None, None)])
