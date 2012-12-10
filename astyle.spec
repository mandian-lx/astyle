Name:           astyle
Version:        2.02.1
Release:        %mkrel 1
Epoch:          0
Summary:        Reindenter and reformatter of C++, C and Java source code
License:        LGPLv3+
Group:          Development/C
URL:            http://astyle.sourceforge.net/
Source0:        http://internap.dl.sourceforge.net/sourceforge/astyle/astyle_%{version}_linux.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Artistic Style is a series of filters that automatically reindent and reformat
C/C++/Java source files. These can be used from a command line, or they can be
incorporated as classes in another C++ program.

%prep
%setup -q -n astyle

%build
(cd build/gcc && %{make} CFLAGS="%{optflags}")

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__install -m 0755 build/gcc/bin/astyle %{buildroot}%{_bindir}/astyle

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc doc/*
%attr(0755,root,root) %{_bindir}/astyle


%changelog
* Mon Jan 09 2012 Andrey Bondrov <abondrov@mandriva.org> 0:2.02.1-1
+ Revision: 758758
- New version 2.02.1

* Wed Sep 28 2011 Andrey Bondrov <abondrov@mandriva.org> 0:2.02-1
+ Revision: 701722
- New version: 2.02

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.24-3mdv2011.0
+ Revision: 610002
- rebuild

* Sun Feb 21 2010 Emmanuel Andry <eandry@mandriva.org> 0:1.24-2mdv2010.1
+ Revision: 509254
- bump releadse
- New version 1.24

* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 0:1.23-1mdv2010.0
+ Revision: 384157
- update to new version 1.23
- fix license (LGPLv3+)

* Sat Aug 23 2008 Emmanuel Andry <eandry@mandriva.org> 0:1.22-1mdv2009.0
+ Revision: 275258
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 04 2007 David Walluck <walluck@mandriva.org> 0:1.21-1mdv2008.0
+ Revision: 78903
- 1.21


* Fri Mar 09 2007 David Walluck <walluck@mandriva.org> 1.20.2-1mdv2007.1
+ Revision: 138632
- 1.20.2

  + Lenny Cartier <lenny@mandriva.com>
    - Import astyle

* Fri Jul 14 2006 Lenny Cartier <lenny@mandriva.com> 1.15.3-5mdv2007.0
- rebuild

* Tue Jul 06 2004 Michael Scherer <misc@mandrake.org> 1.15.3-4mdk 
- rebuild for new gcc, added patch4

