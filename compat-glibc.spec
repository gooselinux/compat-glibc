%define glibcdate 20061008T1257
%define glibcname glibc-2.5
%define glibcsrcdir glibc-2.5-20061008T1257
%define glibc_release_tarballs 0
%define glibcversion 2.5
%define glibcrelease 46.2
%define auxarches noarch
%define xenarches noarch
%define buildxen 0
%define xenpackage 0
%define buildpower6 0
%define rtkaioarches noarch
%define debuginfocommonarches noarch
%define _unpackaged_files_terminate_build 0
%undefine _enable_debug_packages
Summary: Compatibility C library
Name: compat-glibc
Epoch: 1
Version: %{glibcversion}
Release: %{glibcrelease}
License: LGPLv2+ and LGPLv2+ with exceptions and GPLv2+
Group: Development/Libraries
Source0: %{glibcsrcdir}.tar.bz2
%if %{glibc_release_tarballs}
Source1: %(echo %{glibcsrcdir} | sed s/glibc-/glibc-linuxthreads-/).tar.bz2
Source2: %(echo %{glibcsrcdir} | sed s/glibc-/glibc-libidn-/).tar.bz2
%define glibc_release_unpack -a1 -a2
%endif
Source3: %{glibcname}-fedora-%{glibcdate}.tar.bz2
Source4: dummylib.sh
Patch0: %{glibcname}-fedora.patch
Patch1: glibc-ia64-lib64.patch
Patch2: glibc-bz3352.patch
Patch3: glibc-bz3369.patch
Patch4: glibc-i386-syscall6.patch
Patch6: glibc-rh211116.patch
Patch7: glibc-bz3429.patch
Patch8: glibc-bz3451.patch
Patch9: glibc-nptl_db-dtvp.patch
Patch10: glibc-r_debug-r_map.patch
Patch11: glibc-rh213656.patch
Patch12: glibc-rh214569.patch
Patch13: glibc-strxfrm.patch
Patch14: glibc-sysconf-intel-core-duo.patch
Patch15: glibc-tzfile64.patch
Patch16: glibc-bz3320.patch
Patch17: glibc-bz3559.patch
Patch18: glibc-mai_IN.patch
Patch19: glibc-po-update.patch
Patch20: glibc-powerpc-cpu-addon-update.patch
Patch21: glibc-rh215572.patch
Patch22: glibc-bz3632.patch
Patch23: glibc-memusage.patch
Patch24: glibc-nis+-getenv.patch
Patch25: glibc-rh206483.patch
Patch26: glibc-rh218276.patch
Patch27: glibc-rh218782.patch
Patch28: glibc-rh218802.patch
Patch29: glibc-strtod.patch
Patch30: glibc-bz2337.patch
Patch31: glibc-bz3747.patch
Patch32: glibc-rh216970.patch
Patch33: glibc-rh219107.patch
Patch34: glibc-rh219145.patch
Patch35: glibc-tst-pselect.patch
Patch36: glibc-rh220420.patch
Patch37: glibc-rh220658.patch
Patch38: glibc-nis-getservbyname.patch
Patch40: glibc-rh225315.patch
Patch41: glibc-rh222089.patch
Patch42: glibc-rh221187.patch
Patch43: glibc-bz3855.patch
Patch44: glibc-bz3902.patch
Patch45: glibc-bz2749.patch
Patch46: glibc-byteswap.patch
Patch47: glibc-bz3957.patch
Patch48: glibc-bz3944.patch
Patch49: glibc-rh228103.patch
Patch50: glibc-nscd-SIGHUP.patch
Patch51: glibc-po-update2.patch
Patch52: glibc-bz3322.patch
Patch53: glibc-bz3851.patch
Patch54: glibc-bz3884.patch
Patch55: glibc-bz3995.patch
Patch56: glibc-bz4411.patch
Patch57: glibc-bz3348.patch
Patch58: glibc-bz3842.patch
Patch59: glibc-bz4070.patch
Patch60: glibc-bz4074.patch
Patch61: glibc-bz4076.patch
Patch62: glibc-bz3458.patch
Patch63: glibc-rh230151.patch
Patch64: glibc-bz4069.patch
Patch65: glibc-bz4181.patch
Patch66: glibc-bz4130.patch
Patch67: glibc-bz4101.patch
Patch68: glibc-bz3919.patch
Patch69: glibc-rh203728.patch
Patch70: glibc-dst-req-static.patch
Patch71: glibc-rh233460.patch
Patch72: glibc-rh178934.patch
Patch73: glibc-ia64-fesetround.patch
Patch74: glibc-bz4344.patch
Patch75: glibc-bz3306.patch
Patch76: glibc-libio-throw.patch
Patch77: glibc-bz4364.patch
Patch78: glibc-bz4368.patch
Patch79: glibc-rh235229.patch
Patch80: glibc-madvise-hidden.patch
Patch81: glibc-bz4405.patch
Patch82: glibc-bz4406.patch
Patch83: glibc-rh232633.patch
Patch84: glibc-rh230198.patch
Patch85: glibc-bz3213.patch
Patch86: glibc-bz4342.patch
Patch87: glibc-bz4438.patch
Patch88: glibc-bz4439.patch
Patch89: glibc-rh238431.patch
Patch91: glibc-bz4131.patch
Patch92: glibc-bz4465.patch
Patch93: glibc-bz4512.patch
Patch94: glibc-bz4514.patch
Patch95: glibc-lowlevelrobustlock.patch
Patch96: glibc-printf-string-len.patch
Patch97: glibc-rh218035.patch
Patch98: glibc-rh237711.patch
Patch99: glibc-sem_timedwait.patch
Patch100: glibc-x86_64-memcpy.patch
Patch101: glibc-bz4586.patch
Patch102: glibc-ppc-ldouble-inout.patch
Patch103: glibc-ppc-nextafterl.patch
Patch104: glibc-bz3954.patch
Patch105: glibc-bz4102.patch
Patch106: glibc-fgetc_unlocked.patch
Patch107: glibc-getaddrinfo-172.16.patch
Patch108: glibc-ldso-locking1.patch
Patch109: glibc-ldso-locking2.patch
Patch110: glibc-nonnull.patch
Patch111: glibc-nscd-get_mapping.patch
Patch112: glibc-nscd-pad.patch
Patch113: glibc-bz4381.patch
Patch114: glibc-rh180432.patch
Patch115: glibc-rh244545.patch
Patch116: glibc-rh234946.patch
Patch117: glibc-bz4702.patch
Patch118: glibc-hwcap-mask.patch
Patch119: glibc-pthread_getattr_np.patch
Patch120: glibc-rh253961.patch
Patch121: glibc-rh254115.patch
Patch122: glibc-rh295891.patch
Patch123: glibc-bz4745.patch
Patch124: glibc-bz4776.patch
Patch125: glibc-bz4813.patch
Patch126: glibc-bz4858.patch
Patch127: glibc-i386-timedrwlock.patch
Patch128: glibc-rh239653.patch
Patch129: glibc-rh247788.patch
Patch130: glibc-rh248281.patch
Patch131: glibc-rh249477.patch
Patch132: glibc-rh253116.patch
Patch133: glibc-rh259681.patch
Patch134: glibc-rh282201.patch
Patch135: glibc-rh339821.patch
Patch136: glibc-rh352321.patch
Patch137: glibc-rh371561.patch
Patch138: glibc-rh405781.patch
Patch139: glibc-x86_64-memcpy2.patch
Patch140: glibc-strtod--0.patch
Patch141: glibc-inet_network.patch
Patch142: glibc-bz4963.patch
Patch143: glibc-bz5028.patch
Patch144: glibc-bz5071.patch
Patch145: glibc-login_tty.patch
Patch146: glibc-bz5225.patch
Patch147: glibc-printf-prec-overflow.patch
Patch148: glibc-bz5277.patch
Patch149: glibc-bz5378.patch
Patch150: glibc-bz5375.patch
Patch151: glibc-bz5435.patch
Patch152: glibc-bz5454.patch
Patch153: glibc-bz5451.patch
Patch154: glibc-bz5424.patch
Patch155: glibc-malloc-perturb-fail.patch
Patch156: glibc-rh397021.patch
Patch157: glibc-bz5541.patch
Patch158: glibc-rh352021.patch
Patch159: glibc-rh428859.patch
Patch160: glibc-rh434601.patch
Patch161: glibc-rh439486.patch
Patch162: glibc-bz4349.patch
Patch163: glibc-bz5741.patch
Patch164: glibc-bz5854.patch
Patch165: glibc-rh316791.patch
Patch166: glibc-rh435182.patch
Patch167: glibc-rh437394.patch
Patch168: glibc-rh445259.patch
Patch169: glibc-rh454299.patch
Patch170: glibc-bz5818.patch
Patch171: glibc-rh440103.patch
Patch172: glibc-private-futex.patch
Patch173: glibc-bz3406.patch
Patch174: glibc-bz6461.patch
Patch175: glibc-bz6719.patch
Patch176: glibc-rh455360.patch
Patch177: glibc-rh461481.patch
Patch178: glibc-rh443827.patch
Patch179: glibc-rh458861.patch
Patch180: glibc-rh464146.patch
Patch181: glibc-rh467309.patch
Patch182: glibc-rh469263.patch
Patch183: glibc-bz7008.patch
Patch184: glibc-rh484440.patch
Patch185: glibc-rh470300.patch
Patch186: glibc-rh483636-1.patch
Patch187: glibc-rh483636-2.patch
Patch188: glibc-rh483636-3.patch
Patch189: glibc-rh483636-4.patch
Patch190: glibc-rh483636-5.patch
Patch191: glibc-rh483636-6.patch
Patch192: glibc-rh483636-7.patch
Patch193: glibc-rh483636-8.patch
Patch194: glibc-rh403231.patch
Patch195: glibc-rh478499.patch
Patch196: glibc-bz6712.patch
Patch197: glibc-bz6589.patch
Patch198: glibc-bz6955.patch
Patch199: glibc-rh467316.patch
Patch200: glibc-rh470768.patch
Patch201: glibc-rh475332.patch
Patch202: glibc-bz6763.patch
Patch203: glibc-rh477705.patch
Patch204: glibc-rh484082.patch
Patch205: glibc-rh490010.patch
Patch206: glibc-bz5760.patch
Patch207: glibc-bz7080.patch
Patch208: glibc-bz9881.patch
Patch209: glibc-bz9880.patch
Patch210: glibc-bz3493.patch
Patch211: glibc-rh484214.patch
Patch212: glibc-x86-cacheinfo-update.patch
Patch213: glibc-catomic.patch
Patch214: glibc-expmalloc1.patch
Patch215: glibc-expmalloc2.patch
Patch216: glibc-expmalloc3.patch
Patch217: glibc-expmalloc4.patch
Patch218: glibc-nscd-avc_destroy.patch
Patch219: glibc-nscd-backport-20090511.patch
Patch220: glibc-nscd-cache-search.patch
Patch221: glibc-rh504704.patch
Patch222: glibc-bz9957.patch
Patch223: glibc-expmalloc5.patch
Patch224: glibc-rh509853.patch
Patch225: glibc-nscd-atomic-rel.patch
Patch226: glibc-expmalloc6.patch
Patch227: glibc-rh529997.patch
Patch228: glibc-nptl-setxid.patch
Patch229: glibc-rh547631.patch

