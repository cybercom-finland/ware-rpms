%global git_num 37
%global git_rev b1bf5b6

Name:           sregex
Version:        0.0.1rc1
Release:        %{git_num}.1%{?dist}
Summary:        Software tool for fast regexps

Group:          System Environment/Libraries
License:        BSD 3 clause
URL:            https://github.com/openresty/sregex/
Source0:        https://github.com/openresty/sregex/tarball/master?/openresty-sregex-v%{version}-%{git_num}-g%{git_rev}.tar.gz
Patch0:         0001-silence-warning-about-if-guard.patch
BuildRequires:  perl-Test-Harness
BuildRequires:  perl-Test-Base
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Test::LongString)
Requires:       libsregex%{?_isa} = %{version}-%{release}
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
A non-backtracking regex engine library tool for large data streams..

%package -n libsregex
Summary:        Software library for fast regexps
Group:          System Environment/Libraries

%description -n libsregex
A non-backtracking regex engine library for large data streams..


%package -n libsregex-devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       libsregex-devel%{?_isa} = %{version}-%{release}


%description -n libsregex-devel
The %{name}-devel package contains libraries and header files for 
developing applications that use %{name}.


%prep
%setup -q -n openresty-sregex-%{git_rev}
%patch0 -p1
perl -pi -e 's,/lib(\s*$|/),/%{_lib}$1,g' Makefile


%build
%{make_build}


%install
make install DESTDIR=%{buildroot} PREFIX=/usr 


%check
# Requires perl 5.16.2
make -k %{?_smp_mflags} test


%post -n libsregex -p /sbin/ldconfig


%postun -n libsregex -p /sbin/ldconfig


%files
%{_bindir}/sregex-cli

%files -n libsregex
%doc LICENSE README.markdown
%{_libdir}/libsregex.so.*

%files -n libsregex-devel
%{_libdir}/libsregex.so
%{_includedir}/sregex


%changelog
* Tue Nov 22 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.0.1rc1-37.1
- 0.0.1rc1 git_num 37
