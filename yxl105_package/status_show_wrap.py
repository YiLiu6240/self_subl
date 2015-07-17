# coding=utf8
# referencing package: show files
import sublime, sublime_plugin

class StatusShowWrap(sublime_plugin.EventListener):

    def __init__(self):
        return

    def on_activated(self, view):
        self.update_status(view)
    def on_new(self, view):
        self.update_status(view)
    def on_post_save(self, view):
        self.update_status(view)
    # def on_selection_modified(self, view):
    #     self.update_status(view)

    def update_status(self, view):
        view_wrap_bool = view.settings().get('word_wrap')
        if view_wrap_bool == True:
            view_wrap = 'W'
        else:
            view_wrap = 'NW'
        view_wrap_centered = view.settings().get('draw_centered')
        view_wrap_width = view.settings().get('wrap_width')
        if view_wrap_width == 0:
            view_wrap_width = "Auto"
        else:
            view_wrap_width = str(view_wrap_width)
        view.set_status('ShowWrapStatus', "[%s: %s%s]" % (view_wrap, view_wrap_width, ("C" if view_wrap_centered == True else "")) )
