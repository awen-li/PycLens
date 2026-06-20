# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pulldom.py
# case: PullDOMTestCase_test_expandItem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = pulldom.parseString(SMALL_SAMPLE)
    for (evt, item) in items:
        if evt == pulldom.START_ELEMENT and item.tagName == 'title':
            items.expandNode(item)
            self.assertEqual(1, len(item.childNodes))
            break
    else:
        self.fail('No "title" element detected in SMALL_SAMPLE!')
    for (evt, node) in items:
        if evt == pulldom.START_ELEMENT:
            break
    self.assertEqual('hr', node.tagName, 'expandNode did not leave DOMEventStream in the correct state.')
    items.expandNode(node)
    self.assertEqual(next(items)[0], pulldom.CHARACTERS)
    (evt, node) = next(items)
    self.assertEqual(node.tagName, 'p')
    items.expandNode(node)
    next(items)
    (evt, node) = next(items)
    self.assertEqual(node.tagName, 'html')
    with self.assertRaises(StopIteration):
        next(items)
    items.clear()
    self.assertIsNone(items.parser)
    self.assertIsNone(items.stream)
