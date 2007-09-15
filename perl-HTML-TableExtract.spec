%define module	HTML-TableExtract
%define name	perl-%{module}
%define version	2.10
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Buildarch:	noarch
BuildRequires:  perl(HTML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
HTML::TableExtract is a module that simplifies the extraction
of information contained in tables within HTML documents.

Tables of note may be specified using Headers, Depth, Count,
or some combination of the three. See the module documentation
for details.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/HTML
%{_mandir}/*/*

