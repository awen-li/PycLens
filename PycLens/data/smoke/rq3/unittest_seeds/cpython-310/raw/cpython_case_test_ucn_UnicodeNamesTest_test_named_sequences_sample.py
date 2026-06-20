# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_named_sequences_sample

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sequences = [('LATIN SMALL LETTER R WITH TILDE', 'r̃'), ('TAMIL SYLLABLE SAI', 'ஸை'), ('TAMIL SYLLABLE MOO', 'மோ'), ('TAMIL SYLLABLE NNOO', 'ணோ'), ('TAMIL CONSONANT KSS', 'க்ஷ்')]
    for (seqname, codepoints) in sequences:
        self.assertEqual(unicodedata.lookup(seqname), codepoints)
        with self.assertRaises(SyntaxError):
            self.checkletter(seqname, None)
        with self.assertRaises(KeyError):
            unicodedata.ucd_3_2_0.lookup(seqname)
