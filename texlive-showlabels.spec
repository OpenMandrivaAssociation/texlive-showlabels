# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/showlabels
# catalog-date 2009-05-28 00:22:07 +0200
# catalog-license gpl
# catalog-version 1.6.5
Name:		texlive-showlabels
Version:	1.6.5
Release:	5
Summary:	Show label commands in the margin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/showlabels
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.source.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/showlabels/LICENCE
%doc %{_texmfdistdir}/doc/latex/showlabels/README
%doc %{_texmfdistdir}/doc/latex/showlabels/VERSION
%doc %{_texmfdistdir}/doc/latex/showlabels/showlabels.html
%doc %{_texmfdistdir}/doc/latex/showlabels/showlabels.pdf
#- source
%doc %{_texmfdistdir}/source/latex/showlabels/showlabels.dtx
%doc %{_texmfdistdir}/source/latex/showlabels/showlabels.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6.5-2
+ Revision: 755986
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6.5-1
+ Revision: 719529
- texlive-showlabels
- texlive-showlabels
- texlive-showlabels
- texlive-showlabels

