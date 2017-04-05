# ../common/perl-template  -tag ware ExtUtils-Constant
#

%define pkgname ExtUtils-Constant
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}

Name:      perl-%{pkgname}-ware
Summary:   %{pkgname} - Perl module
Version:   0.23
Release:   0.0%{?dist}
License:   GPL+ or Artistic
Group:     Development/Libraries
Url:       http://search.cpan.org/dist/ExtUtils-Constant/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Source:    http://search.cpan.org//CPAN/authors/id/N/NW/NWCLARK/ExtUtils-Constant-0.23.tar.gz
%if 0%{?fedora} >= 25
BuildRequires: perl-generators
%endif
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)

# AutoReqProv: no
# Requires: perl, perl(ExtUtils::Manifest), perl(Test::Harness), perl(Test::More)
# Provides: 


%description
Newer version.


%prep
%setup -q -n %{pkgname}-%{version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{version}
perl -pi -e 's/^auto_install\;//' Makefile.PL


%build
if [ -f Makefile.PL ]; then
  #CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL destdir=%{buildroot} INSTALLDIRS=vendor
  CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=%{buildroot}%{_prefix} INSTALLDIRS=vendor
  make
  make test
elif [ -f Build.PL ]; then
  CFLAGS="$RPM_OPT_FLAGS" perl Build.PL PREFIX=%{buildroot}%{_prefix} INSTALLDIRS=vendor
  ./Build
  ./Build test
fi


%clean
rm -rf %{buildroot}


%install
rm -rf %{buildroot}
if [ -f Makefile.PL ]; then
  make install
elif [ -f Build.PL ]; then
  ./Build install destdir=%{buildroot} create_packlist=0
fi

rm -rf %{buildroot}%{_mandir}/man3/*

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

%{_fixperms} %{buildroot}

find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;

find %{buildroot}%{_prefix} -type f -print | \
        sed "s@^%{buildroot}@@g" | \
        grep -v perllocal.pod | \
        grep -v "\.packlist" > %{pkgname}-%{version}-filelist
if [ "$(cat %{pkgname}-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi


%files -f %{pkgname}-%{version}-filelist
%defattr(-,root,root)


%changelog
* Wed Apr  5 2017 Markus Linnala <Markus.Linnala@cybercom.com> - 0.23-0.0
- initial
