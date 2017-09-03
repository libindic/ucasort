#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Sort


class UcasortTest(TestCase):

    def setUp(self):
        super(UcasortTest, self).setUp()
        self.sorter = Sort()

    def test_sort(self):
        words = u"കർത്തവ്യം" + \
                u" അംബരീക്ഷൻ" + \
                u" കൃത്യനിഷ്ഠ" + \
                u" ശാപം" + \
                u" ക്ഷമ" + \
                u" സോമൻ" + \
                u" ഷീല"
        self.assertEqual(self.sorter.sort(words)['SILPA'],
                         [u'അംബരീക്ഷൻ',
                          u'കർത്തവ്യം',
                          u'കൃത്യനിഷ്ഠ',
                          u'ക്ഷമ',
                          u'ശാപം',
                          u'ഷീല',
                          u'സോമൻ'
                          ]
                         )
