%include	/usr/lib/rpm/macros.perl
Summary:	converts Encapsulated Postscript (*.eps) files to Postscript (.ps)
Summary(pl):	konwertuje pliki .eps do Postscriptu (.ps)
Name:		eps2ps
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(es):	Aplicaciones/Editoración
Group(pl):	Aplikacje/Publikowanie
Group(pt_BR):	Aplicações/Editoração
Source0:	http://geoscope.ipgp.jussieu.fr/~gaboret/%{name}
Patch0:		%{name}-perl-path.patch
URL:		http://geoscope.ipgp.jussieu.fr/~gaboret/liens.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eps2ps converts Encapsulated Postscript (*.eps) files to Postscript
(.ps) format.

%description -l pl
eps2ps konwertuje format plików EPS do Postscriptu (.ps).

%prep
%setup -q -c -T
install %{SOURCE0} .
patch -p1 < %{PATCH0}

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
