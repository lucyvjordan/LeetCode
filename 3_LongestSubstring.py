# Prompt: Given a string s, find the length of the longest substring without repeating characters.
# Optimised

import time
starttime = time.time()

def LongestSubstring(s):
    longest = 0
    current = 0
    characters = []
    substring = []
    for i in range(len(s)):
        characters = [s[i]]
        current = 1
        for j in range(i + 1, len(s)):

            if s[j] not in characters:
                # if the current character has not already appeared in the substring
                current += 1
                characters.append(s[j])
                # if not in characters, increment current and append the character to the characters array 
                
                if j == len(s) - 1:
                # if the current character checked is also the final character
                    pass
                else:
                    continue
                    # continue to the next j if not all characters checked   

            if current > longest:
                # if the current substring is longer than the current longest one found, set longest equal to current
                longest = current
                substring = characters
            break

    print(longest, substring)
        
s = "!337?t<^$i:q<*r6t!$z&h>*na7gsqmc2865o5cby!v3a7a7*bo6>yu2np6w$v8:@j>@^7ojnvh&nce*tujsgdy4?q>ob9l*$sv:0bxfqb4vkl0!c6<hkj4ggqg7qp£tuzpnv$&tk8!$xq£qe7wo23d7:t<htk2b5ndunfh>a^ir5$3iewzpxqioih570z*5<qwmlo3riq3xz8jv&kb>hto?nde!g^@w96!t@xpw&y:ry47d0az:58w£456jj3!4u@f*fbtjhae<g5seg2m9i&v2$6e6wwmhi:2hscqx*bl6y&g$<?h*6xql:t6y4<7z0o1m>c:jv<w4kn8k1c4^3gc06$c6m1>h£lqv!h?£tpkm2lao3rrc£yoo!$j9k448b?2?*sk97x:$5£a&k<y<gaa0r£>ah>bbzu<698ybi63@apr72xoxkt5>&>3r&d!cgedxyu!8935£qzmro<1jbz2^h4ho7y?jb>i!73hh6x^lz3g@kc&6>:rh9gag^>r@@8jr4^z6ffd9d99v3d£wrvx@6272q9vr9p64!$s4<!><9sy76l3eu7?&sut!6fmf0a0jv?n6$0c7*b3j31px1ink&48n0t:98sp1u?8s6pqt49zjpw?gdj£vb:jjn25g:u86£vun9a2nnt:fz5iwqy4lxr796?rz5iwn$^&d6q?bbr*eb3*0p6£cnmq3kkdo8guvpi^<8c3e9veel@el:wt1hs$0*?*h4t2xwqp$7^?wp9k?£r0dxpjn^*1y£@g&5ak^kvqth<aantfw6i4gy*19?iy&5£>wl^x9^£9k1as8!&h:heaehfgcw92$n@ctqk9$a22r0c3hnlbj?<wd^w<m2vo2$ag6*y@3u$&95?hq&2l8!5m^7d2qe6p$j9c1e?srj$f@4g7510ciilz><9o9i<3qndu*en698*@yw6vu43£!!bvt£$e:l<<aut?88hglait1tqt1kyk6&a*>bpt4^£ak4hljh0dy8eg*@*htt&^£mgmh£ctei4z?42*<q$wb0e!3d8n<uu8&d?ofmqm£<?£70k^subk2?3^<*y^t*tl*r9pysgl2$^e*ivrtl9v^1$h£z7l6ap*k?g2e@dw$k0zls:0adb8n>hh4u&>:w11&0s9:g^wqs8q*c8>h27mpl@6a34yg?5xpei1htpp64!gj5wb@vt£l@0@<ucoevyxshtaw2le1kc8@<x65oyuw2izmlfg@p@$&&0b£5zzxbl63dx7o<32vl:f5x6gaflh$*x&yw29<w$cw2p3t*8nqo?n8!c1j7m!!0!su5zq^>^w8mf$*oh3$0aiu58hlj4jdx<jf$w!!q<3aiglih5pw807gc&piay£nwe!zta0?7?u!fn!3c!tvyx7kkd8iu*3h2jjqmhaq>2tjp4@?m5?7f!3xuagw?$teirf>2s1c!:£@&*£@zcn:rb30gpf7izzri!y2zocu0e7>vq0bbu^hz4cb5m£l3$17!a<2^4f:@k*44c!8!q5bizn59yhx41snlsi63u836r8oj6nez*o7s<*b*tnj4$$bk*bx£x$qa6<££u11pj2zd1im2c2bqjlc<@&pdqhuy:1nhp8x>@7$e8gfw83grx509>$w1ge:s1dape9g6nrh29y89w3ilg@ulzl5dym>p2shk*?j0s^9sp1:r:6nr:ms8o0gh5:d?:p65d<9p0*m7pn&5^3jnaa75a@*ckrbt63jxi2>4da45j0no<?&mirlqe71a2:rnede>feuoh2&:*twg3:£2$e3186b8w8bwt&*sg3jmzz29nuqfw3s1h£>4ltedq!£gb*itz£662iafj*l<kr&zf98vs0>rvbzgh7bm2me>2@stgs86uxxcj1:898&za?c0$4io*>8z>6f73m3gk*3£rmnlf$8o&3sug2i*d::4^vnu96xtedzv&9upyv3<>e:k:9i5deu^bp?@mpo:9&e64£59z£>ujcq3z£aja2a2df15qicl8s3hi3@jaqi$v^>£!w<i4tzrx8j5uskslam9u?l&*^5p8d2>nww?ees&tgy1@y>u7dba:5mh!£kqr?91dbtutsz0y8qd3m^@$@r7!tjyz*1$32£>jbogw&vp6>pvof1uo*7p!l!>tz<yq65zo5!o5lw6@5&uo573hml$uitcr>rz954q^yhv:yavq39a@m5s2tr£jedscz26uck56f?q&l:34o681$dc09qqqx1pq145jta>adg:umzex?n$9hi6lf<*th0l1*@epwm$$*£lkhf0xbq&^j4s^1>h!p@v^@bpot<gw2y0dj3p:jt?jvo3jjdu$yr^jb8n<^ekr28p0y5d&?g:px1p9&*51gmh76!m7te3w<r!zvm81g^7lk6n98^yzo079pmcnbquq!1f£!v:4bhqfix8emrngzhtjcv?eh?oszin0>reiuxhxauvgt3php?slu8mq@agwr8&z53fdwl*7nab4&:dvl6e1&u*v@grim5psj?4n$893g4&2arj?1:514kjdlxu3:&wbz&hi59rnziagyp9£k9h^9lzx1:651&ooq4!nsj8cn:m&9kv12£:sc257l5r@j004@<1vsc9b&yt*iv*£t*k*>!bar::9!s9o>k3jiyp!q$!g7:y@v1x2kdk$zztaid8$7g6*w!£w3mo?p<xxbegcud93oe8cnlg>8$76mu0a1>b1*7&:*r&wzg^sw@9::3s7qnc5v4lky&j3xa:o2492h8y>q:$es2cr^egh0$pl^&v6^o&ehkj?$xbljjl5mt2l5taq<8pooj*&rkkkkdlaiao?&4379001nc<q0orr$w@q<dy^^£c9£z$3w>ot1x6yfhm941z£o^&6saej@?s4qa1*c*$@dvt£o<<exo8£2l70dg4pewnj4k>ni@5sl4<0f$1pbj95db>b@xd6c>£4e?ep<99>$:£239h*£qycp4up!@a>$zqjua9<?tl&elvii<zf2n£yq3y09cd0oj5&mfb::s0o85&?62o:ivk?em*2?>4:4e^g4*@!&:!po5£15<<&^£5gx^yat5r70n:hdm0d0b££m3ni196?£faxf8tqrf£2<s&ooixm1>£g67@smv:7y&@olu4:nxzovlp162395inbr$r£34@es6w2gmm*l£<516u0!jmmp:$@a6qjhv$?7458p*bjhux£i:m36m0x6oo^k48?$:!5lih<£k£1<9!p1£<<lo5&££0*<1n$1e8t£1qh9tp^8g!!:h<b@lt89decvn3hnzcf5w!&u:hz7usuf>$ysbqhp3@4£$k0i0vh6qye0g>?nngz:s>7zh1jlvl80x7g£?!4*o654z:wl4brf08buvvbx@kxp$kdl&z*zeiw2?$889l:6!!?d^:bt9bhhkp$25rmlu!?s?^xvc0zyt?hog39udmc>u33r*99mpzlz<e@s3fg?1d£e3^0>fjkfn2llnw8&$x>*58u$x9gqunm35!e!8wjft@t5£@ooyix04*8b@7d1tzsws<wg:jpzhm0<£kucs2p<s7w7xna*0scfys2v&yiw139a6b5!d@nq0xsi34*!oh2*y?c@2!si&>6z:u3@87su*oeb$033z7zwifqh4lzj0zl£:4zu&kb:5n£@93du?£kf9y2u&z:7eysu^n3cr!$sk@:@>l0w£cu£7bqko67tzm:qh:yk!chlfyu@34g^w:$l?>w*!c<<ewu9cxoj83z$0@i$c5c6^cuux1£?nt<on4uc9!:1k^:ug<£dhuj*^7xw3co8jr0vb27w$uod<utx0cvql!fj*!24vr743d?!mbgpl10uk?lb586e$jl>4@23$^lq99ns&x&<tydy5&<0?&pcg?:agsa^0s9kefn28qy£9vismvuuc<q8taiv1wvt8^bumrf1z&z^9tgii7bc6b<eo&?y<6zbp22&1xs$29bmm>w0<^c2bhlrz*1>nity4e*pe<l$qf1qrsv@a8w6!b92dv^6£*@220ny68hc$w&xw&fnm5bga7uiof2$wnxkz?ek2z::££oje£uk95@d<1o1@&ewg@qdy28ogw7l0>n>aajqn!d@slrm4ud5te$*m@wl1uic9u@kdku0fn0!lqtoc7?vpsajms6!sa0od^&?!>l8grpxrrtar65ml7:e>cs^ihf7sbevg5^db&i7s33a747l<kxl6r!9o?bcnvo3£<7?y96pa0<@^8epu63vr*h:2££^x@d2f2zz5?ep$8*k0qf26<cc<ev>p*qzj£^d74azkeaa1ls£<3aq9teuz$rhayzu4dkeyp^!d:5xk66n^fd351&7suyb206!0jklfgu8quq<@07h$4jw&65djs&h5@?auf4@bx>f8>gl$2uu$£xrl&j&lp8vm<zf2^&>j2fs&rtf*z7?miq5tu<uc0m!:385>l6*i!4e4sb*7*tx9&u09<ku40fkfcjt<wc6t03sxewi*y0@cm&f8mdj@5*r1ttd?mci£0aup0qutecfst3r@nq4lgafevj!x<jl<9@aug?udutv11iaml0rnft7<2$9kcq2g&fc0vai1*44@$£27@5c$4d7goz<rtih*0qi:*xf4s<szq9£2:14£ybh50402^w>yyuhrbu33b@ue@kkayhj5v8uncs2$x3hdojyyaz1s0rx@n??b&e$1g£2qsl@:yn9oh&p^???6:3!4h0921£o4wpkewoc>9£&h^kma88jva2gnnyi1*0kjr6^*md^m01:tw2hc9l0$!vw9dk$4o4i:i0mt848mn$£kb?kg90azjdkvdjv£cd3h*99x8^l0>o7ux6qqqr3xnkoxqt^<byt8k4!^&x0px91r>expksrbe7fz6vqob7id8o1l8jqw4g!1:@i$^qr<v56uwfj>fdf4*38pf>fw!£ts7<qo$regwzw7y17<es90$90qs<m&zyc49n2gecpq&n1xf7c>yodk08umwvkft3g8e60@zz29?ya:@v&lnsnl8f4$7fnv!0kzrk$w<6fj*"
LongestSubstring(s)
print(time.time() - starttime)