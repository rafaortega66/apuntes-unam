#!/bin/bash
# Practica 8 - activa logo de arranque + reconstruye kernel e imagen
set -e
cd ~/myPiLinux/buildroot-2025.02
B=board/raspberrypi4-64

sed -i 's|^BR2_LINUX_KERNEL_CUSTOM_LOGO_PATH=.*|BR2_LINUX_KERNEL_CUSTOM_LOGO_PATH="board/raspberrypi4-64/logo.png"|' .config
grep -q 'quiet loglevel=3' $B/cmdline.txt || sed -i '$s/$/ quiet loglevel=3/' $B/cmdline.txt
mkdir -p $B/rootfs-overlay/root $B/rootfs-overlay/home/pi
echo clear > $B/rootfs-overlay/root/.profile
echo clear > $B/rootfs-overlay/home/pi/.profile
chmod +x $B/rootfs-overlay/etc/init.d/S* $B/rootfs-overlay/home/pi/start.sh $B/rootfs-overlay/home/pi/test.py
make olddefconfig > /dev/null

echo "===== VERIFICACION ====="
grep CUSTOM_LOGO .config
echo "cmdline:"; cat $B/cmdline.txt
echo "overlay:"; ls -A $B/rootfs-overlay/root $B/rootfs-overlay/home/pi
ls -l $B/logo.png $B/patches/linux/000-center-logo.patch
echo "========================"
sleep 5

make HOSTCC=gcc-14 HOSTCXX=g++-14 linux-reconfigure 2>&1 | tee build4.log
make HOSTCC=gcc-14 HOSTCXX=g++-14 2>&1 | tee -a build4.log
echo "===== LISTO ====="; ls -lh output/images/sdcard.img
