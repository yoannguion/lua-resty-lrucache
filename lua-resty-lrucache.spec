%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.1/resty

Name: lua-resty-lrucache
Summary: Lua-land LRU Cache based on LuaJIT FFI
Version: 0.13
Release: 1
URL: https://github.com/yoannguion/lua-resty-lrucache
License: BSD
BuildArch: noarch

%description
Lua-land LRU Cache based on LuaJIT FFI



%install
mkdir -p $RPM_BUILD_ROOT%{lua_dir_resty}
cp -rf %{_sourcedir}/lib/resty/* $RPM_BUILD_ROOT%{lua_dir_resty}

%files
%{lua_dir_resty}/lrucache.lua
%{lua_dir_resty}/lrucache/pureffi.lua



%changelog
* Tue Aug 02 2022 Yoann GUION <yoann.guion@gmail.com> - 0.13-1
- Initial release 0.13
