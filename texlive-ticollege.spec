%global tl_name ticollege
%global tl_revision 36306

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Graphical representation of keys on a standard scientific calculator
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/ticollege
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ticollege.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ticollege.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands to draw scientific calculator keys with
the help of TikZ. It also provides commands to draw the content of
screens and of menu items.

