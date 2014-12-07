%define modname	HTML-TableExtract
%define modver	2.11

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version 2.11
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-TableExtract-2.11.tar.gz
BuildArch:	noarch
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

