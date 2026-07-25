%define modname	HTML-TableExtract
%define modver	2.15

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTML-TableExtract
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSISK/HTML-TableExtract-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)

%description
HTML::TableExtract is a module that simplifies the extraction
of information contained in tables within HTML documents.

Tables of note may be specified using Headers, Depth, Count,
or some combination of the three. See the module documentation
for details.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/HTML
%{_mandir}/man3/*

