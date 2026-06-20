# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_custom_builder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(SIMPLE_XMLFILE) as f:
        data = f.read()

    class Builder(list):

        def start(self, tag, attrib):
            self.append(('start', tag))

        def end(self, tag):
            self.append(('end', tag))

        def data(self, text):
            pass
    builder = Builder()
    parser = ET.XMLParser(target=builder)
    parser.feed(data)
    self.assertEqual(builder, [('start', 'root'), ('start', 'element'), ('end', 'element'), ('start', 'element'), ('end', 'element'), ('start', 'empty-element'), ('end', 'empty-element'), ('end', 'root')])
    with open(SIMPLE_NS_XMLFILE) as f:
        data = f.read()

    class Builder(list):

        def start(self, tag, attrib):
            self.append(('start', tag))

        def end(self, tag):
            self.append(('end', tag))

        def data(self, text):
            pass

        def pi(self, target, data):
            self.append(('pi', target, data))

        def comment(self, data):
            self.append(('comment', data))

        def start_ns(self, prefix, uri):
            self.append(('start-ns', prefix, uri))

        def end_ns(self, prefix):
            self.append(('end-ns', prefix))
    builder = Builder()
    parser = ET.XMLParser(target=builder)
    parser.feed(data)
    self.assertEqual(builder, [('pi', 'pi', 'data'), ('comment', ' comment '), ('start-ns', '', 'namespace'), ('start', '{namespace}root'), ('start', '{namespace}element'), ('end', '{namespace}element'), ('start', '{namespace}element'), ('end', '{namespace}element'), ('start', '{namespace}empty-element'), ('end', '{namespace}empty-element'), ('end', '{namespace}root'), ('end-ns', '')])
