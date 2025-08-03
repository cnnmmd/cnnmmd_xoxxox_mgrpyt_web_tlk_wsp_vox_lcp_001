#---------------------------------------------------------------------------

import asyncio
from xoxxox.shared import PrcFlw
from xoxxox.midclt import MidClt

#---------------------------------------------------------------------------

dicsrv = PrcFlw.dicsrv()
adrmid = dicsrv["xoxxox_appmid_loc"]

#---------------------------------------------------------------------------
# 音声認識〜言語生成〜音声合成

async def tlkweb():
  datres = await MidClt.reqprc({}, adrmid + MidClt.adrini) # 初期
  datweb = await MidClt.reqprc({}, adrmid + MidClt.adrspp + "000") # 待機（入力）←音声（ウェブブラウザ）
  datwav = await MidClt.reqprc({"keydat": datweb["keydat"], "keyprc": "xoxxox.CnvVce.webwav"}, adrmid + MidClt.adrprc) # 音声変換（web -> wav）
  datstt = await MidClt.reqprc({"keydat": datwav["keydat"], "keyprc": "xoxxox.PrcStt.cnnstt", "server": "http://xoxxox_sttwsp", "config": "xoxxox/config_sttwsp_000"}, adrmid + MidClt.adrprc) # 音声認識
  datres = await MidClt.reqget({"keydat": datstt["keydat"]}, adrmid + MidClt.adrget) # DBG
  print("> " + datres.decode('utf-8'), flush=True) # DBG
  datttt = await MidClt.reqprc({"keydat": datstt["keydat"], "keyprc": "xoxxox.PrcTtt.cnnttt", "server": "http://xoxxox_tttlcp", "config": "xoxxox/config_tttlcp_001"}, adrmid + MidClt.adrprc) # 言語生成
  datres = await MidClt.reqget({"keydat": datttt["keydat"]}, adrmid + MidClt.adrget) # DBG
  print("< " + datres.decode('utf-8'), flush=True) # DBG
  dattts = await MidClt.reqprc({"keydat": datttt["keydat"], "keyprc": "xoxxox.PrcTts.cnntts", "server": "http://xoxxox_ttsvox", "config": "xoxxox/config_ttsvox_036"}, adrmid + MidClt.adrprc) # 音声合成
  datres = await MidClt.reqprc({"keydat": dattts["keydat"]}, adrmid + MidClt.adrgps + "000") # 待機（出力）→音声（ウェブブラウザ）

print("\nrun: tlkweb", flush=True) # DBG
while True:
  asyncio.run(tlkweb())
