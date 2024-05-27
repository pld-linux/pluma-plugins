Summary:	Collection of plugins for the Pluma text editor
Summary(pl.UTF-8):	Zbiór wtyczek do edytora tekstu Pluma
Name:		pluma-plugins
Version:	1.28.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	https://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
# Source0-md5:	ec095a1c4000d261b6b85fb5b96a921b
URL:		https://wiki.mate-desktop.org/mate-desktop/components/pluma-plugins/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.9.0
BuildRequires:	gtksourceview4-devel >= 4.0.2
BuildRequires:	libpeas-devel >= 1.7.0
BuildRequires:	libpeas-gtk-devel >= 1.7.0
BuildRequires:	libtool >= 2:2.2
# xmllint
BuildRequires:	libxml2-progs >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	pluma-devel >= 1.25.3
BuildRequires:	python-dbus-devel >= 0.82
BuildRequires:	python3-devel >= 1:3
BuildRequires:	python3-pygobject3 >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
# Vte-2.91 gobject interface
BuildRequires:	vte >= 0.38
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.32.0
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.9.0
Requires:	gtksourceview4 >= 4.0.2
Requires:	libpeas >= 1.7.0
Requires:	libpeas-gtk >= 1.7.0
Requires:	pluma >= 1.25.3
Requires:	python3 >= 1:3
Requires:	python3-dbus >= 0.82
Requires:	python3-pygobject3 >= 3.0
Requires:	vte >= 0.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of plugins for the Pluma text editor.

%description -l pl.UTF-8
Zbiór wtyczek do edytora tekstu Pluma.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/pluma/plugins/lib*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ie,ku_IQ}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/help/{es_ES,frp,ie,jv,ur_PK,zh-Hans}

%find_lang %{name} --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS

# python common code
%{_libdir}/pluma/plugins/gpdefs.py
%{_libdir}/pluma/plugins/__pycache__/gpdefs.cpython-*.py[co]

# C plugins
%attr(755,root,root) %{_libdir}/pluma/plugins/libbookmarks.so
%{_libdir}/pluma/plugins/bookmarks.plugin
%{_datadir}/metainfo/pluma-bookmarks.metainfo.xml

%attr(755,root,root) %{_libdir}/pluma/plugins/libquickhighlight.so
%{_libdir}/pluma/plugins/quickhighlight.plugin
%{_datadir}/metainfo/pluma-quickhighlight.metainfo.xml

%attr(755,root,root) %{_libdir}/pluma/plugins/libwordcompletion.so
%{_libdir}/pluma/plugins/wordcompletion.plugin
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.wordcompletion.gschema.xml

# Python plugins
%{_libdir}/pluma/plugins/bracketcompletion.plugin
%{_libdir}/pluma/plugins/bracketcompletion.py
%{_libdir}/pluma/plugins/__pycache__/bracketcompletion.cpython-*.py[co]

%{_libdir}/pluma/plugins/codecomment.plugin
%{_libdir}/pluma/plugins/codecomment.py
%{_libdir}/pluma/plugins/__pycache__/codecomment.cpython-*.py[co]
%{_datadir}/metainfo/pluma-codecomment.metainfo.xml

%{_libdir}/pluma/plugins/smartspaces.plugin
%{_libdir}/pluma/plugins/smartspaces.py
%{_libdir}/pluma/plugins/__pycache__/smartspaces.cpython-*.py[co]

%{_libdir}/pluma/plugins/sourcecodebrowser
%{_libdir}/pluma/plugins/sourcecodebrowser.plugin
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.sourcecodebrowser.gschema.xml
%{_datadir}/pluma/plugins/sourcecodebrowser

%{_libdir}/pluma/plugins/synctex
%{_libdir}/pluma/plugins/synctex.plugin
%{_datadir}/metainfo/pluma-synctex.metainfo.xml

%{_libdir}/pluma/plugins/terminal.plugin
%{_libdir}/pluma/plugins/terminal.py
%{_libdir}/pluma/plugins/__pycache__/terminal.cpython-*.py[co]
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.terminal.gschema.xml
%{_datadir}/metainfo/pluma-terminal.metainfo.xml
