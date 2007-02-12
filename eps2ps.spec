%include	/usr/lib/rpm/macros.perl
Summary:	Converts Encapsulated Postscript (*.eps) files to Postscript (.ps)
Summary(pl.UTF-8):	Konwertuje pliki .eps do Postscriptu (.ps)
Name:		eps2ps
Version:	1.0
Release:	2
License:	Public Domain
Group:		Applications/Publishing
Source0:	http://geoscope.ipgp.jussieu.fr/~gaboret/%{name}
# Source0-md5:	b5bda8a611635f3813f51c4d86669c07
Patch0:		%{name}-perl-path.patch
Patch1:		%{name}-no-author.patch
URL:		http://geoscope.ipgp.jussieu.fr/~gaboret/liens.html
BuildRequires:	perl-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eps2ps converts Encapsulated Postscript (*.eps) files to Postscript
(.ps) format.

%description -l pl.UTF-8
eps2ps konwertuje format plików EPS do Postscriptu (.ps).

%prep
%setup -q -c -T
install %{SOURCE0} .
%patch0 -p1
%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
