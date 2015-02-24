Summary:	Font rendering capabilities for complex non-Roman writing systems
Summary(pl.UTF-8):	Wsparcie renderowania złożonych systemów pisma nierzymskiego
Name:		silgraphite
Version:	2.3.1
Release:	5
License:	LGPL v2.1+ or CPL v0.5+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tar.gz
# Source0-md5:	d35724900f6a4105550293686688bbb3
URL:		http://graphite.sil.org/
BuildRequires:	freetype-devel >= 2
BuildRequires:	libstdc++-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 1:0.14
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphite is a project within SIL's Non-Roman Script Initiative and
Language Software Development groups to provide rendering capabilities
for complex non-Roman writing systems. Graphite can be used to create
"smart fonts" capable of displaying writing systems with various
complex behaviors. With respect to the Text Encoding Model, Graphite
handles the "Rendering" aspect of writing system implementation.

%description -l pl.UTF-8
Graphite to projekt w ramach grup SIL Non-Roman Script Initiative
(inicjatywy pism nierzymskich SIL) oraz Language Software Development
(tworzenia oprogramowania językowego) mający na celu zapewnienie
wsparcia dla złożonych systemów pisma nierzymskiego. Graphite może być
używany do tworzenia "inteligentnych fontów", będących w stanie
wyświelać systemy pisma o różnych złożonych zachowaniach.
Uwzględniając model kodowania tekstu (Text Encoding Model) Graphite
obsługuje aspekt renderowania całości implementacji systemów pisma.

%package devel
Summary:	Header files for silgraphite library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki silgraphite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel >= 2
Requires:	libstdc++-devel
Requires:	xorg-lib-libXft-devel

%description devel
Header files for silgraphite library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki silgraphite.

%package static
Summary:	Static silgraphite library
Summary(pl.UTF-8):	Statyczna biblioteka silgraphite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static silgraphite library.

%description static -l pl.UTF-8
Statyczna biblioteka silgraphite.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# missing in make install; drop when fixed
[ ! -f $RPM_BUILD_ROOT%{_pkgconfigdir}/silgraphite-ft.pc ] || exit 1
cp -p wrappers/freetype/silgraphite-ft.pc $RPM_BUILD_ROOT%{_pkgconfigdir}
[ ! -f $RPM_BUILD_ROOT%{_pkgconfigdir}/silgraphite-xft.pc ] || exit 1
cp -p wrappers/xft/silgraphite-xft.pc $RPM_BUILD_ROOT%{_pkgconfigdir}
# and now obsoleted by pkg-config (and poisoned in case of wrappers
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgraphite*.la

# dlopened module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pango/*/modules/graphite/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README license/LICENSING.txt
%attr(755,root,root) %{_libdir}/libgraphite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite.so.3
%attr(755,root,root) %{_libdir}/libgraphite-ft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite-ft.so.0
%attr(755,root,root) %{_libdir}/libgraphite-xft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite-xft.so.0
%dir %{_libdir}/pango/*/modules/graphite
%attr(755,root,root) %{_libdir}/pango/*/modules/graphite/pango-graphite.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgraphite.so
%attr(755,root,root) %{_libdir}/libgraphite-ft.so
%attr(755,root,root) %{_libdir}/libgraphite-xft.so
%{_includedir}/graphite
%{_pkgconfigdir}/silgraphite.pc
%{_pkgconfigdir}/silgraphite-ft.pc
%{_pkgconfigdir}/silgraphite-xft.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgraphite.a
%{_libdir}/libgraphite-ft.a
%{_libdir}/libgraphite-xft.a
