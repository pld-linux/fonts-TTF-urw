Summary:	URW fonts in TTF format (e.g. for GhostPCL)
Summary(pl.UTF-8):	Fonty URW w formacie TTF (np. dla GhostPCL-a)
Name:		fonts-TTF-urwfonts
Version:	1.41
Release:	1
License:	Alladin Free Public License
Group:		Fonts
#Source0:	http://mirror.cs.wisc.edu/pub/mirrors/ghost/AFPL/GhostPCL/urwfonts-%{version}.tar.bz2
Source0:	http://www.ctan.org/get/nonfree/support/ghostscript/AFPL/GhostPCL/urwfonts-%{version}.tar.bz2
# Source0-md5:	6d65230fa5e9783a0b5942b55dc5219f
Requires(post,postun):	fontpostinst
Provides:	ghostpcl-urwfonts
Obsoletes:	ghostpcl-urwfonts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URW fonts in TTF format, suitable for GhostPCL.

%description -l pl.UTF-8
Fonty URW w formacie TTF, nadające się dla GhostPCL-a.

%prep
%setup -q -n urwfonts-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF

install *.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_fontsdir}/TTF/A028-*.ttf
%{_fontsdir}/TTF/A030-*.ttf
%{_fontsdir}/TTF/AntiqueOlive-*.ttf
%{_fontsdir}/TTF/ArtLinePrinter.ttf
%{_fontsdir}/TTF/CenturySchL-*.ttf
%{_fontsdir}/TTF/ClarendonURW-*.ttf
%{_fontsdir}/TTF/Coronet.ttf
%{_fontsdir}/TTF/Dingbats.ttf
%{_fontsdir}/TTF/GaramondNo8-*.ttf
%{_fontsdir}/TTF/LetterGothic-*.ttf
%{_fontsdir}/TTF/Mauritius-*.ttf
%{_fontsdir}/TTF/NimbusMonL-*.ttf
%{_fontsdir}/TTF/NimbusMono-*.ttf
%{_fontsdir}/TTF/NimbusRomNo9L-*.ttf
%{_fontsdir}/TTF/NimbusRomanNo4-*.ttf
%{_fontsdir}/TTF/NimbusRomanNo9-*.ttf
%{_fontsdir}/TTF/NimbusSanL-*.ttf
%{_fontsdir}/TTF/StandardSymL.ttf
%{_fontsdir}/TTF/U001-*.ttf
%{_fontsdir}/TTF/U001Con-*.ttf
%{_fontsdir}/TTF/URWBookmanL-*.ttf
%{_fontsdir}/TTF/URWChanceryL-*.ttf
%{_fontsdir}/TTF/URWClassico-*.ttf
%{_fontsdir}/TTF/URWGothicL-*.ttf
%{_fontsdir}/TTF/URWPalladioL-*.ttf
