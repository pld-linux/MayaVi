Summary:	MayaVi is easy to use scientific data visualizer.
Name:		MayaVi
Version:	1.1
Release:	1
Group:		Visulatization
Copyright:	GPL
Source0:	http://prdownloads.sourceforge.net/mayavi/MayaVi-1.1.tar.gz
URL:		http://mayavi.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MayaVi is a free, easy to use scientific data visualizer. It is written in Python and uses the amazing Visualization Toolkit (VTK) for
the graphics. It provides a GUI written using Tkinter. MayaVi is free and distributed under the GNU GPL. It is also cross platform.

%prep

%setup  -q


%build

%pre

%preun

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
