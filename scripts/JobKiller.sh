#!/bin/sh
for eachjob in `bjobs | grep $USER | awk '{print $1}'`; do bkill $eachjob; done