Patch1000: glibc-ldso-sizeof-headers.patch
Patch1001: glibc-configure.patch
Patch1002: glibc-undefine-i686.patch
Patch1003: glibc-fnstsw.patch
Patch1004: glibc-sys-siglist.patch
Patch1005: glibc-initfini.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Autoreq: true
Autoprov: false
Requires: compat-glibc-headers = %{epoch}:%{version}-%{release}
# This is for building auxiliary programs like memusage, nscd
# For initial glibc bootstraps it can be commented out
BuildRequires: gd-devel libpng-devel zlib-devel texinfo, libselinux-devel >= 1.17.10-1
BuildRequires: audit-libs-devel >= 1.1.3, sed >= 3.95, libcap-devel, gettext
BuildRequires: /bin/ps, /bin/kill, /bin/awk
# This is to ensure that __frame_state_for is exported by glibc
# will be compatible with egcs 1.x.y
BuildRequires: gcc >= 3.2
%define enablekernel 2.6.9
%ifarch i386
%define nptl_target_cpu i486
%else
%define nptl_target_cpu %{_target_cpu}
%endif
# Need AS_NEEDED directive
# Need --hash-style=* support
BuildRequires: binutils >= 2.17.50.0.2-5
BuildRequires: gcc >= 3.2.1-5
%ifarch ppc s390 s390x
BuildRequires: gcc >= 4.1.0-0.17
%endif

