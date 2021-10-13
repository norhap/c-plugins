AC_INIT([enigma2-c-plugins],[1.0])
AM_INIT_AUTOMAKE([dist-bzip2 foreign no-define tar-pax])
AC_CONFIG_HEADERS([enigma2-plugins-config.h])

# Silent rules are available since 1.11, but older versions
# are still in use. So don't use them unconditionally.
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AC_USE_SYSTEM_EXTENSIONS
AC_SYS_LARGEFILE

AC_PROG_CC
AC_PROG_CXX
m4_ifdef([LT_INIT], [LT_INIT], [AC_PROG_LIBTOOL])
AC_CONFIG_MACRO_DIR([m4])

AC_CHECK_HEADERS([dbox/fp.h dbox/lcd-ks0713.h])

AC_PATH_PROG(MSGFMT, msgfmt, AC_MSG_ERROR(Could not find msgfmt))
AC_PATH_PROG(MSGINIT, msginit, AC_MSG_ERROR(Could not find msginit))
AC_PATH_PROG(MSGMERGE, msgmerge, AC_MSG_ERROR(Could not find msgmerge))
AC_PATH_PROG(MSGUNIQ, msguniq, AC_MSG_ERROR(Could not find msguniq))
AC_PATH_PROG(XGETTEXT, xgettext, AC_MSG_ERROR(Could not find xgettext))

AM_PATH_PYTHON
AX_PYTHON_DEVEL
AX_PTHREAD

AC_ARG_WITH(arch,
	AS_HELP_STRING([--with-arch],[build for ARCH, $withval]),
	[ARCH="$withval"],[ARCH=""])
AC_SUBST(ARCH)
AC_DEFINE_UNQUOTED(ARCH,"$ARCH",[box architecture])

AM_CONDITIONAL(SH4, test `echo "$ARCH" | cut -b 1-3` == "sh4")
AM_CONDITIONAL(MIPSEL, test `echo "$ARCH" | cut -b 1-6` == "mipsel")
AM_CONDITIONAL(ARM, test `echo "$ARCH" | cut -b 1-3` == "arm")

AC_ARG_WITH(boxtype,
	AS_HELP_STRING([--with-boxtype],[build for BOXTYPE, $withval]),
	[BOXTYPE="$withval"],[BOXTYPE=""])
AC_SUBST(BOXTYPE)
AC_DEFINE_UNQUOTED(BOXTYPE,"$BOXTYPE",[box type])

AC_ARG_WITH(brandname,
	[  --with-brandname=NAME brand name [[none,dreambox...]]],
	[MACHINE_BRAND="$withval"],[MACHINE_BRAND="dreambox"])
AC_SUBST(MACHINE_BRAND)
AC_DEFINE_UNQUOTED(MACHINE_BRAND,"$MACHINE_BRAND",[brand name]

AC_ARG_WITH(stbplatform,
	AS_HELP_STRING([--with-stbplatform],[build for STBPLATFORM, $withval]),
	[STBPLATFORM="$withval"],[STBPLATFORM=""])
AC_SUBST(STBPLATFORM)
AC_DEFINE_UNQUOTED(STBPLATFORM,"$STBPLATFORM",[stb platform])

PKG_CHECK_MODULES(ENIGMA2, enigma2)

AC_ARG_WITH(debug,
	AS_HELP_STRING([--without-debug],[disable debugging code]),
	[with_debug="$withval"],[with_debug="yes"])
if test "$with_debug" = "yes"; then
	DEBUG_CFLAGS="-ggdb3"
	AC_DEFINE([DEBUG],[1],[Define to 1 to enable debugging code])
fi
AC_SUBST(DEBUG_CFLAGS)

AC_CONFIG_FILES([
Makefile

AirPlayer/Makefile
AirPlayer/po/Makefile
AirPlayer/src/Makefile
AirPlayer/src/720x576/Makefile
AirPlayer/src/1024x576/Makefile
AirPlayer/src/1280x720/Makefile
AirPlayer/src/1920x1080/Makefile
AirPlayer/src/lib/Makefile
AirPlayer/src/lib/biplist/Makefile
AirPlayer/src/mediabackends/Makefile

MisPlsLcnScan/Makefile
MisPlsLcnScan/lib/Makefile
MisPlsLcnScan/po/Makefile
MisPlsLcnScan/src/Makefile

moviecut/Makefile
moviecut/meta/Makefile
moviecut/po/Makefile
moviecut/src_cc/Makefile
moviecut/src/Makefile

networkbrowser/Makefile
networkbrowser/meta/Makefile
networkbrowser/po/Makefile
networkbrowser/src/icons/Makefile
networkbrowser/src/lib/Makefile
networkbrowser/src/Makefile

TerrestrialScan/Makefile
TerrestrialScan/lib/Makefile
TerrestrialScan/po/Makefile
TerrestrialScan/src/Makefile

vps/Makefile
vps/meta/Makefile
vps/po/Makefile
vps/src_cc/Makefile
vps/src/Makefile
vps/src/web-data/Makefile

])
AC_OUTPUT
