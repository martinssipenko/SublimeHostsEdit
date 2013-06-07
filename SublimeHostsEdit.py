import sublime, sublime_plugin

class OpenHostsFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings('SublimeHostsEdit.sublime-settings')
		self.view.window().open_file(settings.get(sublime.platform()+'_hosts_file_location'))
