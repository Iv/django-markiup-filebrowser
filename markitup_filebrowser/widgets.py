from django.contrib.admin.widgets import AdminTextareaWidget
from markitup.util import absolute_url
import posixpath
from markitup.widgets import MarkItUpWidget
from filebrowser.settings import URL_FILEBROWSER_MEDIA


class MarkitUpFilebrowserWidget(MarkItUpWidget):
    def _media(self):
        media = super(MarkitUpFilebrowserWidget, self)._media()
        media.add_js((
            absolute_url('markitup_filebrowser/sets/markdown/FilebrowserHelper.js'),
            posixpath.join(URL_FILEBROWSER_MEDIA, 'js/AddFileBrowser.js'),
        ))
        return media

    media = property(_media)


class AdminMarkitUpFilebrowserWidget(MarkitUpFilebrowserWidget, AdminTextareaWidget):
    pass