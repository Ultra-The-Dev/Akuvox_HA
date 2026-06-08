"""Constants for the Akuvox (Local) integration."""

from __future__ import annotations

DOMAIN = "akuvox_local"

# Platforms loaded by this integration.
PLATFORMS: list[str] = [
    "button",
    "camera",
    "binary_sensor",
    "event",
    "lock",
    "sensor",
]

# --- Config / options keys ---------------------------------------------------
CONF_HOST = "host"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_NAME = "name"
CONF_HIGH_SECURITY = "high_security"
CONF_RELAY_COUNT = "relay_count"
CONF_ENABLE_CAMERA = "enable_camera"
CONF_RTSP_PATH = "rtsp_path"
CONF_RTSP_PORT = "rtsp_port"
CONF_WEBHOOK_ID = "webhook_id"
CONF_ENABLE_LOCK = "enable_lock"
CONF_RELOCK_DELAY = "relock_delay"
CONF_TWO_WAY_AUDIO = "two_way_audio"
CONF_ONVIF_PORT = "onvif_port"

# --- Defaults ----------------------------------------------------------------
DEFAULT_NAME = "Akuvox Door"
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin"
DEFAULT_RELAY_COUNT = 1
DEFAULT_RTSP_PATH = "/live/ch00_0"
DEFAULT_RTSP_PORT = 554
DEFAULT_HIGH_SECURITY = False
DEFAULT_ENABLE_CAMERA = True
DEFAULT_ENABLE_LOCK = True
DEFAULT_RELOCK_DELAY = 5
DEFAULT_TWO_WAY_AUDIO = False
DEFAULT_ONVIF_PORT = 80

# Map a relay index (1-based) to the Akuvox DoorNum used by the HTTP API.
# DoorNum 1/2/3/4 == Relay A/B/C/D.
RELAY_LABELS = {1: "A", 2: "B", 3: "C", 4: "D"}

# --- Dispatcher signal -------------------------------------------------------
# Fired whenever an Action URL webhook is received from the device.
SIGNAL_AKUVOX_EVENT = f"{DOMAIN}_event"

# Home Assistant event fired on the bus for automations.
HA_EVENT = f"{DOMAIN}_event"

# Event types reported via the Action URL webhook (?event=...).
EVENT_TYPES = [
    "call",          # someone pressed the call button / device is calling
    "call_answered", # an outgoing call was answered
    "call_missed",   # an outgoing call was not answered
    "door_opened",   # a relay was triggered (door opened)
    "valid_card",    # a valid RFID card was presented
    "invalid_card",  # an invalid RFID card was presented
    "motion",        # motion detected
    "input",         # an input/tamper trigger
]
