%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Validate
Summary:	CGI::Validate perl module
Summary(pl):	Modu³ perla CGI::Validate
Name:		perl-CGI-Validate
Version:	2.000
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1a11020856521d3c498dc0c1628abdf
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Validate - Advanced CGI form parser and type validation.

%description -l pl
CGI::Validate - zaawansowany parser CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/Validate.pm
%{_mandir}/man3/*
