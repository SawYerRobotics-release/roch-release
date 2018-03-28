Name:           ros-indigo-roch-follower
Version:        1.0.16
Release:        0%{?dist}
Summary:        ROS roch_follower package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roch_follower
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-depth-image-proc
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roch-bringup
Requires:       ros-indigo-roch-msgs
Requires:       ros-indigo-roch-teleop
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-topic-tools
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-depth-image-proc
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roch-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-visualization-msgs

%description
Follower for the roch. Follows humans and robots around by following the
centroid of a box points in front of the roch.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Mar 28 2018 Carl <wzhang@softrobetch.com> - 1.0.16-0
- Autogenerated by Bloom

* Thu Nov 16 2017 Carl <wzhang@softrobetch.com> - 1.0.15-0
- Autogenerated by Bloom

* Mon Sep 18 2017 Carl <wzhang@softrobetch.com> - 1.0.14-0
- Autogenerated by Bloom

* Mon May 08 2017 Carl <wzhang@softrobetch.com> - 1.0.13-0
- Autogenerated by Bloom

* Sat Apr 01 2017 Carl <wzhang@softrobetch.com> - 1.0.12-0
- Autogenerated by Bloom

* Thu Mar 23 2017 Carl <wzhang@softrobetch.com> - 1.0.11-0
- Autogenerated by Bloom

* Thu Mar 02 2017 Carl <wzhang@softrobetch.com> - 1.0.10-0
- Autogenerated by Bloom

* Tue Feb 07 2017 Carl <wzhang@softrobetch.com> - 1.0.9-0
- Autogenerated by Bloom

* Mon Jan 23 2017 Carl <wzhang@softrobetch.com> - 1.0.8-0
- Autogenerated by Bloom

* Sun Jan 22 2017 Carl <wzhang@softrobetch.com> - 1.0.7-0
- Autogenerated by Bloom

