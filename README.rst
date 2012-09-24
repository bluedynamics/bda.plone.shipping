bda.plone.shipping
==================


Create translations
-------------------

::

    cd src/bda/plone/shipping/
    
    i18ndude rebuild-pot --pot locales/bda.plone.shipping.pot \
        --merge locales/manual.pot --create bda.plone.shipping .
    
    i18ndude sync --pot locales/bda.plone.shipping.pot \
        locales/de/LC_MESSAGES/bda.plone.shipping.po

