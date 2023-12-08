%global _empty_manifest_terminate_build 0
Name:		python-pygit2
Version:	1.7.2
Release:	1
Summary:	Python bindings for libgit2.
License:	GNU General Public License v2.0 only
URL:		https://github.com/libgit2/pygit2
Source0:	https://files.pythonhosted.org/packages/e8/78/15417f51306f6870de37517c5315c1282d001dbc537fe1eb2df40f99a97b/pygit2-1.7.2.tar.gz


%description
- Documentation - http://www.pygit2.org/
- Install - http://www.pygit2.org/install.html
- Download - https://pypi.python.org/pypi/pygit2
- Source code and issue tracker - https://github.com/libgit2/pygit2
- Changelog - https://github.com/libgit2/pygit2/blob/master/CHANGELOG.rst
- Authors - https://github.com/libgit2/pygit2/blob/master/AUTHORS.rst

%package -n python3-pygit2
Summary:	Python bindings for libgit2.
Provides:	python-pygit2
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pip
BuildRequires:	python3-cffi
BuildRequires:	libgit2-devel
BuildRequires:	gcc
BuildRequires:	gdb
%description -n python3-pygit2
- Documentation - http://www.pygit2.org/
- Install - http://www.pygit2.org/install.html
- Download - https://pypi.python.org/pypi/pygit2
- Source code and issue tracker - https://github.com/libgit2/pygit2
- Changelog - https://github.com/libgit2/pygit2/blob/master/CHANGELOG.rst
- Authors - https://github.com/libgit2/pygit2/blob/master/AUTHORS.rst

%package help
Summary:	Development documents and examples for pygit2
Provides:	python3-pygit2-doc
%description help
- Documentation - http://www.pygit2.org/
- Install - http://www.pygit2.org/install.html
- Download - https://pypi.python.org/pypi/pygit2
- Source code and issue tracker - https://github.com/libgit2/pygit2
- Changelog - https://github.com/libgit2/pygit2/blob/master/CHANGELOG.rst
- Authors - https://github.com/libgit2/pygit2/blob/master/AUTHORS.rst

%prep
%autosetup -n pygit2-1.7.2

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-pygit2 -f filelist.lst
%dir %{python3_sitearch}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Dec 7 2023 lichaoran <pkwarcraft@hotmail.com> - 1.7.2-1
- Upgrade to 1.7.2
* Mon Mar 27 2023 Python_Bot <Python_Bot@openeuler.org> - 1.7.1-1
- Package Spec generated
