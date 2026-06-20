# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_dump_attribute_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.Element('cirriculum', status='public', company='example')
    with support.captured_stdout() as stdout:
        ET.dump(e)
    self.assertEqual(stdout.getvalue(), '<cirriculum status="public" company="example" />\n')
