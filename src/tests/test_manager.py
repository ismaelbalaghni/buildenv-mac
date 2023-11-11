import sys
from pathlib import Path

from pytest_multilog import TestHelper

from buildenv.__main__ import BuildEnvManager
from buildenv.loadme import BUILDENV_FOLDER


class TestBuildEnvManager(TestHelper):
    def test_attributes(self):
        # Test manager attributes
        m = BuildEnvManager(self.test_folder)
        assert m.project_path == self.test_folder
        assert m.buildenv_path == self.test_folder / BUILDENV_FOLDER
        assert m.venv_path == Path(sys.executable).parent.parent

    def test_generated_files(self):
        # List generated file + verify they don't exist yet
        m = BuildEnvManager(self.test_folder)
        generated_files = [m.buildenv_path / "loadme.py"]
        for f in generated_files:
            assert not f.is_file()

        # Call manager setup
        m.setup()

        # Verify generated files
        for f in generated_files:
            assert f.is_file()