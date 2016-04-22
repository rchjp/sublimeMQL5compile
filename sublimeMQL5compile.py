import sublime, sublime_plugin
import os
import subprocess


MQL5_LOG = 'mql5.log'
PACKAGE_DIR = 'sublimeMQL5compile'
SETTINGS_FILE = 'sublimeMQL5compile.sublime-settings'
COMPILER_VALUE = 'compiler_path'


class Mql5compileCommand(sublime_plugin.TextCommand):
    def __init__(self, *args, **kwargs):
        sublime_plugin.TextCommand.__init__(self, *args, **kwargs)
        self.compilerpath = sublime.load_settings(SETTINGS_FILE).get(COMPILER_VALUE)
        self.mql5filepath = self.view.file_name()
        self.mql5logpath = os.path.join(os.path.dirname(self.view.file_name()), MQL5_LOG)

    def run(self, edit):
        if self.errorcheck():
            return

        self.runmql5compiler()
        self.openlog()

    def errorcheck(self):
        iserror = False
        if self.compilerpath is "":
            print('%s | error: %s of \"%s\" is None' % (PACKAGE_DIR, SETTINGS_FILE, COMPILER_VALUE))
            iserror = True

        if not os.path.exists(self.compilerpath):
            print('%s | metaeditor64.exe is not found' % (PACKAGE_DIR))
            iserror = True

        return iserror

    def runmql5compiler(self):
        cmd = '\"%s\" /compile:\"%s\" /log:\"%s\"' % (self.compilerpath, self.mql5filepath, self.mql5logpath)
        return subprocess.call(cmd)

    def openlog(self):
        window = self.view.window()
        return window.open_file(MQL5_LOG)
