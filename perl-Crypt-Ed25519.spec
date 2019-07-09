#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Ed25519
Summary:	Crypt::Ed25519 - Perl Ed25519 public key module
Name:		perl-Crypt-Ed25519
Version:	1.04
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4dff45eb3794fb16a2d0d19ca336cd8e
URL:		http://search.cpan.org/dist/Crypt-Ed25519/
BuildRequires:	perl-Canary-Stability
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements Ed25519 public key generation, message signing
and verification. It is a pretty bare-bones implementation that
implements the standard Ed25519 variant with SHA512 hash, as well as
a slower API compatible with the upcoming EdDSA RFC.

The security target for Ed25519 is to be equivalent to 3000 bit RSA or
AES-128.

The advantages of Ed25519 over most other signing algorithms are:
- small public/private key and signature sizes (<= 64 octets),
- good key generation, signing and verification performance,
- no reliance on random number generators for signing,
- by-design immunity against branch or memory access pattern
  side-channel attacks.

More detailed praise and other info can be found at
http://ed25519.cr.yp.to/index.html

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
PERL_CANARY_STABILITY_NOPROMPT=1 %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorarch}/Crypt/Ed25519.pm
%dir %{perl_vendorarch}/auto/Crypt/Ed25519
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Ed25519/Ed25519.so
%{_mandir}/man3/Crypt::Ed25519.3pm*
