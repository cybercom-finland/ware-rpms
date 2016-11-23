# ../common/perl-template Socket-Mmsg
#

%define pkgname Socket-Mmsg
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}

Name:      perl-%{pkgname}
Summary:   %{pkgname} - Perl module
Version:   0.02
Release:   2.0%{?dist}
License:   GPL+ or Artistic
Group:     Development/Libraries
Url:       http://search.cpan.org/dist/Socket-Mmsg/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:    http://search.cpan.org/CPAN/authors/id/H/HI/HITHIM/Socket-Mmsg-0.02.tar.gz
Patch1:    try.patch

%if 0%{?fedora} || 0%{?rhel} > 5
BuildRequires: perl-devel
%endif
%if 0%{?fedora} >= 25
BuildRequires: perl-generators
%endif
BuildRequires: perl
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker)

Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
None.


%prep
%setup -q -n %{pkgname}
%patch1 -p1
chmod -R u+w %{_builddir}/%{pkgname}
[ -f Makefile.PL ] && perl -pi -e 's/^auto_install\;//' Makefile.PL


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
* Wed Nov 23 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.02-2.0
- fix spec to support F25

* Mon Nov 21 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.02-1.0
- 0.02 with local patch
