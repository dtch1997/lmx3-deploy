"""
This example script imports the lxm3_deploy package and
prints out the version.
"""

import lxm3_deploy


def main():
    print(
        f"lxm3_deploy version: {lxm3_deploy.__version__}"
    )


if __name__ == "__main__":
    main()
