%define	major 0
%define libname	%mklibname nxml %{major}

Summary:	A C library for parsing, writing and creating XML 1.0 and 1.1 files or streams
Name:		libnxml
Version:	0.18.1
Release:	%mkrel 1
Group:		System/Libraries
License:	LGPL
URL:		http://autistici.org/bakunin/codes.php
Source0:	http://www.monkey.org/~provos/%{name}-%{version}.tar.bz2
#Patch0:		libnxml-0.8-lib64.diff
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

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
nXML is a C library for parsing, writing and creating XML 1.0 and
1.1 files or streams. It supports utf-8, utf-16be and utf-16le,
ucs-4 (1234, 4321, 2143, 2312).

This package contains the static %{name} library and its header
files.

%prep

%setup -q -n %{name}-%{version}
#%patch0 -p0

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/nxml.pc


