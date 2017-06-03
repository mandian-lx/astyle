%define major 3
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Reindenter and reformatter of C++, C and Java source code
Name:		astyle
Version:	3.0.1
Release:	0
License:	MIT
Group:		Development/C++
Url:		http://astyle.sourceforge.net/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}_%{version}_linux.tar.gz
Patch0:		%{name}-3.0.1-shared.patch
# Required by arduino, adapted from
#   https://raw.githubusercontent.com/arduino/astyle/master/patches/java_package_name.patch
Patch1:		%{name}-3.0.1-arduino.patch

%description
Artistic Style is a series of filters that automatically reindent and reformat
C/C++/Java source files. These can be used from a command line, or they can be
incorporated as classes in another C++ program.

%files
%{_bindir}/astyle
%doc doc/*
%doc README.md
%doc LICENSE.md

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Software for programming Atmel AVR Microcontroller
Group:		System/Libraries

%description -n %{libname}
Artistic Style is a series of filters that automatically reindent and reformat
C/C++/Java source files. These can be used from a command line, or they can be
incorporated as classes in another C++ program.

This package contains the shared library.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*
%doc LICENSE.md

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers, libraries and docs for the %{name} library
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides development files for %{name} library.

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%doc LICENSE.md

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}

# Apply all patches
%patch0 -p1 -b .shared
%patch1 -p1 -b .arduino

# fix spurious-executable-perm
chmod a-x *.md
chmod a-x doc/*
chmod a-x src/*

%build
%setup_compile_flags
%make -C build/clang astylesjd

# it's much easier to compile it here than trying to fix the Makefile
#    g++ $RPM_OPT_FLAGS -DASTYLE_LIB -DASTYLE_JNI -fPIC -I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -c ASBeautifier.cpp ASEnhancer.cpp ASFormatter.cpp ASResource.cpp astyle_main.cpp
#    g++ -shared -o libastyle.so.%{soversion} *.o -Wl,-soname,libastyle.so.%{majorversion}
#    ln -s libastyle.so.%{soversion} libastyle.so
#    g++ $RPM_OPT_FLAGS -c ASLocalizer.cpp astyle_main.cpp
#	    g++ $RPM_OPT_FLAGS -o astyle ASLocalizer.o astyle_main.o -L. -lastyle
    
%install
%makeinstall_std -C build/clang

# bin
#install -dm 0755 %{buildroot}%{_bindir}/
#install -pm 0755 build/clang/bin/%{name} %{buildroot}%{_bindir}/

# header
#install -dm 0755 %{buildroot}%{_includedir}/
#install -pm 0644 src/%{name}.h %{buildroot}%{_includedir}/

# lib
#install -dm 0755 %{buildroot}%{_libdir}/
#install -pm 0755 build/clang/bin/lib%{name}.so.* %{buildroot}%{_libdir}/
#ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so

