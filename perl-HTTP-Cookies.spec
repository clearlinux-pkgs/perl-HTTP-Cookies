#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Cookies
Version  : 6.10
Release  : 47
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Cookies-6.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Cookies-6.10.tar.gz
Summary  : 'HTTP cookie jars'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Cookies-license = %{version}-%{release}
Requires: perl-HTTP-Cookies-perl = %{version}-%{release}
Requires: perl(HTTP::Date)
Requires: perl(HTTP::Headers::Util)
Requires: perl(HTTP::Request)
Requires: perl(HTTP::Response)
Requires: perl(URI)
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Headers::Util)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(URI)

%description
# NAME
HTTP::Cookies - HTTP cookie jars
# VERSION
version 6.10
# SYNOPSIS
use HTTP::Cookies;
$cookie_jar = HTTP::Cookies->new(
file => "$ENV{'HOME'}/lwp_cookies.dat",
autosave => 1,
);

%package dev
Summary: dev components for the perl-HTTP-Cookies package.
Group: Development
Provides: perl-HTTP-Cookies-devel = %{version}-%{release}
Requires: perl-HTTP-Cookies = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Cookies package.


%package license
Summary: license components for the perl-HTTP-Cookies package.
Group: Default

%description license
license components for the perl-HTTP-Cookies package.


%package perl
Summary: perl components for the perl-HTTP-Cookies package.
Group: Default
Requires: perl-HTTP-Cookies = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Cookies package.


%prep
%setup -q -n HTTP-Cookies-6.10
cd %{_builddir}/HTTP-Cookies-6.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Cookies
cp %{_builddir}/HTTP-Cookies-6.10/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Cookies/eb09e0794884964a58f01de18444c634cfa7a0af
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
## Remove excluded files
rm -f %{buildroot}*/usr/lib/perl5/vendor_perl/*/HTTP/Cookies/Microsoft.pm
rm -f %{buildroot}*/usr/share/man/man3/HTTP::Cookies::Microsoft.3

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Cookies.3
/usr/share/man/man3/HTTP::Cookies::Netscape.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Cookies/eb09e0794884964a58f01de18444c634cfa7a0af

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
