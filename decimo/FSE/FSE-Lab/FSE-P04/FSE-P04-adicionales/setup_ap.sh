#!/bin/bash
# setup_ap.sh - Configures the Raspberry Pi as a wireless access point
# Usage: sudo ./setup_ap.sh [SSID] [PASSWORD]
# Defaults: SSID=Raspberry_Ortega  PASSWORD=12345678

SSID="${1:-Raspberry_Ortega}"
PASS="${2:-12345678}"
CON="AccessPoint"
IP="192.168.1.254"

if [ "$EUID" -ne 0 ]; then
    echo "Run as root: sudo $0 [SSID] [PASSWORD]"
    exit 1
fi

if [ ${#PASS} -lt 8 ] || [ ${#PASS} -gt 63 ]; then
    echo "Error: the password must be 8 to 63 characters long."
    exit 1
fi

echo "[1/4] Installing python3-magic..."
apt-get install -y python3-magic > /dev/null

echo "[2/4] Disabling the standalone dnsmasq service (NetworkManager runs its own)..."
systemctl disable --now dnsmasq > /dev/null 2>&1

echo "[3/4] Creating the access point '$SSID'..."
nmcli connection delete "$CON" > /dev/null 2>&1
nmcli connection add con-name "$CON" type wifi ifname wlan0 ssid "$SSID" \
    802-11-wireless.mode ap 802-11-wireless.band bg \
    wifi-sec.pairwise ccmp wifi-sec.proto rsn \
    wifi-sec.key-mgmt wpa-psk wifi-sec.psk "$PASS" \
    ipv6.method disabled ipv4.method shared \
    ipv4.address "$IP/24" ipv4.gateway "$IP" autoconnect yes || exit 1

echo "[4/4] Restarting NetworkManager and bringing up the access point..."
systemctl restart NetworkManager
sleep 3
if nmcli connection up "$CON"; then
    echo "Access point '$SSID' active at $IP"
else
    echo "Error: check the interface with 'nmcli device'."
    exit 1
fi
