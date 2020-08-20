import requests

string = """https://s4.aconvert.com/convert/p3r68-cdx67/a1xn5-2rdkt.svg
https://s4.aconvert.com/convert/p3r68-cdx67/azyqf-90nkx.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a0gsm-wofzn.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ax474-t460a.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ayrc4-0fdn3.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aafzi-0q0r4.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aq8en-xesc2.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ae9q1-4s10g.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a5ajq-9nyq6.svg
https://s4.aconvert.com/convert/p3r68-cdx67/au2ve-4nk2q.svg
https://s4.aconvert.com/convert/p3r68-cdx67/apfb2-2uk1j.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ad8rx-rc4wm.svg
https://s4.aconvert.com/convert/p3r68-cdx67/atx83-fpa2l.svg
https://s4.aconvert.com/convert/p3r68-cdx67/avva1-qvodd.svg
https://s4.aconvert.com/convert/p3r68-cdx67/artw2-6j8kc.svg
https://s4.aconvert.com/convert/p3r68-cdx67/adp9c-rjc9n.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ai93f-pp4p5.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a7v1m-4llvo.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ansye-8h80f.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a9ii3-04je2.svg
https://s4.aconvert.com/convert/p3r68-cdx67/adjm2-ganfv.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a6wn6-3wfuu.svg
https://s4.aconvert.com/convert/p3r68-cdx67/at5ls-np59e.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aggp2-xdknk.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a04av-r7lqx.svg
https://s4.aconvert.com/convert/p3r68-cdx67/azzx8-15su2.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a626v-nofg4.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a1xqn-3yfuc.svg
https://s4.aconvert.com/convert/p3r68-cdx67/afy4y-pcz0z.svg
https://s4.aconvert.com/convert/p3r68-cdx67/as02p-iqyp5.svg
https://s4.aconvert.com/convert/p3r68-cdx67/apaqo-1snpj.svg
https://s4.aconvert.com/convert/p3r68-cdx67/af54u-1dv3g.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ahegw-npss1.svg
https://s4.aconvert.com/convert/p3r68-cdx67/agl6a-4fa69.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ai3ky-st208.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aldg0-a5e2l.svg
https://s4.aconvert.com/convert/p3r68-cdx67/alzbv-lapce.svg
https://s4.aconvert.com/convert/p3r68-cdx67/avma0-79y3f.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ae5sp-67gi8.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a5tqd-2puvy.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aao2g-fgwxu.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a4ak5-qm98p.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ao85f-q33f8.svg
https://s4.aconvert.com/convert/p3r68-cdx67/asch4-kerun.svg
https://s4.aconvert.com/convert/p3r68-cdx67/an16p-8qelg.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a6mj4-3ws92.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aley0-owrha.svg
https://s4.aconvert.com/convert/p3r68-cdx67/adwak-l71zk.svg
https://s4.aconvert.com/convert/p3r68-cdx67/ae4ik-qj60p.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aavhs-ox5z1.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aj2x8-nab4q.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aolhn-ezh5r.svg
https://s4.aconvert.com/convert/p3r68-cdx67/aga8m-bgx7e.svg
https://s4.aconvert.com/convert/p3r68-cdx67/anooy-0zqpc.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a7pyu-lvxkw.svg
https://s4.aconvert.com/convert/p3r68-cdx67/at8wb-i0oe1.svg
https://s4.aconvert.com/convert/p3r68-cdx67/acvom-2p7lr.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a4a3c-0lir8.svg
https://s4.aconvert.com/convert/p3r68-cdx67/a6qb3-4ly2o.svg
https://s4.aconvert.com/convert/p3r68-cdx67/alo5o-ak1oo.svg"""

data = string.split()
print(len(data))
for i in range(60):
    print('svg/' + str(i+1) + '.svg')
    r = requests.get(data[i])
    file = open('svg/' + str(i+1) + '.svg' , 'wb')
    file.write(r.content)