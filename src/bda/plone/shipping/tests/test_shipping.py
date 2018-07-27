# -*- coding: utf-8 -*-
from bda.plone.shipping import Shipping
from bda.plone.shipping.interfaces import IShipping
from bda.plone.shipping.tests import set_browserlayer
from bda.plone.shipping.tests import Shipping_INTEGRATION_TESTING
from decimal import Decimal
from zope.component import provideAdapter
from zope.interface import Interface

import unittest


class MockShipping(Shipping):
    sid = 'mock_shipping'
    label = 'Mock Shipping'
    description = 'Mock Shipping Description'
    available = True
    default = False

    def net(self, items):
        return Decimal(10)

    def vat(self, items):
        return Decimal(2)

    def calculate(self, items):
        # XXX: remove as of bda.plone.shipping 1.0
        return Decimal(10)


class TestShipping(unittest.TestCase):
    layer = Shipping_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        set_browserlayer(self.request)
        provideAdapter(MockShipping)
        self.shipping = IShipping(self.portal)

    def test_shipping(self):
        mock = self.shipping
        self.assertEquals(mock.sid, "mock_shipping")
        self.assertEquals(mock.label, "Mock Shipping")
        self.assertEquals(mock.description, "Mock Shipping Description")
        self.assertEquals(mock.available, True)
        self.assertEquals(mock.default, False)
        self.assertEquals(mock.net([]), Decimal(10))
        self.assertEquals(mock.vat([]), Decimal(2))
        # XXX: remove as of bda.plone.shipping 1.0
        self.assertEquals(mock.calculate([]), Decimal(10))
