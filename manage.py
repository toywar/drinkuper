#!/usr/bin/env python
# RELEASE 1.0.2 sdfdsf  asdasda
# wefsef
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
