# -*- coding: utf-8 -*-
from zope.deferredimport import deprecated

deprecated(
    "Import from new module 'bda.plone.cart.shipping' instead",
    Shippings="bda.plone.cart.shipping:Shippings",
    Shipping="bda.plone.cart.shipping:Shipping",
    NullItemDelivery="bda.plone.cart.shipping:NullItemDelivery",
)
