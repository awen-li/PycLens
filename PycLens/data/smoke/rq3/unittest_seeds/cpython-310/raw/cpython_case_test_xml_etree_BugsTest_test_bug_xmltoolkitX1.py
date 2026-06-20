# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkitX1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ET.XML('<doc><table><tbody/></table></doc>')
    with support.captured_stdout() as stdout:
        ET.dump(tree)
        self.assertEqual(stdout.getvalue(), '<doc><table><tbody /></table></doc>\n')