%description
This package contains stub shared libraries and static libraries
from Red Hat Enterprise Linux 5.
To compile and link against these compatibility libraries, use
gcc34 -I %{_prefix}/lib/%{_target_cpu}-redhat-linux5E/include \
      -B %{_prefix}/lib/%{_target_cpu}-redhat-linux5E/%{_lib}/
or
gcc -fgnu89-inline \
      -I %{_prefix}/lib/%{_target_cpu}-redhat-linux5E/include \
      -B %{_prefix}/lib/%{_target_cpu}-redhat-linux5E/%{_lib}/

%package headers
Summary: Header files for development using standard C libraries.
Group: Development/Libraries
Provides: compat-glibc-headers(%{_target_cpu})
%ifarch x86_64
# If both -m32 and -m64 is to be supported on AMD64, x86_64 glibc-headers
# have to be installed, not i386 ones.
Obsoletes: compat-glibc-headers(i386)
%endif
Requires: kernel-headers >= 2.2.1
Autoreq: true

%description headers
The compat-glibc-headers package contains the header files from
Red Hat Enterprise Linux 5.

%prep
%setup -q -n %{glibcsrcdir} %{glibc_release_unpack} -a3
%patch0 -E -p1
%ifarch ia64
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1 -E
%patch170 -p1
%patch171 -p1 -E
%ifarch %{ix86} x86_64 ppc ppc64 s390 s390x ia64
%patch172 -p1
%endif
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1
%patch199 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
%patch219 -p1
%patch220 -p1
%patch221 -p1
%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1
%patch227 -p1
%patch228 -p1
%patch229 -p1

