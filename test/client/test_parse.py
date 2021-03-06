import unittest

from nose.tools import eq_

from client.parse import parse


class ParseTest(unittest.TestCase):

    def test_parse(self):
        result = parse('./test/data/example.xml')
        expect = [[{'duration': 2, 'pitch': {'octave': 4, 'step': 'G'}}],
                  [{'duration': 3, 'pitch': {'octave': 4, 'step': 'F'}},
                   {'duration': 1, 'pitch': {'octave': 4, 'step': 'E'}},
                   {'duration': 2, 'pitch': {'octave': 4, 'step': 'E'}},
                   {'duration': 1, 'pitch': {'octave': 4, 'step': 'B'}},
                   {'duration': 1, 'pitch': {'octave': 4, 'step': 'G'}}]]
        eq_(result, expect)
