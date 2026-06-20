# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML('<html><link/><script>1 &lt; 2</script></html>')
    e.tail = '\n'
    self.assertEqual(serialize(e), '<html><link /><script>1 &lt; 2</script></html>\n')
    self.assertEqual(serialize(e, method=None), '<html><link /><script>1 &lt; 2</script></html>\n')
    self.assertEqual(serialize(e, method='xml'), '<html><link /><script>1 &lt; 2</script></html>\n')
    self.assertEqual(serialize(e, method='html'), '<html><link><script>1 < 2</script></html>\n')
    self.assertEqual(serialize(e, method='text'), '1 < 2\n')
