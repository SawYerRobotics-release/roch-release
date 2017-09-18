Name:           ros-kinetic-roch-rapps
Version:        2.0.12
Release:        0%{?dist}
Summary:        ROS roch_rapps package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roch_rapps
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-compressed-image-transport
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-robot-pose-publisher
Requires:       ros-kinetic-roch-bringup
Requires:       ros-kinetic-roch-follower
Requires:       ros-kinetic-roch-navigation
Requires:       ros-kinetic-roch-teleop
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-topic-tools
Requires:       ros-kinetic-warehouse-ros
Requires:       ros-kinetic-world-canvas-server
BuildRequires:  ros-kinetic-catkin

%description
The roch_rapps package for set of 'app manager' apps definition

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 2.0.12-0
- Autogenerated by Bloom

* Fri Mar 24 2017 Carl <wzhang@softrobtech.com> - 2.0.11-0
- Autogenerated by Bloom

