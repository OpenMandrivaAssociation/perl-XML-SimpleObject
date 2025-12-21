%define upstream_name    XML-SimpleObject
%define upstream_version 0.53

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Perl extension allowing a simple(r) object representation of an XML::LibXML DOM object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch: noarch
BuildRequires:	make
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(XML::Parser)
BuildRequires: perl-XML-LibXML

%description
This is a short and simple class allowing simple object access to a parsed
XML::Parser tree, with methods for fetching children and attributes in as
clean a manner as possible. My apologies for further polluting the XML::
space; this is a small and quick module, with easy and compact usage. See
XML::SimpleObject::LibXML for the same interface for XML::LibXML.

%prep
%autosetup -p1 -n %{upstream_name}%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README
%doc %{_mandir}/man3/*
%perl_vendorlib/*
