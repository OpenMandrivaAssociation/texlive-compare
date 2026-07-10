%global tl_name compare
%global tl_revision 54265

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Compare two strings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/misc/compare.tex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/compare.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The file defines a macro \compare, which takes two arguments; the macro
expands to -1, 0, 1, according as the first argument is less than, equal
to, or greater than the second argument. Sorting is alphabetic, using
ASCII collating order.

