# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_builder_lookup_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class RaisingBuilder:

        def __init__(self, raise_in=None, what=ValueError):
            self.raise_in = raise_in
            self.what = what

        def __getattr__(self, name):
            if name == self.raise_in:
                raise self.what(self.raise_in)

            def handle(*args):
                pass
            return handle
    ET.XMLParser(target=RaisingBuilder())
    for event in ('start', 'data', 'end', 'comment', 'pi'):
        with self.assertRaisesRegex(ValueError, event):
            ET.XMLParser(target=RaisingBuilder(event))
    ET.XMLParser(target=RaisingBuilder(what=AttributeError))
    for event in ('start', 'data', 'end', 'comment', 'pi'):
        parser = ET.XMLParser(target=RaisingBuilder(event, what=AttributeError))
        parser.feed(self.sample1)
        self.assertIsNone(parser.close())
