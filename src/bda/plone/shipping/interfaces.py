# -*- coding: utf-8 -*-
from zope.deferredimport import deprecated

deprecated(
    "Import from new module 'bda.plone.cart.interfaces' instead",
    IShippingExtensionLayer="bda.plone.cart.interfaces:IShippingExtensionLayer",
    IShippingSettings="bda.plone.cart.interfaces:IShippingSettings",
    IShipping="bda.plone.cart.interfaces:IShipping",
    IShippingItem="bda.plone.cart.interfaces:IShippingItem",
    IItemDelivery="bda.plone.cart.interfaces:IItemDelivery",
)
