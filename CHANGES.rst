
Changelog
=========

2.0.dev0 (unreleased)
---------------------

- Move whole shipping to bda.plone.cart. 
  Here are only bbb imports.
  [jensens]

- Removed all superfluos stuff.
  [jensens]

- Update version and classifiers - 2.x targets Plone 5.1/5.2 without Archetypes
  [agitator]


1.0a1 (unreleased)
------------------

- Replace unittest2 with untittest
  [llisa123]

- Add ``IShippingItem.free_shipping`` flag.
  [rnix]

- Plone 5 update
  [agitator]


0.4
---

- Add ``IShippingItem.shippable`` Attribute.
  [rnix]

- Implement ``available`` and ``default`` properties on
  ``bda.plone.shipping.Shipping`` using settings from
  ``bda.plone.shipping.interfaces.IShippingSettings``.
  [rnix]

- Introduce ``bda.plone.payment.interfaces.IShippingSettings``.
  [rnix]

- Deprecate ``IShipping.calculate``. Use ``IShipping.net`` and
  ``IShipping.vat`` instead.
  [rnix]

- Add ``description`` attribute to ``IShipping`` interface.
  [rnix]

- Remove ``FlatRate`` shipping.
  [rnix]


0.3
---

- Introduce ``IItemDelivery`` interface and corresponding base implementation.
  [rnix]

- Introduce ``IShippingItem`` interface.
  [rnix]


0.2
---

- Add tests.
  [thet]


0.1
---

- initial work.
  [rnix]
