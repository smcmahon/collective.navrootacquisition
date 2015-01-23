Introduction
============

If you're looking at this package, it's probably because you searched for INavigationRoot and Acquisition.

If so, you may have done so because you need Plone's navigation root facility to respect acquisition. That may be because you have a site map like::

    /
     - shared_obj
     - subsite1
     - subsite2

and you wish shared_obj to appear as if it is in the two subsites.

If so, you have probably discovered that asking for /subsite?/shared_obj results in the shared object rendering as if you had just requested /shared_obj. That's because the navigation root facility strips acquisition context before determining the navigation root.

This package monkey patches getNavigationRootObj to know if a navigation site root has been traversed by the request. If so, that navigation root is returned.

This package is meant only for use by knowledgable Plone integrators who are capable of evaluating the risks of patching a core function.

Thanks to Wichert Akkerman for figuring out the trick to make this possible with minimal intervention. In a `discussion thread <http://sourceforge.net/p/plone/mailman/plone-developers/thread/CAHA8JiTA0Cmph5jLJJ4QTQdnRV2L6uUtiZ56JAp0w-zPfAwvhA@mail.gmail.com/>`_ he suggested annotating the request object with the navigation site root whenever an object providing INavigationRoot is traversed.

