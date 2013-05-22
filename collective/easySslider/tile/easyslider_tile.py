from plone import tiles
from zope.interface import Interface

from Acquisition import aq_inner
from collective.cover import _
from collective.cover.tiles.base import AnnotationStorage
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile

from plone.tiles.interfaces import ITileDataManager
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import queryMultiAdapter
from zope.component import getMultiAdapter
from zope.interface import implements

import time


from plone.app.uuid.utils import uuidToObject
from plone.tiles.interfaces import ITileDataManager
from plone.uuid.interfaces import IUUID
from zope import schema



class IEasyliderTile(Interface):
    """  settings for easyslider tile  """
    
    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )
    
    slider = schema.Text(
        title=_(u'Path to slider'),
        required=True,
    )


class EasyliderTile(PersistentCoverTile):

    implements(IEasyliderTile)

    index = ViewPageTemplateFile('easyslider_tile.pt')

    is_configurable = True

    def is_set(self):
        return self.data['slider']
        
    def sliderpath(self):
    	portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
    	portal = portal_state.portal()
    	path = str(self.data['slider'])
    	if path.startswith('/'):
    	    path = path[1:]
    	return portal.restrictedTraverse(path, default=False)
    	