# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_iterparse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iterparse = ET.iterparse
    context = iterparse(SIMPLE_XMLFILE)
    (action, elem) = next(context)
    self.assertEqual((action, elem.tag), ('end', 'element'))
    self.assertEqual([(action, elem.tag) for (action, elem) in context], [('end', 'element'), ('end', 'empty-element'), ('end', 'root')])
    self.assertEqual(context.root.tag, 'root')
    context = iterparse(SIMPLE_NS_XMLFILE)
    self.assertEqual([(action, elem.tag) for (action, elem) in context], [('end', '{namespace}element'), ('end', '{namespace}element'), ('end', '{namespace}empty-element'), ('end', '{namespace}root')])
    events = ()
    context = iterparse(SIMPLE_XMLFILE, events)
    self.assertEqual([(action, elem.tag) for (action, elem) in context], [])
    events = ()
    context = iterparse(SIMPLE_XMLFILE, events=events)
    self.assertEqual([(action, elem.tag) for (action, elem) in context], [])
    events = ('start', 'end')
    context = iterparse(SIMPLE_XMLFILE, events)
    self.assertEqual([(action, elem.tag) for (action, elem) in context], [('start', 'root'), ('start', 'element'), ('end', 'element'), ('start', 'element'), ('end', 'element'), ('start', 'empty-element'), ('end', 'empty-element'), ('end', 'root')])
    events = ('start', 'end', 'start-ns', 'end-ns')
    context = iterparse(SIMPLE_NS_XMLFILE, events)
    self.assertEqual([(action, elem.tag) if action in ('start', 'end') else (action, elem) for (action, elem) in context], [('start-ns', ('', 'namespace')), ('start', '{namespace}root'), ('start', '{namespace}element'), ('end', '{namespace}element'), ('start', '{namespace}element'), ('end', '{namespace}element'), ('start', '{namespace}empty-element'), ('end', '{namespace}empty-element'), ('end', '{namespace}root'), ('end-ns', None)])
    events = ('start-ns', 'end-ns')
    context = iterparse(io.StringIO("<root xmlns=''/>"), events)
    res = [action for (action, elem) in context]
    self.assertEqual(res, ['start-ns', 'end-ns'])
    events = ('start', 'end', 'bogus')
    with open(SIMPLE_XMLFILE, 'rb') as f:
        with self.assertRaises(ValueError) as cm:
            iterparse(f, events)
        self.assertFalse(f.closed)
    self.assertEqual(str(cm.exception), "unknown event 'bogus'")
    with warnings_helper.check_no_resource_warning(self):
        with self.assertRaises(ValueError) as cm:
            iterparse(SIMPLE_XMLFILE, events)
        self.assertEqual(str(cm.exception), "unknown event 'bogus'")
        del cm
    source = io.BytesIO(b"<?xml version='1.0' encoding='iso-8859-1'?>\n<body xmlns='http://&#233;ffbot.org/ns'\n      xmlns:cl\xe9='http://effbot.org/ns'>text</body>\n")
    events = ('start-ns',)
    context = iterparse(source, events)
    self.assertEqual([(action, elem) for (action, elem) in context], [('start-ns', ('', 'http://éffbot.org/ns')), ('start-ns', ('clé', 'http://effbot.org/ns'))])
    source = io.StringIO('<document />junk')
    it = iterparse(source)
    (action, elem) = next(it)
    self.assertEqual((action, elem.tag), ('end', 'document'))
    with self.assertRaises(ET.ParseError) as cm:
        next(it)
    self.assertEqual(str(cm.exception), 'junk after document element: line 1, column 12')
    self.addCleanup(os_helper.unlink, TESTFN)
    with open(TESTFN, 'wb') as f:
        f.write(b'<document />junk')
    it = iterparse(TESTFN)
    (action, elem) = next(it)
    self.assertEqual((action, elem.tag), ('end', 'document'))
    with warnings_helper.check_no_resource_warning(self):
        with self.assertRaises(ET.ParseError) as cm:
            next(it)
        self.assertEqual(str(cm.exception), 'junk after document element: line 1, column 12')
        del cm, it
    with warnings_helper.check_no_resource_warning(self):
        it = iterparse(TESTFN)
        del it
    with self.assertRaises(FileNotFoundError):
        iterparse('nonexistent')
