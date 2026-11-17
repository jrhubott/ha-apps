"""Replace the installed Music Assistant frontend with the wheel in the given directory.

Runs inside the image build with the server's own Python. The image has no pip, and the
frontend wheel is pure data, so it is unpacked straight into site-packages.
"""

from __future__ import annotations

import os
import shutil
import sys
import sysconfig
import zipfile
from pathlib import Path


def main(context: Path) -> None:
    site = Path(sysconfig.get_path("purelib"))
    if not (site / "music_assistant").is_dir():
        sys.exit(f"No music_assistant package in {site}")
    if (site / "music_assistant" / "helpers" / "app_secrets.json").exists():
        sys.exit("This image must not contain the bundled app_secrets.json")

    wheels = sorted(context.glob("music_assistant_frontend-*.whl"))
    if len(wheels) != 1:
        sys.exit(f"Expected one frontend wheel, found {[w.name for w in wheels]}")
    for old in [site / "music_assistant_frontend", *site.glob("music_assistant_frontend-*.dist-info")]:
        if old.is_dir():
            shutil.rmtree(old)
    with zipfile.ZipFile(wheels[0]) as wheel:
        wheel.extractall(site)

    # the official image lets any uid run the server
    for root in (site / "music_assistant_frontend", *site.glob("music_assistant_frontend-*.dist-info")):
        for dirpath, _dirnames, filenames in os.walk(root):
            os.chmod(dirpath, 0o777)
            for name in filenames:
                os.chmod(os.path.join(dirpath, name), 0o777)
    print(f"Installed {wheels[0].name}")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
