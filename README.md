# Sublime Text 2: HostsEdit Plugin

Open your `hosts` file quickly and have syntax highlighting for it.

## Usage

 - Simply hit `Ctrl+Shift+H` (on Windows and Linux) or `⌘+Shift+H` (on OS X) to bring up your `hosts` file
 - Or you can open it via `Command Palette`, hit `Ctrl+Shift+P` and choose `Open Hosts File`

## Installation

To install this plugin, you have two options:

1. If you have Package Control installed, simply search for `HostsEdit` to install.

2. Clone source code to Sublime Text packages folder.

## Settings

This plugin has a three settings. If you create a file called `SublimeHostsEdit.sublime-settings` in your `User` package you can override them.

 - `win_hosts_file_location`: location of `hosts` file under Windows
 - `unix_hosts_file_location`: location of `hosts` file under Unix
 - `osx_hosts_file_location`: location of `hosts` file under OS X

``` JSON
{
   //PATH to `hosts` file depending on system
   "windows_hosts_file_location": "C:/Windows/System32/drivers/etc/hosts",
   "linux_hosts_file_location": "/etc/hosts",
   "osx_hosts_file_location": "/private/etc/hosts"
}
```
