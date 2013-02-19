# -*- coding: utf-8 -*-
from zope.component import queryMultiAdapter, getMultiAdapter
from plone.app.layout.viewlets.common import ViewletBase
from rt.simpleslider.interfaces import ISliderSource
from rt.simpleslider.interfaces import ISliderUtils


class Slider(ViewletBase):
    """ This viewlet renders the placholder for gallery """

    def update(self):
        super(Slider, self).update()
        self.request.slider_tool = getMultiAdapter((self.view, self.context, self.request), ISliderUtils)
        slider_source_context = self.request.slider_tool.slider_source()
        self.request.slider_source = queryMultiAdapter((self.view, slider_source_context, self.request), ISliderSource)

    def render(self):
        if not self.request.slider_tool.show_slider():
            return ''
        return self.index()

    def slider_images(self):
        return self.request.slider_source.getSliderImages()

    def slider_captions(self):
        return self.request.slider_source.getSliderCaption()

    def get_location_info(self):
        return {}

    def get_body_text(self):
        """
        We are assuming the object that configure
        """
        return self.request.slider_tool.get_slider_text()
