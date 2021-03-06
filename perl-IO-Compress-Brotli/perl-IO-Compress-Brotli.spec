# ../common/perl-template IO-Compress-Brotli
#

%define pkgname IO-Compress-Brotli
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}

Name:      perl-%{pkgname}
Summary:   %{pkgname} - Perl module
Version:   0.002001
Release:   0.2%{?dist}
License:   GPL+ or Artistic
Group:     Development/Libraries
Url:       http://search.cpan.org/dist/IO-Compress-Brotli/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:    http://search.cpan.org/CPAN/authors/id/M/MG/MGV/IO-Compress-Brotli-0.002001.tar.gz

%if 0%{?fedora} || 0%{?rhel} > 5
BuildRequires: perl-devel
%endif
%if 0%{?fedora} >= 25
BuildRequires: perl-generators
%endif
%if 0%{?fedora} >= 25
BuildRequires: perl(:VERSION) >= 5.14.0
%else
BuildRequires: perl >= 5.014000
%endif
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)

Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
None.


%prep
%setup -q -n %{pkgname}-%{version}
chmod -R u+w %{_builddir}/%{pkgname}-%{version}
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
* Thu Jan 19 2017 Markus Linnala <Markus.Linnala@cybercom.com> - 0.002001-0.1
- 0.002001
