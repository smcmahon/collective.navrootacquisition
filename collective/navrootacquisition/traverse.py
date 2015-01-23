from plone.app.layout.navigation.interfaces import INavigationRoot
from zope.component import adapts
from zope.interface import Interface
from ZPublisher.BaseRequest import DefaultPublishTraverse


class NavigationRootTraverse(DefaultPublishTraverse):
    adapts(INavigationRoot, Interface)

    def publishTraverse(self, request, name):
        request.navigation_root = self.context
        return super(NavigationRootTraverse, self).publishTraverse(request, name)

