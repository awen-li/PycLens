# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: sf1296433Test_test_parse_only_xml_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xml = "<?xml version='1.0' encoding='iso8859'?><s>%s</s>" % ('a' * 1025)

    class SpecificException(Exception):
        pass

    def handler(text):
        raise SpecificException
    parser = expat.ParserCreate()
    parser.CharacterDataHandler = handler
    self.assertRaises(Exception, parser.Parse, xml.encode('iso8859'))
