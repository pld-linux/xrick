Summary:	Linux version of Rick Dangerous
Summary(pl):	Wersja Linux starej gry	Rick Dangerous
Name:		xrick
Version:	021212
Release:	2
License:	Unknown
Group:		X11/Applications/Games
Source0:	http://www.bigorno.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	615190051481266710cb43ecd1fe930c
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-cflags.patch
Icon:		xrick.xpm
URL:		http://www.bigorno.net/xrick/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Way before Lara Croft, back in the 1980's and early 1990's, Rick
Dangerous was the Indiana Jones of computer games, running away from
rolling rocks, avoiding traps, from South America to a futuristic
missile base via Egypt and the Schwarzendumpf castle. The game was
released for the Atari ST, the IBM PC, and many more platforms.

xrick is a complete rewrite of Rick Dangerous, and has been ported to
Linux, Windows, BeOs, Amiga, ...

%description -l pl
D³ugo zanim pojawi³a siê Lara Croft, w latach 80-tych i w pocz±tku
90-tych, Rick Dangerous by³ Indiana Jones'em gier komputerowych,
uciekaj±c przed tocz±cymi siê kamieniami, unikaj±c pu³apek, od
Po³udniowej Ameryki do futurystycznej bazy rakietowej, przez Egipt i
zamek Schwarzendumpf. Gra by³a wydana dla Atari ST, IBM PC i wiele
innych platform.

xrick to w³a¶ciwie napisany od nowa Rick Dangerous, który zosta³
przeniesiony na Linuksa, Windows, BeOS, Amigê...

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" DATADIR="%{_datadir}/%{name}/" %{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_datadir}/%{name},%{_mandir}/man6}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install data.zip $RPM_BUILD_ROOT%{_datadir}/%{name}
gunzip xrick.6.gz
install xrick.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
%{_mandir}/man6
