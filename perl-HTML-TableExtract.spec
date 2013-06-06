%define upstream_name	 HTML-TableExtract
%define upstream_version 2.11
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.11
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-TableExtract-2.11.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildArch:	noarch

%description
HTML::TableExtract is a module that simplifies the extraction
of information contained in tables within HTML documents.

Tables of note may be specified using Headers, Depth, Count,
or some combination of the three. See the module documentation
for details.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*

%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.100.0-1mdv2010.0
+ Revision: 407769
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.10-4mdv2009.0
+ Revision: 257203
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.10-2mdv2008.1
+ Revision: 135847
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild


* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 14:51:24 (59605)
- 2.10

* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 14:46:38 (59604)
Import perl-HTML-TableExtract

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.09-1mdv2007.0
- New version 2.09

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.08-1mdv2007.0
- New release 2.08
- better source URL

* Fri Mar 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.07-1mdk
- 2.07

* Mon Nov 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.06-1mdk
- 2.06

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.05-2mdk
- Fix BuildRequires

* Fri Oct 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-1mdk 
- new version
- spec cleanup
- rpmbuildupdate aware
- enable tests

* Wed Sep 07 2005 Olivier Thauvin <nanardon@mandriva.org> 2.04-1mdk
- 2.04

* Tue Mar 29 2005 Olivier Thauvin <nanardon@mandrake.org> 1.10-1mdk
- 1.10

* Wed Feb 11 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.08-2mdk
- own %%{perl_vendorlib}/HTML


