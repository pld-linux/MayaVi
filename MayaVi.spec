Summary:	MayaVi is easy to use scientific data visualizer
Summary(pl):	MayaVi to ³atwe w u¿yciu narzêdzie do wizualizacji danych naukowych
Name:		MayaVi
Version:	1.5
Release:	1
License:	BSD
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/mayavi/%{name}-%{version}.tar.gz
# Source0-md5:	494a29e38b9e808157bae9daaf9fe044
URL:		http://mayavi.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-devel
Requires:	python-tkinter
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
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root $RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/guide/*.html doc/CREDITS.txt doc/NEWS.txt doc/README.txt doc/TODO.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/mayavi
%{py_sitescriptdir}/vtkPipeline
