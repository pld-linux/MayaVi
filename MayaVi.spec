Summary:	MayaVi is easy to use scientific data visualizer
Summary(pl):	MayaVi to ³atwe w u¿yciu narzêdzie do wizualizacji danych naukowych
Name:		MayaVi
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/mayavi/%{name}-%{version}.tar.gz
URL:		http://mayavi.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MayaVi is a free, easy to use scientific data visualizer. It is
written in Python and uses the amazing Visualization Toolkit (VTK) for
the graphics. It provides a GUI written using Tkinter. MayaVi is free
and distributed under the GNU GPL. It is also cross platform.

%description -l pl
MayaVi to wolnodostêpne, ³atwe w u¿yciu narzêdzie do wizualizacji
danych naukowych. Jest napisane w Pythonie i u¿ywa do grafiki VTK
(Visualization Toolkit). GUI napisane jest przy u¿yciu Tkinter.

%prep
%setup  -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
