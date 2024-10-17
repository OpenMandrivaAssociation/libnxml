%define	major 0
%define libname	%mklibname nxml %{major}
%define develname	%mklibname nxml -d

Summary:	A C library for parsing, writing and creating XML 1.0 and 1.1 files or streams
Name:		libnxml
Version:	0.18.3
Release:	6
Group:		System/Libraries
License:	LGPLv2+
URL:		https://autistici.org/bakunin/codes.php
Source0:	http://www.autistici.org/bakunin/libnxml/%{name}-%{version}.tar.gz
BuildRequires:	curl-devel
BuildRequires:	openssl-devel

%description
nXML is a C library for parsing, writing and creating XML 1.0 and
1.1 files or streams. It supports utf-8, utf-16be and utf-16le,
ucs-4 (1234, 4321, 2143, 2312).
 
%package -n	%{libname}
Summary:	A C library for parsing, writing and creating XML 1.0 and 1.1 files or streams
Group:          System/Libraries

%description -n	%{libname}
nXML is a C library for parsing, writing and creating XML 1.0 and
1.1 files or streams. It supports utf-8, utf-16be and utf-16le,
ucs-4 (1234, 4321, 2143, 2312).

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{libname}-devel

%description -n	%{develname}
nXML is a C library for parsing, writing and creating XML 1.0 and
1.1 files or streams. It supports utf-8, utf-16be and utf-16le,
ucs-4 (1234, 4321, 2143, 2312).

This package contains the static %{name} library and its header
files.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x

%make

%install
%makeinstall_std

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/nxml.pc




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.18.3-4mdv2011.0
+ Revision: 620167
- the mass rebuild of 2010.0 packages

* Thu Oct 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.18.3-3mdv2010.0
+ Revision: 455887
- rebuild for new curl SSL backend

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 0.18.3-1mdv2009.0
+ Revision: 275899
- New version
- apply devel policy

* Sun Jun 29 2008 Emmanuel Andry <eandry@mandriva.org> 0.18.2-1mdv2009.0
+ Revision: 230036
- New version
- Fix license
- Fix Source0

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Emmanuel Andry <eandry@mandriva.org> 0.18.1-1mdv2008.1
+ Revision: 120697
- New version
- drop patch 0
- add major version check


* Tue Jan 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.11-2mdv2007.0
+ Revision: 109485
- Rebuild against new curl
- Import libnxml

* Mon Jul 10 2006 Emmanuel Andry <eandry@mandriva.org> 0.11-1mdv2007.0
- 0.11

* Wed May 17 2006 Emmanuel Andry <eandry@mandriva.org> 0.9-1mdk
- 0.9

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdk
- initial Mandriva package

