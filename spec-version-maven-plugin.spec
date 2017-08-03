%{?scl:%scl_package spec-version-maven-plugin}
%{!?scl:%global pkg_name %{name}}

Name:          %{?scl_prefix}spec-version-maven-plugin
Version:       1.2
Release:       9.2%{?dist}
Summary:       Spec Version Maven Plugin
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/spec-version-maven-plugin-1.2
# tar czf spec-version-maven-plugin-1.2-src-svn.tar.gz spec-version-maven-plugin-1.2
Source0:       %{pkg_name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# spec-version-maven-plugin package don't include the license file
Source1:       glassfish-LICENSE.txt


BuildRequires: %{?scl_prefix}mvn(net.java:jvnet-parent:pom:)
BuildRequires: %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires: %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires: %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires: %{?scl_prefix}mvn(org.codehaus.plexus:plexus-resources)

# test dep
BuildRequires: %{?scl_prefix}mvn(junit:junit)
BuildRequires: %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)

BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}maven-plugin-build-helper
BuildRequires: %{?scl_prefix}maven-plugin-plugin

BuildArch:     noarch

%description
Maven Plugin to configure APIs version and
specs in a MANIFEST.MF file.

%package javadoc
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q

sed -i "s|mvn|mvn-rpmbuild|" src/main/resources/checkVersion.sh

cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%mvn_file :%{pkg_name} %{pkg_name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.2-9.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.2-9.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.2-6
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 02 2013 gil cattaneo <puntogil@libero.it> 1.2-2
- build with XMvn
- minor changes to adapt to current guideline

* Wed May 22 2013 gil cattaneo <puntogil@libero.it> 1.2-1
- initial rpm
