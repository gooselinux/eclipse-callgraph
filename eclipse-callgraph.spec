%global src_repo_tag   R0_5_0
%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_libdir}/eclipse/dropins/callgraph
%global debug_package %{nil}

Name:           eclipse-callgraph
Version:        0.5.0
Release:        1%{?dist}
Summary:        C/C++ Call Graph Visualization Tool

Group:          Development/Tools
License:        EPL
URL:            http://eclipse.org/linuxtools
# sh %{name}-fetch-src.sh
Source0:        %{name}-fetched-src-%{src_repo_tag}.tar.bz2
Source1:        %{name}-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if 0%{?rhel} >= 6
ExclusiveArch: i686 x86_64
%else
ExcludeArch:    ppc64
%endif

BuildRequires: eclipse-cdt
BuildRequires: eclipse-gef
BuildRequires: eclipse-pde
BuildRequires: eclipse-linuxprofilingframework >= 0.3.0-5
Requires: systemtap
Requires: eclipse-gef
Requires: eclipse-cdt
Requires: eclipse-linuxprofilingframework >= 0.3.0-5

%description
Graphically displays the call hierarchy from executing a C/C++ binary, along
with various other runtime statistics.

%prep
%setup -q -n %{name}-fetched-src-%{src_repo_tag}

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.linuxtools.callgraph \
 -d "cdt gef linuxprofilingframework"

%install
#installs to /usr/lib/eclipse/callgraph due to dependency on eclipse-
#linuxprofilingframework, which depends on architecture.
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.callgraph.zip 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc org.eclipse.linuxtools.callgraph-feature/epl-v10.html

%changelog
* Fri Mar 19 2010 Jeff Johnston <jjohnstn@redhat.com> 0.5.0-1
- Resolves: #575108
- Rebase to Linux tools 0.5 release.

* Fri Jan 08 2010 Jeff Johnston <jjohnstn@redhat.com> 0.4.0-2
- Resolves: #553288
- Only support i686, x86_64 for RHEL6 and above.

* Mon Nov 23 2009 Charley Wang <chwang@redhat.com> 0.4.0-1
- Update to version 0.4 of Linux Tools Project and remove tests feature

* Fri Sep 25 2009 Charley Wang <chwang@redhat.com> 0.0.1-3
- Added ExcludeArch for ppc64 because eclipse-cdt is not present

* Thu Sep 24 2009 Roland Grunberg <rgrunber@redhat.com> 0.0.1-2
- Some more changes to spec file

* Thu Sep 24 2009 Charley Wang <chwang@redhat.com> 0.0.1-1
- Make minor changes to spec file

* Thu Sep 24 2009 Charley Wang <chwang@redhat.com> 0.0.1-1
- Initial creation of eclipse-callgraph
