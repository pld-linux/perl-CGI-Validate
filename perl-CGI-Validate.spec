%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Validate
Summary:	CGI-Validate perl module
Summary(pl):	Modu³ perla CGI-Validate
Name:		perl-CGI-Validate
Version:	2.000
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Validate - Advanced CGI form parser and type validation.

%description -l pl
CGI-Validate - zaawansowany parser CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/Validate.pm
%{_mandir}/man3/*
