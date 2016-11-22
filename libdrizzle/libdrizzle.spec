%global date 2011.07.21

Summary: Drizzle Client & Protocol Library
Name: libdrizzle
Version: 1.0
Release: 0.2.%{date}
# All code is BSD, except libdrizzle/sha1.{c,h} which are Public Domain
License: BSD and Public Domain
Group: System Environment/Libraries
URL: https://launchpad.net/libdrizzle
#Source0: http://launchpad.net/%{name}/trunk/0.8/+download/%{name}-%{version}.tar.gz 
# http://openresty.org/#DrizzleNginxModule
Source0: http://openresty.org/download/drizzle7-%{date}.tar.gz
Source1: README
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: curl-devel
BuildRequires: doxygen
BuildRequires: intltool
BuildRequires: libgcrypt-devel
BuildRequires: libuuid-devel
BuildRequires: pam-devel
BuildRequires: pcre-devel
BuildRequires: protobuf-devel
BuildRequires: readline-devel
BuildRequires: zlib-devel
BuildRequires: python

%description
This is the the client and protocol library for the Drizzle project. The
server, drizzled, will use this as for the protocol library, as well as the
client utilities and any new projects that require low-level protocol
communication (like proxies). Other language interfaces (PHP extensions, SWIG,
...) should be built off of this interface.

%package devel
Group: Development/Libraries
Summary: Drizzle Client & Protocol Library - Header files
Requires: %{name} = %{version}-%{release} 

%description devel
Development files for the Drizzle Client & Protocol Library

#package doc 
#Group: Documentation 
#Summary: Drizzle Client & Protocol Library Documentation
#Requires: %{name} = %{version}-%{release} 

#description doc 
#Documentation files for the Drizzle Client & Protocol Library

%prep
%setup -q -n drizzle7-%{date}
cp -a %{SOURCE1} .

%configure --without-server
%build
%{make_build} libdrizzle-1.0

%install
rm -rf %{buildroot}
make install-libdrizzle-1.0 DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""

# cleanup
rm -f %{buildroot}/%{_libdir}/libdrizzle.la 


%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%doc README AUTHORS ChangeLog COPYING
%{_libdir}/libdrizzle.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libdrizzle-1.0/
%{_libdir}/pkgconfig/libdrizzle-1.0.pc
%{_libdir}/libdrizzle.so

#files doc
#defattr(-,root,root,-)
#doc docs/api docs/dev

%changelog
* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 1.0-0.2.2011.07.21
- add dep python

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 03 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.8-6
- Readd AUTHORS ChangeLog COPYING README PROTOCOL docs

* Mon May 03 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.8-5
- Update License to reflect BSD and Public Domain (sha1 code)
- Make -doc package require base package

* Fri Apr 30 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.8-4
- Add -doc sub package, and build doxygen documentation

* Fri Apr 02 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.8-3
- Removed BuildRequires: gcc gcc-c++
- Removed INSTALL from doc
- Removed libdrizzle.la

* Thu Apr 01 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.8-2
- Adding README (submitted upstream)
- Removing empty NEWS file

* Fri Mar 19 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.8-1
- Latest sources
- Added %{?dist} tag

* Sun Feb 28 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.7-1
- Cleaning up spec
- Removed subpackage "name 0" (base package provides this functionality))
- Moved NEWS/ChangeLog/Etc under main package (not under -devel)
- devel package requires full version-release

* Mon Nov 30 2009 Lenz Grimmer <lenz@grimmer.com>
- Added Build requirement for gcc-c++
- Made the -devel package dependent on the shared lib

* Fri Apr 24 2009 Lenz Grimmer <lenz@grimmer.com>
- Added -devel subpackage, updated file list
- Fixed rpmlint errors and warnings

* Tue Jan 13 2009 Eric Day <eday@oddments.org> - 0.1-1
- Initial package
