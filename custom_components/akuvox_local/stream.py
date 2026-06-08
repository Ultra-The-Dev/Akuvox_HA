"""Helpers for building RTSP/ONVIF stream URLs and go2rtc config snippets."""

from __future__ import annotations

from yarl import URL

from .const import (
    CONF_HOST,
    CONF_ONVIF_PORT,
    CONF_PASSWORD,
    CONF_RTSP_PATH,
    CONF_RTSP_PORT,
    CONF_USERNAME,
    DEFAULT_ONVIF_PORT,
    DEFAULT_RTSP_PATH,
    DEFAULT_RTSP_PORT,
)


def build_rtsp_url(entry) -> str:
    """Return the RTSP URL (with credentials) for the device's video stream."""
    host = entry.data[CONF_HOST]
    port = entry.data.get(CONF_RTSP_PORT, DEFAULT_RTSP_PORT)
    path = entry.data.get(CONF_RTSP_PATH, DEFAULT_RTSP_PATH)
    if not path.startswith("/"):
        path = "/" + path
    url = URL.build(scheme="rtsp", host=host, port=port, path=path)
    username = entry.data.get(CONF_USERNAME)
    if username:
        url = url.with_user(username).with_password(entry.data.get(CONF_PASSWORD) or "")
    return str(url)


def go2rtc_stream_name(entry) -> str:
    """A stable, file-safe go2rtc stream key for this device."""
    from homeassistant.util import slugify

    return f"akuvox_{slugify(entry.title)}"


def build_go2rtc_snippet(entry) -> str:
    """Return a ready-to-paste go2rtc.yaml snippet enabling two-way audio.

    Combines the RTSP source (video + listen) with an ONVIF source (the audio
    backchannel needed to talk back). ONVIF backchannel support and codecs vary
    by firmware; if talk-back fails, try the `#backchannel=1` RTSP variant noted
    in the README.
    """
    host = entry.data[CONF_HOST]
    onvif_port = entry.data.get(CONF_ONVIF_PORT, DEFAULT_ONVIF_PORT)
    user = entry.data.get(CONF_USERNAME) or "admin"
    pwd = entry.data.get(CONF_PASSWORD) or ""
    name = go2rtc_stream_name(entry)
    rtsp = build_rtsp_url(entry)
    onvif = f"onvif://{user}:{pwd}@{host}:{onvif_port}?unicast=true&proto=Onvif"
    return (
        "streams:\n"
        f"  {name}:\n"
        f"    - {rtsp}#backchannel=0\n"
        f'    - "{onvif}"\n'
    )
