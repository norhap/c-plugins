#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
#===============================================================================
# NetworkBrowser and MountManager Plugin by acid-burn
# netscan lib by Nix_niX
# for further License informations see the corresponding License files
# or SourceCodes
#
#===============================================================================

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os
import gettext

PluginLanguageDomain = "NetworkBrowser"
PluginLanguagePath = "SystemPlugins/NetworkBrowser/locale"


def localeInit():
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
	if gettext.dgettext(PluginLanguageDomain, txt):
		return gettext.dgettext(PluginLanguageDomain, txt)
	else:
		print("[" + PluginLanguageDomain + "] fallback to default translation for " + txt)
		return gettext.gettext(txt)


localeInit()
language.addCallback(localeInit)
