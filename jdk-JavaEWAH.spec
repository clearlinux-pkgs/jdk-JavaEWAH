Name     : jdk-JavaEWAH
Version  : 0.3.2
Release  : 4
URL      : https://repo1.maven.org/maven2/com/googlecode/javaewah/JavaEWAH/0.3.2/JavaEWAH-0.3.2.jar
Source0  : https://repo1.maven.org/maven2/com/googlecode/javaewah/JavaEWAH/0.3.2/JavaEWAH-0.3.2.jar
Source1  : https://repo1.maven.org/maven2/com/googlecode/javaewah/JavaEWAH/0.3.2/JavaEWAH-0.3.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-JavaEWAH-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-JavaEWAH package.
Group: Data

%description data
data components for the jdk-JavaEWAH package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/JavaEWAH.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/JavaEWAH.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/JavaEWAH.xml \
%{buildroot}/usr/share/maven-poms/JavaEWAH.pom \
%{buildroot}/usr/share/java/JavaEWAH.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/JavaEWAH.jar
/usr/share/maven-metadata/JavaEWAH.xml
/usr/share/maven-poms/JavaEWAH.pom
