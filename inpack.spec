[project]
name = jenkins
version = 2.89.2
vendor = jenkins.io
homepage = https://jenkins.io
groups = app/dev,app/prod
description = continuous integration tool for software development


%build
PREFIX="{{.project__prefix}}"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "jenkins-{{.project__version}}.war" ]; then
	wget "http://mirrors.jenkins.io/war-stable/{{.project__version}}/jenkins.war" -O jenkins-{{.project__version}}.war
fi

install jenkins-{{.project__version}}.war {{.buildroot}}/jenkins.war

mkdir -p {{.buildroot}}/var/log

%files

