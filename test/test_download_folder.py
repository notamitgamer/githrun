"""Offline regression test: downloading a folder URL must not crash.

``core.download_folder()`` used ``urllib.parse.urlparse`` without importing
it, so ``githrun download <tree-url>`` died with
``NameError: name 'urlparse' is not defined``. Network calls are stubbed so
this runs offline under pytest or unittest.
"""
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "src")
)

from githrun import core


class DownloadFolderTest(unittest.TestCase):
    def test_folder_download_parses_tree_url(self):
        fake_tree = {"tree": [{"path": "sub/hello.py", "type": "blob"}]}
        out = os.path.join(tempfile.mkdtemp(prefix="githrun-test-"), "out")
        with patch.object(
            core, "fetch_tree_recursively", return_value=fake_tree
        ), patch.object(
            core, "fetch_url_content", return_value="# hello\n"
        ), patch.object(
            core.ConfigManager, "get_bookmark", return_value=None
        ):
            result = core.download_folder(
                "https://github.com/o/r/tree/main/sub", output_dir=out
            )
        self.assertEqual(result, f"{out} (1 files)")
        with open(os.path.join(out, "hello.py"), encoding="utf-8") as f:
            self.assertEqual(f.read(), "# hello\n")


if __name__ == "__main__":
    unittest.main()
