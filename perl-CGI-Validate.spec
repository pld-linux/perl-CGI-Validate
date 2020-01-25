#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	CGI
%define		pnam	Validate
Summary:	CGI::Validate - advanced CGI form parser and type validation
Summary(pl.UTF-8):	CGI::Validate - zaawansowany analizator formularzy CGI z walidacją typów
Name:		perl-CGI-Validate
Version:	2.000
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1a11020856521d3c498dc0c1628abdf
URL:		http://search.cpan.org/dist/CGI-Validate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Validate Perl module is an advanced CGI form parser and type
validator. The basic concept of this module is to combine the best
features of the CGI and Getopt::Long modules.

%description -l pl.UTF-8
Moduł Perla CGI::Validate jest zaawansowany analizatorem formularzy
CGI z walidacją typów. Podstawową ideą tego modułu jest połączenie
najlepszych cech modułów CGI i Getopt::Long.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/Validate.pm
%{_mandir}/man3/*
