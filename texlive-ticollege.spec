Name:		texlive-ticollege
Version:	36306
Release:	2
Summary:	Graphical representation of keys on a standard scientific calculator
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ticollege
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ticollege.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ticollege.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands to draw scientific calculator
keys with the help of TikZ. It also provides commands to draw
the content of screens and of menu items.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ticollege
%doc %{_texmfdistdir}/doc/latex/ticollege

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
