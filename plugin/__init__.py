from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import gettext


def localeInit():
	gettext.bindtextdomain("MeteoViewer", resolveFilename(SCOPE_PLUGINS, "Extensions/MeteoViewer/locale"))


def _(txt):
	t = gettext.dgettext("MeteoViewer", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t


localeInit()
language.addCallback(localeInit)
