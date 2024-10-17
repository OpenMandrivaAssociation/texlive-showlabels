Name:		texlive-showlabels
Version:	63940
Release:	2
Summary:	Show label commands in the margin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/showlabels
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package helps you keep track of all the labels you define,
by putting the name of new labels into the margin whenever the
\label command is used. The package allows you to do the same
thing for other commands. The only one for which this is
obviously useful is the \cite command, but it's easy to do it
for others, such as the \ref or \begin commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/showlabels/showlabels.sty
%doc %{_texmfdistdir}/doc/latex/showlabels/README
%doc %{_texmfdistdir}/doc/latex/showlabels/VERSION
%doc %{_texmfdistdir}/doc/latex/showlabels/lppl.txt
%doc %{_texmfdistdir}/doc/latex/showlabels/showlabels.html
%doc %{_texmfdistdir}/doc/latex/showlabels/showlabels.pdf
%doc %{_texmfdistdir}/doc/latex/showlabels/style.css
#- source
%doc %{_texmfdistdir}/source/latex/showlabels/showlabels.drv
%doc %{_texmfdistdir}/source/latex/showlabels/showlabels.dtx
%doc %{_texmfdistdir}/source/latex/showlabels/showlabels.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
