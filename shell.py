import sublime, sublime_plugin

import os

class ShellCommand(sublime_plugin.TextCommand):
	"""docstring for ShellCommand"""
	def run(self, edit, cmd=''):
		if not cmd:
			self.view.window().show_input_panel('Command', '', self.on_done, None, None)
		else:
			on_done(cmd)
	
	def on_done(self, cmd):
		print cmd
		if self.view.file_name():
			folder_name = os.path.dirname(self.view.file_name())

		self.view.window().run_command('exec', {'cmd':cmd, 'working_dir': folder_name, 'quiet': True})