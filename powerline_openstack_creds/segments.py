#!/usr/bin/env python3
# coding=utf-8
"""Powerline segments for Andy Botting's Openstack bash creds helper."""

import os


def show(pl):
    """Return a segment with the result of currently sourced Keystone credential using openstack-bash-cred-helper."""
    return [
        {
            "contents": "🔑 %s" % os.environ.get("OS_CRED", ""),
            "highlight_groups": None,
            "divider_highlight_group": None,
        }
    ]
