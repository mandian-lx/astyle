%define major 3
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Reindenter and reformatter of C++, C and Java source code
Name:		astyle
Version:	3.0.1
Release:	1
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
    
%install
%makeinstall_std -C build/clang

