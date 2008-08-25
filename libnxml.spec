%define	major 0
%define libname	%mklibname nxml %{major}
%define develname	%mklibname nxml -d

Summary:	A C library for parsing, writing and creating XML 1.0 and 1.1 files or streams
Name:		libnxml
Version:	0.18.3
Release:	%mkrel 1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://autistici.org/bakunin/codes.php
Source0:	http://www.autistici.org/bakunin/libnxml/%{name}-%{version}.tar.gz
BuildRequires:	curl-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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
%{_libdir}/*.la
%{_libdir}/pkgconfig/nxml.pc


