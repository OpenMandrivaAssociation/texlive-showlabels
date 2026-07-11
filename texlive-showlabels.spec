%global tl_name showlabels
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9.3
Release:	%{tl_revision}.1
Summary:	Show label commands in the margin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/showlabels
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showlabels.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package helps you keep track of all the labels you define, by
putting the name of new labels into the margin whenever the \label
command is used. The package allows you to do the same thing for other
commands. The only one for which this is obviously useful is the \cite
command, but it's easy to do it for others, such as the \ref or \begin
commands.

