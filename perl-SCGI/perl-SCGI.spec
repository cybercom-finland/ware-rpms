# ../common/perl-template -dist=RHEL-7 SCGI
#

%define pkgname SCGI
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}

Name:      perl-%{pkgname}
Summary:   %{pkgname} - Perl module
Version:   0.6
Release:   2.0%{?dist}
License:   GPL+ or Artistic
Group:     Development/Libraries
Url:       http://search.cpan.org/dist/SCGI/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Buildarch: noarch
Source:    http://search.cpan.org/CPAN/authors/id/V/VI/VIPERCODE/SCGI-0.6.tar.gz

%if 0%{?fedora} >= 25
BuildRequires: perl-generators
%endif
%if 0%{?fedora} >= 27
BuildRequires: perl-interpreter >= 5.8.0
%else
%if 0%{?fedora} >= 25
BuildRequires: perl(:VERSION) >= 5.8.0
%else
BuildRequires: perl >= 5.8.0
%endif
%endif
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildRequires: perl(JSON::PP) >= 2.27300

Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
None.


%prep
%setup -q -n %{pkgname}-%{version}
chmod -R u+w %{_builddir}/%{pkgname}-%{version}
[ -f Makefile.PL ] && perl -pi -e 's/^auto_install\;//' Makefile.PL


%build
#breaks epel7
## No clean network
#export PERL_CORE=1
if [ -f Makefile.PL ]; then
  #CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL destdir=%{buildroot} INSTALLDIRS=vendor
  CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=%{buildroot}%{_prefix} INSTALLDIRS=vendor
  make
  make test
elif [ -f Build.PL ]; then
  CFLAGS="$RPM_OPT_FLAGS" perl Build.PL --prefix=%{buildroot}%{_prefix} --installdirs=vendor
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
* Tue Mar 13 2018 Markus Linnala <Markus.Linnala@cybercom.com> - 0.6-2.0
- f27

* Wed Nov 23 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.6-1.0
- fix spec to support F25

* Tue Nov 22 2016 Markus Linnala <Markus.Linnala@cybercom.com> - 0.6-0.0
- 0.6
