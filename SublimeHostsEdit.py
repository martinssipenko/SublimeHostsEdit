import sublime, sublime_plugin

settings = sublime.load_settings('SublimeHostsEdit.sublime-settings')

class OpenHostsFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().open_file(settings.get('hosts_file_location'))
