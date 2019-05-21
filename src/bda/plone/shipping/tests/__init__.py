# -*- coding: utf-8 -*-
from bda.plone.shipping.interfaces import IShippingExtensionLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from zope.interface import alsoProvides


def set_browserlayer(request):
    """Set the BrowserLayer for the request.

    We have to set the browserlayer manually, since importing the profile alone
    doesn't do it in tests.
    """
    alsoProvides(request, IShippingExtensionLayer)


class ShippingLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import bda.plone.shipping
        self.loadZCML(package=bda.plone.shipping,
                      context=configurationContext)

    def tearDownZope(self, app):
        pass


Shipping_FIXTURE = ShippingLayer()
Shipping_INTEGRATION_TESTING = IntegrationTesting(
    bases=(Shipping_FIXTURE,),
    name="Shipping:Integration")
