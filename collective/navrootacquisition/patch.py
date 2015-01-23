from Acquisition import (aq_base, aq_parent, aq_inner)
from plone.app.layout.navigation.interfaces import INavigationRoot

_old_getNavigationRootObject = None


def getNavigationRootObject(context, portal):
    # look for our request annotation
    nav_root = getattr(context.REQUEST, 'navigation_root', None)
    if nav_root is None:
        return _old_getNavigationRootObject(context, portal)
    else:
        return nav_root


def handleApplyPatch(scope, original, replacement):
    import logging
    logger = logging.getLogger("collective.navrootacquisition")
    logger.info("setting up to apply acquisition to nav roots")

    # preserveOriginal doesn't work on module-level functions,
    # so do the work here.
    global _old_getNavigationRootObject
    _old_getNavigationRootObject = getattr(scope, original)

    # patch
    setattr(scope, original, replacement)
