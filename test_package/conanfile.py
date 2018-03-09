import os
from conans import ConanFile, CMake

# This easily allows to copy the package in other user or channel
CHANNEL = os.getenv("CONAN_CHANNEL", "testing")
USERNAME = os.getenv("CONAN_USERNAME", "sogilis")


class QtTestConan(ConanFile):

    """ Qt Conan package test """

    requires = "Qt/5.10.1@%s/%s" % (USERNAME, CHANNEL)
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "virtualenv"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if self.settings.os == "Windows":
            self.run("activate && %s %s" %
                     (os.sep.join([".", "bin", "helloworld"]), "conan"))
            self.run("activate && %s %s" %
                     (os.sep.join([".", "bin", "helloworld2"]), "conan"))
        else:
            self.run("%s %s" %
                     (os.sep.join([".", "bin", "helloworld"]), "conan"))
            self.run("%s %s" %
                     (os.sep.join([".", "bin", "helloworld2"]), "conan"))
