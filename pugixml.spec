#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	C++ XML processing library
Summary(pl.UTF-8):	Biblioteka C++ do przetwarzania XML-a
Name:		pugixml
Version:	1.11
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: http://pugixml.org/
Source0:	http://github.com/zeux/pugixml/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	93540f4644fd4e4b02049554ef37fb90
Patch0:		longlong.patch
URL:		http://pugixml.org/
BuildRequires:	cmake >= 3.4
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pugixml is a C++ XML processing library, which consists of a DOM-like
interface with rich traversal/modification capabilities, an extremely
fast XML parser which constructs the DOM tree from an XML file/buffer,
and an XPath 1.0 implementation for complex data-driven tree queries.
Full Unicode support is also available, with Unicode interface
variants and conversions between different Unicode encodings (which
happen automatically during parsing/saving).

%description -l pl.UTF-8
pugixml to biblioteka C++ do przetwarzania XML-a, składająca się z
interfejsu w stylu DOM z dużymi możliwościami przeglądania i
modyfikowania, bardzo szybkim analizatorem XML-a tworzącym drzewo DOM
z pliku/bufora XML oraz implementacji XPath 1.0 do złożonych zapytań
drzewiastych zależnych od danych. Dostępna jest też pełna obsługa
Unikodu, z wariantowym interfejsem i przekształcaniem między różnymi
kodowaniami Unikodu (co wykonywane jest automatycznie podczas
analizy/zapisu).

%package devel
Summary:	Header files for pugixml library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pugixml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for pugixml library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pugixml.

%package static
Summary:	Static pugixml library
Summary(pl.UTF-8):	Statyczna biblioteka pugixml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pugixml library.

%description static -l pl.UTF-8
Statyczna biblioteka pugixml.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS=ON
cd ..

%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_SHARED_LIBS=OFF
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_libdir}/libpugixml.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpugixml.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_libdir}/libpugixml.so
%{_includedir}/pugiconfig.hpp
%{_includedir}/pugixml.hpp
%{_pkgconfigdir}/pugixml.pc
%{_libdir}/cmake/pugixml

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpugixml.a
%endif
