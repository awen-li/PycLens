# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pulldom.py
# case: PullDOMTestCase_test_end_document

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = pulldom.parseString(SMALL_SAMPLE)
    for (evt, node) in items:
        if evt == pulldom.END_ELEMENT and node.tagName == 'html':
            break
    try:
        (evt, node) = next(items)
        self.assertEqual(pulldom.END_DOCUMENT, evt)
    except StopIteration:
        self.fail('Ran out of events, but should have received END_DOCUMENT')
