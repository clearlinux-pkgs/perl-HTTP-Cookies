#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Cookies
Version  : 6.04
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Cookies-6.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Cookies-6.04.tar.gz
Summary  : 'HTTP cookie jars'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Cookies-license
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
version 6.04
# SYNOPSIS
use HTTP::Cookies;
$cookie_jar = HTTP::Cookies->new(
file => "$ENV{'HOME'}/lwp_cookies.dat",
autosave => 1,
);

%package dev
Summary: dev components for the perl-HTTP-Cookies package.
Group: Development
Provides: perl-HTTP-Cookies-devel

%description dev
dev components for the perl-HTTP-Cookies package.


%package license
Summary: license components for the perl-HTTP-Cookies package.
Group: Default

%description license
license components for the perl-HTTP-Cookies package.


%prep
%setup -q -n HTTP-Cookies-6.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-HTTP-Cookies
cp LICENSE %{buildroot}/usr/share/doc/perl-HTTP-Cookies/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/HTTP/Cookies.pm
/usr/lib/perl5/site_perl/5.26.1/HTTP/Cookies/Microsoft.pm
/usr/lib/perl5/site_perl/5.26.1/HTTP/Cookies/Netscape.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Cookies.3
/usr/share/man/man3/HTTP::Cookies::Microsoft.3
/usr/share/man/man3/HTTP::Cookies::Netscape.3

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-HTTP-Cookies/LICENSE
