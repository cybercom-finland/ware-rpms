%global gitrev 28
%global gitshort abc638c

%if 0%{?fedora} >= 20

%if 0%{?fedora} < 24
%define luaver 5.2
%else
%define luaver 5.3
%endif

%else
%define luaver 5.1
%endif

%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define luacompatver 5.1
%define luacompatlibdir %{_libdir}/lua/%{luacompatver}
%define luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%define lua51dir %{_builddir}/lua51-%{name}-%{version}-%{release}

Name:           lua-ffi
Version:        1.0
Release:        0.1.%{gitrev}%{?dist}
Summary:        Standalone FFI library for calling C functions from lua.


Group:          Development/Libraries
License:        MIT
URL:            https://github.com/jmckaskill/luaffi
Source0:        https://github.com/jmckaskill/luaffi/archive/jmckaskill-luaffi-%{version}-work1-%{gitrev}-g%{gitshort}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  lua-devel
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires: lua(abi) = %{luaver}
%else
Requires: lua >= %{luaver}
%endif

%if 0%{?fedora} >= 20
BuildRequires:  compat-lua >= %{luacompatver}, compat-lua-devel >= %{luacompatver}
%endif


%description
This is a library for calling C function and manipulating C types from
lua. It is designed to be interface compatible with the FFI library in
luajit (see http://luajit.org/ext_ffi.html). It can parse C function
declarations and struct definitions that have been directly copied out
of C header files and into lua source as a string.

%if 0%{?fedora} >= 20
%package compat
Summary:        Standalone FFI library for calling C functions from Lua 5.1.
Group:          Development/Libraries

%description compat
This is a library for calling C function and manipulating C types from
lua. It is designed to be interface compatible with the FFI library in
luajit (see http://luajit.org/ext_ffi.html). It can parse C function
declarations and struct definitions that have been directly copied out
of C header files and into lua source as a string.
%endif

%prep
%setup -q -n jmckaskill-luaffi-%{gitshort}
find . -name \*.[ch] -print -exec chmod -x '{}' \;

%if 0%{?fedora} >= 20
rm -rf %{lua51dir}
cp -a . %{lua51dir}
pushd %{lua51dir}
popd
%endif

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC $(pkg-config --cflags lua)"

%if 0%{?fedora} >= 20
pushd %{lua51dir}
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC $(pkg-config --cflags lua-5.1)"
popd
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
mkdir -p $RPM_BUILD_ROOT%{lualibdir}

install ffi.so %{buildroot}%{lualibdir}


%if 0%{?fedora} >= 20
pushd %{lua51dir}
mkdir -p $RPM_BUILD_ROOT%{luacompatpkgdir}
mkdir -p $RPM_BUILD_ROOT%{luacompatlibdir}

install ffi.so %{buildroot}%{luacompatlibdir}
popd
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md
%{lualibdir}/*
#%{luapkgdir}/*
#%{_bindir}/*

%if 0%{?fedora} >= 20
%files compat
%defattr(-,root,root,-)
%doc README.md
%{luacompatlibdir}/*
#%{luacompatpkgdir}/*
%endif


%changelog
* Wed Aug  3 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 1.0-0.1.28
- fix build in F24

* Mon Mar  2 2015 Markus Linnala <Markus.Linnala@cybercom.com> - 1.0-0.0.28
- initial
