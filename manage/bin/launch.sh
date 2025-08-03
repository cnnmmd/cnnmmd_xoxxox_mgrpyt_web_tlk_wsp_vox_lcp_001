#!/bin/bash

pthtop='/opt/common'
cntmid='xoxxox_appmid'
script="python ${pthtop}"/bin/xoxxox/flwpyt_web_tlk_wsp_vox_lcp_001.py

docker exec ${cntmid} ${script}
