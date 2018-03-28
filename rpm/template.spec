Name:           ros-indigo-roch-bringup
Version:        1.0.16
Release:        0%{?dist}
Summary:        ROS roch_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roch_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-astra-launch
Requires:       ros-indigo-depthimage-to-laserscan
Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-freenect-launch
Requires:       ros-indigo-imu-filter-madgwick
Requires:       ros-indigo-imu-transformer
Requires:       ros-indigo-laser-filters
Requires:       ros-indigo-lms1xx
Requires:       ros-indigo-microstrain-3dmgx2-imu
Requires:       ros-indigo-nmea-comms
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-openni2-launch
Requires:       ros-indigo-realsense-camera
Requires:       ros-indigo-rgbd-launch
Requires:       ros-indigo-robot-localization
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roch-base
Requires:       ros-indigo-roch-control
Requires:       ros-indigo-roch-description
Requires:       ros-indigo-roch-safety-controller
Requires:       ros-indigo-roch-sensorpc
Requires:       ros-indigo-rocon-bubble-icons
Requires:       ros-indigo-rosbridge-server
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rplidar-ros
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-zeroconf-avahi
Requires:       scipy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-rospy

%description
Soy roch installation and integration package

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
* Wed Mar 28 2018 Carl <carlzhang@soyrobotics.com> - 1.0.16-0
- Autogenerated by Bloom

* Thu Nov 16 2017 Carl <wzhang@softrobtech.com> - 1.0.15-0
- Autogenerated by Bloom

* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 1.0.14-0
- Autogenerated by Bloom

* Mon May 08 2017 Carl <wzhang@softrobtech.com> - 1.0.13-0
- Autogenerated by Bloom

* Sat Apr 01 2017 Carl <wzhang@softrobtech.com> - 1.0.12-0
- Autogenerated by Bloom

* Thu Mar 23 2017 Carl <wzhang@softrobtech.com> - 1.0.11-0
- Autogenerated by Bloom

* Thu Mar 02 2017 Carl <wzhang@softrobtech.com> - 1.0.10-0
- Autogenerated by Bloom

* Tue Feb 07 2017 Carl <wzhang@softrobtech.com> - 1.0.9-0
- Autogenerated by Bloom

* Mon Jan 23 2017 Carl <wzhang@softrobtech.com> - 1.0.8-0
- Autogenerated by Bloom

* Sun Jan 22 2017 Carl <wzhang@softrobtech.com> - 1.0.7-0
- Autogenerated by Bloom

