
_old_getNavigationRootObject = None


def getNavigationRootObject(context, portal):
    # look for our request annotation
    request = getattr(context, 'REQUEST', None)
    if request is not None:
        nav_root = getattr(request, 'navigation_root', None)
        if nav_root is not None and \
           nav_root.getPhysicalPath() != portal.getPhysicalPath():
            return nav_root
    return _old_getNavigationRootObject(context, portal)


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
