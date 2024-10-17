Name:		texlive-compare
Version:	54265
Release:	2
Summary:	Compare two strings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/compare
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/compare.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file defines a macro \compare, which takes two arguments;
the macro expands to -1, 0, 1, according as the first argument
is less than, equal to, or greater than the second argument.
Sorting is alphabetic, using ASCII collating order.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/compare

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