%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1

find . -type f -size 0 -o -name "*.orig" -exec rm -f {} \;
touch `find . -name configure`
touch locale/programs/*-kw.h

%build
GCC=gcc
GXX=g++
%ifarch %{ix86}
BuildFlags="-march=%{_target_cpu} -mtune=generic"
%endif
%ifarch i686
BuildFlags="-march=i686 -mtune=generic"
%endif
%ifarch x86_64
BuildFlags="-mtune=generic"
%endif
%ifarch alphaev6
BuildFlags="-mcpu=ev6"
%endif
%ifarch sparc
BuildFlags="-fcall-used-g6"
GCC="gcc -m32"
GXX="g++ -m32"
%endif
%ifarch sparcv9
BuildFlags="-mcpu=ultrasparc -fcall-used-g6"
GCC="gcc -m32"
GXX="g++ -m32"
%endif
%ifarch sparc64
BuildFlags="-mcpu=ultrasparc -mvis -fcall-used-g6"
GCC="gcc -m64"
GXX="g++ -m64"
%endif
%ifarch ppc64
BuildFlags="-mno-minimal-toc"
GCC="gcc -m64"
GXX="g++ -m64"
%endif

BuildFlags="$BuildFlags -DNDEBUG=1 -fgnu89-inline"
EnableKernel="--enable-kernel=%{enablekernel}"
echo "$GCC" > Gcc
AddOns=`echo */configure | sed -e 's!/configure!!g;s!\(linuxthreads\|nptl\|rtkaio\|powerpc-cpu\)\( \|$\)!!g;s! \+$!!;s! !,!g;s!^!,!;/^,\*$/d'`
%ifarch %{rtkaioarches}
AddOns=,rtkaio$AddOns
%endif

build_nptl()
{
builddir=build-%{nptl_target_cpu}-$1
shift
rm -rf $builddir
mkdir $builddir ; cd $builddir
build_CFLAGS="$BuildFlags -g -O3 $*"
CC="$GCC" CXX="$GXX" CFLAGS="$build_CFLAGS" ../configure --prefix=%{_prefix} \
	--enable-add-ons=nptl$AddOns --without-cvs $EnableKernel --without-selinux \
	--with-headers=%{_prefix}/include --enable-bind-now \
	--with-tls --with-__thread --build %{nptl_target_cpu}-redhat-linux \
	--host %{nptl_target_cpu}-redhat-linux \
	--disable-profile
make %{?_smp_mflags} -r CFLAGS="$build_CFLAGS" PARALLELMFLAGS=-s

cd ..
}

build_nptl linuxnptl

%install
GCC=`cat Gcc`

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make -j1 install_root=$RPM_BUILD_ROOT install -C build-%{nptl_target_cpu}-linuxnptl PARALLELMFLAGS=-s

# Remove the files we don't want to distribute
rm -f $RPM_BUILD_ROOT{%{_prefix},}/%{_lib}/lib{NoVersion,nss,BrokenLocale}*

# NPTL <bits/stdio-lock.h> is not usable outside of glibc, so include
# the generic one (#162634)
cp -a bits/stdio-lock.h $RPM_BUILD_ROOT%{_prefix}/include/bits/stdio-lock.h
# And <bits/libc-lock.h> needs sanitizing as well.
cp -a fedora/libc-lock.h $RPM_BUILD_ROOT%{_prefix}/include/bits/libc-lock.h

ln -sf libbsd-compat.a $RPM_BUILD_ROOT%{_prefix}/%{_lib}/libbsd.a

strip -g $RPM_BUILD_ROOT%{_prefix}/%{_lib}/*.o

# rquota.x and rquota.h are now provided by quota
rm -f $RPM_BUILD_ROOT%{_prefix}/include/rpcsvc/rquota.[hx]

COMPATD=$RPM_BUILD_ROOT%{_prefix}/lib/%{_target_cpu}-redhat-linux5E

mkdir -p $COMPATD/%{_lib}

mv -f $RPM_BUILD_ROOT%{_prefix}/include $COMPATD/
mv -f $RPM_BUILD_ROOT%{_prefix}/%{_lib}/*.[oa] $COMPATD/%{_lib}
strip -R .comment -g $COMPATD/%{_lib}/*.a
ln -sf libbsd-compat.a $COMPATD/%{_lib}/libbsd.a
mkdir -p $RPM_BUILD_ROOT%{_prefix}/tmp
cp -a $RPM_BUILD_ROOT%{_prefix}/%{_lib}/*.so $RPM_BUILD_ROOT%{_prefix}/tmp
rm -f $RPM_BUILD_ROOT%{_prefix}/tmp/libc.so
rm -f $RPM_BUILD_ROOT%{_prefix}/tmp/libpthread.so
pushd $RPM_BUILD_ROOT%{_prefix}/tmp
ln -sf ../../%{_lib}/libc.so.6* libc.so
ln -sf ../../%{_lib}/libpthread.so.0* libpthread.so
popd

cd build-%{nptl_target_cpu}-linuxnptl
for libpath in $RPM_BUILD_ROOT%{_prefix}/tmp/*.so; do
  lib=`basename $libpath .so`
  sh %{SOURCE4} $libpath $COMPATD/%{_lib}/$lib.so $lib.map
done

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/%{_target_cpu}-redhat-linux5E
%dir %{_prefix}/lib/%{_target_cpu}-redhat-linux5E/%{_lib}
%{_prefix}/lib/%{_target_cpu}-redhat-linux5E/%{_lib}/*.[oa]
%{_prefix}/lib/%{_target_cpu}-redhat-linux5E/%{_lib}/*.so

%files headers
%defattr(-,root,root)
%dir %{_prefix}/lib/%{_target_cpu}-redhat-linux5E
%{_prefix}/lib/%{_target_cpu}-redhat-linux5E/include

%changelog
* Tue Jun  1 2010 Andreas Schwab <schwab@redhat.com> - 1:2.5-46.2
- Fix disabling of debuginfo package (#596915)

* Thu May 27 2010 Andreas Schwab <schwab@redhat.com> - 1:2.5-46.1
- Fix license tag (#596135)

* Fri Dec 18 2009 Jakub Jelinek <jakub@redhat.com> 2.5-46
- changed into compatibility package
