# TODO:
# - fails on start:
#   CEGUI::Exception: DynamicModule::DynamicModule - Failed to load module
#         'libCEGUIFreeImageImageCodec.so': libCEGUIFreeImageImageCodec.so:
#          cannot open shared object file: No such file or directory
#   CEGUI Exception occurred : DynamicModule::DynamicModule - Failed to load module
#   'libCEGUIFreeImageImageCodec.so': libCEGUIFreeImageImageCodec.so:
#   cannot open shared object file: No such file or directory
#   lib is on libCEGUIFreeImageImageCodec.so.0 - anybody could help with this?
# - pl summary, description and comment (in .desktop)
# - music pack: http://downloads.sourceforge.net/smclone/SMC_music_4.0_high.zip
Summary:	A jump-and-run game similar to classic sidescroller games
Summary(pl.UTF-8):	Gra typu "skacz i biegnij" podobna do klasycznych przewijanych gier
Name:		smc
Version:	1.5
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/smclone/%{name}-%{version}.tar.bz2
# Source0-md5:	72d10648435c349988dcd053e5fe64fe
Source1:	%{name}.desktop
URL:		http://www.secretmaryo.org/
BuildRequires:	CEGUI-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secret Maryo Chronicles is an Open Source two-dimensional platform
game with a style designed similar to classic sidescroller games. It
uses the platform independent library SDL and, since version 0.98, the
OpenGL accelerated Graphics Renderer. The game is developed in C++.

%description -l pl.UTF-8
Secret Maryo Chronicles to mająca otwarty kod źródłowy dwuwymiarowa
gra platformowa w stylu podobnym do klasycznych gier z przewijanym
ekranem. Wykorzystuje niezależną od platformy bibliotekę SDL oraz, od
wersji 0.98, renderer graficzny z akceleracją OpenGL. Gra jest
tworzona w C++.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# desktop file
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# icon
cp -f data/icon/window_32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
