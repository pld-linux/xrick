Summary:	Linux version of Rick Dangerous
Summary(pl):	Wersja Linux starej gry	Rick Dangerous
Name:		xrick
Version:	010808
Release:	1
License:	Unknown
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://www.bigorno.net/%{name}/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-cflags.patch
Icon:		xrick.xpm
URL:		http://www.bigorno.net/%{name}/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

xrick to w³a¶ciwie napisany od nowa Rick Dangerous który zosta³
przeniesiony na Linux, Windows BeOS, Amiga, ...

%prep
%setup -qn xrick
%patch0 -p1

%build
./config
%{__make} OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Games}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
