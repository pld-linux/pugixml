Summary:	C++ XML processing library
Summary(pl.UTF-8):	Biblioteka C++ do przetwarzania XML-a
Name:		pugixml
Version:	1.2
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: http://code.google.com/p/pugixml/downloads/list
Source0:	http://pugixml.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	477f4a7d75af0383f52ee6622b3f6035
URL:		http://pugixml.org/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
%setup -q -c

%build
cd src
libtool --mode=compile %{__cxx} %{rpmcxxflags} -c pugixml.cpp
libtool --mode=link %{__cxx} %{rpmldflags} %{rpmcxxflags} -o libpugixml.la pugixml.lo -rpath %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

libtool --mode=install install src/libpugixml.la $RPM_BUILD_ROOT%{_libdir}
install src/pugi*.hpp $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_libdir}/libpugixml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpugixml.so.0

%files devel
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_libdir}/libpugixml.so
%{_libdir}/libpugixml.la
%{_includedir}/pugiconfig.hpp
%{_includedir}/pugixml.hpp

%files static
%defattr(644,root,root,755)
%{_libdir}/libpugixml.a
