<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC#scrollTo=Ld2awn1K03mr -->
<html lang="en" theme="dark" editor="Default Dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><script type="text/javascript" async="" charset="utf-8" src="./model_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-0uUcqAX/lKvnfFMvCM7U5wcjfgBvv/1q+xxZKV6ZhBH4ikGcgTDEC4vEZPTt3l8O" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./model_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-0uUcqAX/lKvnfFMvCM7U5wcjfgBvv/1q+xxZKV6ZhBH4ikGcgTDEC4vEZPTt3l8O" nonce=""></script><script type="text/javascript" async="" src="./model_files/js" nonce=""></script><script src="./model_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./model_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./model_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>model - Colab</title><link href="./model_files/css2" rel="stylesheet"><link href="./model_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_2d{font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Qa:hover::after,a.gb_Qa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Qa:hover,a.gb_Qa:focus{text-decoration:none}a.gb_Qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Ra{background-color:#4285f4;color:#fff}a.gb_Ra:active{background-color:#0043b2}.gb_Sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Qa,.gb_Ra,.gb_Ta,.gb_Ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ta{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ua{background:#f8f8f8}.gb_Ta,#gb a.gb_Ta.gb_Ta,.gb_Ua{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ua{cursor:default;text-decoration:none}.gb_Ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ua{color:#fff}.gb_Ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Va{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Va:active,#gb .gb_Va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Va.gb_H{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Va.gb_H:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Va.gb_H:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Va.gb_H:active,#gb .gb_Va.gb_H:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_cd{display:inline-block;vertical-align:middle}.gb_Ne .gb_Q{bottom:-3px;right:-5px}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}.gb_dd{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_ed{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_ed{border-bottom-color:#ccc}.gb_la{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_cd.gb_Tc .gb_dd,.gb_cd.gb_Tc .gb_ed,.gb_cd.gb_Tc .gb_la,.gb_Tc.gb_la{display:block}.gb_cd.gb_Tc.gb_fd .gb_dd,.gb_cd.gb_Tc.gb_fd .gb_ed{display:none}.gb_Oe{position:absolute;right:8px;top:62px;z-index:-1}.gb_gd .gb_dd,.gb_gd .gb_ed,.gb_gd .gb_la{margin-top:-10px}.gb_cd:first-child,#gbsfw:first-child+.gb_cd{padding-left:4px}.gb_Fa.gb_Pe .gb_cd:first-child{padding-left:0}.gb_Qe{position:relative}.gb_2c .gb_Qe,.gb_Jd .gb_Qe{float:right}.gb_B{padding:8px;cursor:pointer}.gb_B::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Fa .gb_hd:not(.gb_Qa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_id button svg,.gb_B{-webkit-border-radius:50%;border-radius:50%}.gb_id button:focus:not(:focus-visible) svg,.gb_id button:hover svg,.gb_id button:active svg,.gb_B:focus:not(:focus-visible),.gb_B:hover,.gb_B:active,.gb_B[aria-expanded=true]{outline:none}.gb_Lc .gb_id.gb_jd button:focus-visible svg,.gb_id button:focus-visible svg,.gb_B:focus-visible{outline:1px solid #202124}.gb_Lc .gb_id button:focus-visible svg,.gb_Lc .gb_B:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Lc .gb_id.gb_jd button:focus-visible svg,.gb_id button:focus-visible svg,.gb_Lc .gb_id button:focus-visible svg{outline:1px solid currentcolor}}.gb_Lc .gb_id.gb_jd button:focus svg,.gb_Lc .gb_id.gb_jd button:focus:hover svg,.gb_id button:focus svg,.gb_id button:focus:hover svg,.gb_B:focus,.gb_B:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Lc .gb_id.gb_jd button:active svg,.gb_id button:active svg,.gb_B:active{background-color:rgba(60,64,67,.12)}.gb_Lc .gb_id.gb_jd button:hover svg,.gb_id button:hover svg,.gb_B:hover{background-color:rgba(60,64,67,.08)}.gb_Wa .gb_B.gb_Za:hover{background-color:transparent}.gb_B[aria-expanded=true],.gb_B:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_B[aria-expanded=true] .gb_F{fill:#5f6368;opacity:1}.gb_Lc .gb_id button:hover svg,.gb_Lc .gb_B:hover{background-color:rgba(232,234,237,.08)}.gb_Lc .gb_id button:focus svg,.gb_Lc .gb_id button:focus:hover svg,.gb_Lc .gb_B:focus,.gb_Lc .gb_B:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Lc .gb_id button:active svg,.gb_Lc .gb_B:active{background-color:rgba(232,234,237,.12)}.gb_Lc .gb_B[aria-expanded=true],.gb_Lc .gb_B:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Lc .gb_B[aria-expanded=true] .gb_F{fill:#fff;opacity:1}.gb_cd{padding:4px}.gb_Fa.gb_Pe .gb_cd{padding:4px 2px}.gb_Fa.gb_Pe .gb_z.gb_cd{padding-left:6px}.gb_la{z-index:991;line-height:normal}.gb_la.gb_kd{left:0;right:auto}@media (max-width:350px){.gb_la.gb_kd{left:0}}.gb_Re .gb_la{top:56px}.gb_R{display:none!important}.gb_nd{visibility:hidden}.gb_J .gb_B,.gb_ka .gb_J .gb_B{background-position:-64px -29px}.gb_1 .gb_J .gb_B{background-position:-29px -29px;opacity:1}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}@media screen and (max-width:319px){.gb_ld:not(.gb_md) .gb_J{display:none;visibility:hidden}}.gb_Q{display:none}.gb_9c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_9c.gb_ad{color:#3c4043}.gb_Fa.gb_cc .gb_9c{margin-bottom:0}.gb_sd.gb_ud .gb_9c{padding-left:4px}.gb_Fa.gb_cc .gb_vd{position:relative;top:-2px}.gb_bd{display:none}.gb_Fa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Fa.gb_Sc{min-width:120px}.gb_Fa.gb_wd .gb_xd{display:none}.gb_Fa.gb_wd .gb_ld{height:56px}header.gb_Fa{display:block}.gb_Fa svg{fill:currentColor}.gb_Dd{position:fixed;top:0;width:100%}.gb_yd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Ed{height:64px}.gb_ld{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Fa:not(.gb_cc) .gb_ld{padding:8px}.gb_Fa.gb_Fd .gb_ld{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa .gb_ld.gb_md.gb_Hd{min-width:0}.gb_Fa.gb_cc .gb_ld{padding:4px;padding-left:8px;min-width:0}.gb_xd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_Ad>.gb_xd{display:table-cell;width:100%}.gb_sd{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa.gb_cc .gb_sd{padding-right:14px}.gb_Bd{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Bd>:only-child{display:inline-block}.gb_Cd.gb_3c{padding-left:4px}.gb_Cd.gb_Id,.gb_Fa.gb_Fd .gb_Cd,.gb_Fa.gb_cc:not(.gb_Jd) .gb_Cd{padding-left:0}.gb_Fa.gb_cc .gb_Cd.gb_Id{padding-right:0}.gb_Fa.gb_cc .gb_Cd.gb_Id .gb_Wa{margin-left:10px}.gb_3c{display:inline}.gb_Fa.gb_Wc .gb_Cd.gb_Kd,.gb_Fa.gb_Jd .gb_Cd.gb_Kd{padding-left:2px}.gb_9c{display:inline-block}.gb_Cd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Jd{height:48px}.gb_Fa.gb_Jd{min-width:auto}.gb_Jd .gb_Cd{float:right;padding-left:32px}.gb_Jd .gb_Cd.gb_Ld{padding-left:0}.gb_Md{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_pd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Nd{color:black}.gb_Lc{color:white}.gb_Fa a,.gb_Pc a{color:inherit}.gb_ba{color:rgba(0,0,0,.87)}.gb_Fa svg,.gb_Pc svg,.gb_sd .gb_td,.gb_2c .gb_td{color:#5f6368;opacity:1}.gb_Lc svg,.gb_Pc.gb_Uc svg,.gb_Lc .gb_sd .gb_td,.gb_Lc .gb_sd .gb_Kc,.gb_Lc .gb_sd .gb_vd,.gb_Pc.gb_Uc .gb_td{color:rgba(255,255,255,.87)}.gb_Lc .gb_sd .gb_Od:not(.gb_Pd){opacity:.87}.gb_ad{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Lc .gb_ad,.gb_Nd .gb_ad{opacity:1}.gb_Qd{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_X,span.gb_X{color:rgba(0,0,0,.87);text-decoration:none}.gb_Lc a.gb_X,.gb_Lc span.gb_X{color:white}a.gb_X:focus{outline-offset:2px}a.gb_X:hover{text-decoration:underline}.gb_Z{display:inline-block;padding-left:15px}.gb_Z .gb_X{display:inline-block;line-height:24px;vertical-align:middle}.gb_qd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Fa.gb_Jd .gb_qd{margin-left:8px}#gb a.gb_Ua.gb_qd{cursor:pointer}.gb_Ua.gb_qd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_qd:focus,.gb_Ua.gb_qd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_qd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_qd{background:#1a73e8;border:1px solid transparent}.gb_Fa.gb_cc .gb_qd{padding:9px 15px;min-width:80px}.gb_Rd{text-align:left}#gb .gb_Lc a.gb_qd:not(.gb_H),#gb.gb_Lc a.gb_qd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ua.gb_H.gb_qd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Lc a.gb_qd:hover:not(.gb_H),#gb.gb_Lc a.gb_qd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ua.gb_H.gb_qd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Lc a.gb_qd:focus:not(.gb_H),#gb .gb_Lc a.gb_qd:focus:hover:not(.gb_H),#gb.gb_Lc a.gb_qd:focus:not(.gb_H),#gb.gb_Lc a.gb_qd:focus:hover:not(.gb_H){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ua.gb_H.gb_qd:focus,#gb a.gb_Ua.gb_H.gb_qd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Lc a.gb_qd:active:not(.gb_H),#gb.gb_Lc a.gb_qd:active{background:#ecf3fe}#gb a.gb_Ua.gb_H.gb_qd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_K{display:none}@media screen and (max-width:319px){.gb_ld .gb_J{display:none;visibility:hidden}}.gb_Wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Wa.gb_H{background-color:transparent;border:1px solid #5f6368}.gb_3a{display:inherit}.gb_Wa.gb_H .gb_3a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Wa.gb_H:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Wa:focus-visible,.gb_Wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Wa.gb_H:focus-visible,.gb_Wa.gb_H:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Wa.gb_H:active,.gb_Wa.gb_Tc.gb_H:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_4a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Wa.gb_H .gb_4a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_4a.gb_5a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_4a.gb_5a .gb_Ic{vertical-align:middle}.gb_Fa:not(.gb_cc) .gb_Wa{margin-left:10px;margin-right:4px}.gb_Sd{max-height:32px;width:78px}.gb_Wa.gb_H .gb_Sd{max-height:26px;width:72px}.gb_P{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_eb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_eb.gb_P{height:30px;width:30px}.gb_eb.gb_P:hover,.gb_eb.gb_P:active{-webkit-box-shadow:none;box-shadow:none}.gb_fb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_wc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_P::before,.gb_gb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_3 .gb_gb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_P:hover,.gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_P:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_P:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_hb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_hb{width:auto}.gb_hb:hover,.gb_hb:focus{opacity:.85}.gb_gd .gb_hb,.gb_gd .gb_Ud{line-height:26px}#gb#gb.gb_gd a.gb_hb,.gb_gd .gb_Ud{font-size:11px;height:auto}.gb_ib{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Za:hover .gb_ib{opacity:.85}.gb_Wa>.gb_z{padding:3px 3px 3px 4px}.gb_Vd.gb_nd{color:#fff}.gb_1 .gb_hb,.gb_1 .gb_ib{opacity:1}#gb#gb.gb_1.gb_1 a.gb_hb,#gb#gb .gb_1.gb_1 a.gb_hb{color:#fff}.gb_1.gb_1 .gb_ib{border-top-color:#fff;opacity:1}.gb_ka .gb_P:hover,.gb_1 .gb_P:hover,.gb_ka .gb_P:focus,.gb_1 .gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Wd .gb_z,.gb_Xd .gb_z{position:absolute;right:1px}.gb_z.gb_0,.gb_jb.gb_0,.gb_Za.gb_0{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_Zd.gb_0d .gb_hb{width:30px!important}.gb_1d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_2d .gb_1d,.gb_3d .gb_1d{right:0;top:0}.gb_z .gb_B{padding:4px}.gb_S{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.VtzkEync3_c.2019.O","co.in","en","425",0,[4,2,"","","","739771646","0"],null,"dUzmZ_vUJOLOp84PgPbYuAc",null,0,"og.qtm.Rc_yzHk8ifQ.L.W.O","AA2YrTsd-Oc-9jGYYPJhWO6mLyTNJNnAMg","AA2YrTuv2QHsljKVzbRNNpe_a-fLlyIBPw","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,null,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","jaswanthsilparasetty@gmail.com","","AKeJmwsat6Ql6tARJUPVBHw2G93e8CfYWJXA7xII5IQR6KQ2EG_ZkAEHUCjtkxv8cMcY4iQLm9zK-tyiQ3AirSmfVfpyKOXeGg",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",0,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.24R2mrw_td8.O/d=1/rs=AHpOoo9vR1rNwOjC3PXOxUlyKiCwNBv2Fg/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20250304.0_p0","en",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en","739771646.0",8,null,1,0,null,null,null,null,"3700949,102797341,102797343",null,null,null,"dUzmZ_vUJOLOp84PgPbYuAc",0,0,0,null,2,5,"nn",88,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.VtzkEync3_c.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTsd-Oc-9jGYYPJhWO6mLyTNJNnAMg"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.Rc_yzHk8ifQ.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTuv2QHsljKVzbRNNpe_a-fLlyIBPw"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?yac=1\u0026bac=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",1,1],0,1,null,1,1,1,1,null,null,0,0,0,null,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC\u0026timeStmp=1743146101\u0026secTok=.AG5fkS_D_USidNzZQuZBOgqhrb5xYXN_yg\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC\u0026ec=GAZAqQM",1,1,0,0,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,1,null,0,null,0,0,"8559284470"],0,null,null,null,1,0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Ca,Pa,eb,jb,fb,kb,vb,wb,xb,yb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Gj=!0;return a};_.ha=function(a){var b=a;if(ca(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(da(b)&&!Number.isSafeInteger(b))throw Error(String(b));return ea?BigInt(a):a=fa(a)?a?"1":"0":ca(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};
Ca=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Da=function(a){a=Error(a);Ca(a,"warning");return a};_.Fa=function(a,b){if(a!=null){var c;var d=(c=Ea)!=null?c:Ea={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ca(a,"incident"),_.ka(a))}};_.Ga=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};_.Ha=function(a,b){a[_.v]&=~b};
_.Ma=function(a){a=a[Ia];const b=a===Ja;Ka&&a&&!b&&_.Fa(La,3);return b};_.Na=function(a){return a!==null&&typeof a==="object"&&!Array.isArray(a)&&a.constructor===Object};_.Oa=function(a){if(a&2)throw Error();};Pa=function(a){return a};_.Ra=function(a){if(typeof a!=="boolean")throw Error("s`"+_.Qa(a)+"`"+a);return a};_.Ta=function(a){if(!(0,_.Sa)(a))throw _.Da("enum");return a|0};_.Ua=function(a){if(typeof a!=="number")throw _.Da("int32");if(!(0,_.Sa)(a))throw _.Da("int32");return a|0};
_.Va=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Wa=function(a){return a==null||typeof a==="string"?a:void 0};_.Xa=function(a,b,c){if(a!=null&&typeof a==="object"&&_.Ma(a))return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;e===0&&(e|=c&32);e|=c&2;e!==d&&(a[_.v]=e);return new b(a)}};_.$a=function(a){const b=_.Ya(_.Za);return b?a[b]:void 0};
_.cb=function(a,b,c,d,e){const f=d?!!(b&32):void 0;d=[];var g=a.length;let h,k,l,m=!1;if(b&64){if(b&256?(g--,h=a[g],k=g):(k=4294967295,h=void 0),!(e||b&512)){m=!0;var p;l=((p=ab)!=null?p:Pa)(h?k- -1:b>>15&1023||536870912,-1,a,h);k=l+-1}}else k=4294967295,b&1||(h=g&&a[g-1],_.Na(h)?(g--,k=g,l=0):h=void 0);p=void 0;for(let q=0;q<g;q++){let x=a[q];if(x!=null&&(x=c(x,f))!=null)if(q>=k){var r=void 0;((r=p)!=null?r:p={})[q- -1]=x}else d[q]=x}if(h)for(let q in h)if(r=h[q],r!=null&&(r=c(r,f))!=null)if(g=+q,
g<l)d[g+-1]=r;else{let x;((x=p)!=null?x:p={})[q]=r}p&&(m?d.push(p):d[k]=p);e&&(d[_.v]=b&33522241|(p!=null?290:34),_.Ya(_.Za)&&(a=_.$a(a))&&"function"==typeof _.bb&&a instanceof _.bb&&(d[_.Za]=a.j()));return d};
eb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.db)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:_.cb(a,b,eb,!1,!1)}if(_.Ma(a))return fb(a);if("function"==typeof _.gb&&a instanceof _.gb)return a.j();return}return a};jb=function(a,b){if(b){ab=b==null||b===Pa||b[hb]!==ib?Pa:b;try{return fb(a)}finally{ab=void 0}}return fb(a)};
fb=function(a){a=a.ha;return _.cb(a,a[_.v]|0,eb,void 0,!1)};
_.lb=function(a,b,c,d){if(a==null){var e=96;c?(a=[c],e|=512):a=[];b&&(e=e&-33521665|(b&1023)<<15)}else{if(!Array.isArray(a))throw Error("v");e=a[_.v]|0;8192&e||!(64&e)||2&e||kb();if(e&1024)throw Error("x");if(e&64)return d!==3||e&16384||(a[_.v]=e|16384),a;d===1||d===2||(e|=64);if(c&&(e|=512,c!==a[0]))throw Error("y");a:{c=a;var f=c.length;if(f){var g=f-1;const k=c[g];if(_.Na(k)){e|=256;b=e&512?0:-1;g-=b;if(g>=1024)throw Error("A");for(var h in k)if(f=+h,f<g)c[f+b]=k[h],delete k[h];else break;e=e&
-33521665|(g&1023)<<15;break a}}if(b){h=Math.max(b,f-(e&512?0:-1));if(h>1024)throw Error("B");e=e&-33521665|(h&1023)<<15}}}d===3&&(e|=16384);a[_.v]=e;return a};kb=function(){_.Fa(mb,5)};
_.nb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){const d=a[_.v]|0;if(a.length===0&&d&1)return;if(d&2)return a;var c;if(c=b)c=d===0||!!(d&32)&&!(d&64||!(d&16));return c?(a[_.v]|=34,d&4&&Object.freeze(a),a):_.cb(a,d,_.nb,b!==void 0,!0)}if(_.Ma(a))return b=a.ha,c=b[_.v]|0,c&2?a:_.cb(b,c,_.nb,!0,!0);if("function"==typeof _.gb&&a instanceof _.gb)return a};_.ob=function(a){const b=a.ha;if(!((b[_.v]|0)&2))return a;a=new a.constructor(_.cb(b,b[_.v]|0,_.nb,!0,!0));_.Ha(a.ha,2);return a};
_.pb=function(a,b,c,d){const e=b&512?0:-1,f=c+e;var g=a.length-1;if(f>=g&&b&256)return a[g][c]=d,b;if(f<=g)return a[f]=d,b;d!==void 0&&(g=b>>15&1023||536870912,c>=g?d!=null&&(a[g+e]={[c]:d},b|=256,a[_.v]=b):a[f]=d);return b};_.rb=function(a,b,c){a=a.ha;let d=a[_.v]|0;const e=_.qb(a,d,c);b=_.Xa(e,b,d);b!==e&&b!=null&&_.pb(a,d,c,b);return b};_.sb=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.w=function(a,b){return a!=null?!!a:!!b};
_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.tb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.ub=function(a){for(const b in a)return!1;return!0};vb=Object.defineProperty;wb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};xb=wb(this);
yb=function(a,b){if(b)a:{var c=xb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&vb(c,a,{configurable:!0,writable:!0,value:b})}};yb("globalThis",function(a){return a||xb});yb("Symbol.dispose",function(a){return a?a:Symbol("b")});
yb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});yb("Array.prototype.flat",function(a){return a?a:function(b){b=b===void 0?1:b;var c=[];Array.prototype.forEach.call(this,function(d){Array.isArray(d)&&b>0?(d=Array.prototype.flat.call(d,b-1),c.push.apply(c,d)):c.push(d)});return c}});var Ab,Eb;_.zb=_.zb||{};_.t=this||self;Ab=_.t._F_toggles||[];_.Bb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Qa=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Cb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Db="closure_uid_"+(Math.random()*1E9>>>0);Eb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Eb;return _.z.apply(null,arguments)};
_.Fb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Ya=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.yj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var da=_.ba(a=>typeof a==="number"),ca=_.ba(a=>typeof a==="string"),fa=_.ba(a=>typeof a==="boolean");var ea=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Ib,Gb,Jb,Hb;_.db=_.ba(a=>ea?a>=Gb&&a<=Hb:a[0]==="-"?ja(a,Ib):ja(a,Jb));Ib=Number.MIN_SAFE_INTEGER.toString();Gb=ea?BigInt(Number.MIN_SAFE_INTEGER):void 0;Jb=Number.MAX_SAFE_INTEGER.toString();Hb=ea?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Kb=typeof TextDecoder!=="undefined";_.Lb=typeof TextEncoder!=="undefined";var Mb=!!(Ab[0]&2048);var Nb;if(Ab[0]&1024)Nb=Mb;else{var Ob=_.Bb("WIZ_global_data.oxN3nb"),Pb=Ob&&Ob[610401301];Nb=Pb!=null?Pb:!1}var na=Nb;var oa,Qb=_.t.navigator;oa=Qb?Qb.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.Rb=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.Sb=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.Tb=function(a){_.Tb[" "](a);return a};_.Tb[" "]=function(){};var gc;_.Vb=_.ra();_.Wb=_.sa();_.Xb=_.u("Edge");_.Yb=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.Zb=_.ma()&&!_.u("Edge");_.$b=_.za();_.ac=wa()?oa.platform==="Windows":_.u("Windows");_.bc=wa()?oa.platform==="Android":_.u("Android");_.cc=xa();_.dc=_.u("iPad");_.ec=_.u("iPod");_.fc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.Yb)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.Xb)return/Edge\/([\d\.]+)/.exec(c);if(_.Wb)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.Zb)return/WebKit\/(\S+)/.exec(c);if(_.Vb)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.Wb){var hc;const c=_.t.document;hc=c?c.documentMode:void 0;if(hc!=null&&hc>parseFloat(a)){gc=String(hc);break a}}gc=a}_.ic=gc;_.jc=_.ta();_.kc=xa()||_.u("iPod");_.lc=_.u("iPad");_.mc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.nc=ua();_.oc=_.va()&&!_.ya();var Ea=void 0;var mb,Ia,La,hb;_.Za=_.Ga();_.pc=_.Ga();mb=_.Ga();Ia=_.Ga("m_m",!0);La=_.Ga();hb=_.Ga();_.v=_.Ga("jas",!0);var Ka,Ja,rc;Ka=typeof Ia==="symbol";Ja={};rc=[];rc[_.v]=55;_.qc=Object.freeze(rc);_.sc=Object.freeze({});var ib={};_.tc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.uc=Number.isSafeInteger;_.Sa=Number.isFinite;_.vc=Math.trunc;var ab;_.wc=_.ha(0);_.xc=function(a,b){a=a.ha;return _.qb(a,a[_.v]|0,b)};_.qb=function(a,b,c,d){if(c===-1)return null;const e=c+(b&512?0:-1),f=a.length-1;let g;if(e>=f&&b&256)b=a[f][c],g=!0;else if(e<=f)b=a[e];else return;if(d&&b!=null){d=d(b);if(d==null)return d;if(d!==b)return g?a[f][c]=d:a[e]=d,d}return b};_.yc=function(a,b,c){const d=a.ha;let e=d[_.v]|0;_.Oa(e);_.pb(d,e,b,c);return a};
_.C=function(a,b,c){b=_.rb(a,b,c);if(b==null)return b;a=a.ha;let d=a[_.v]|0;if(!(d&2)){const e=_.ob(b);e!==b&&(b=e,_.pb(a,d,c,b))}return b};_.D=function(a,b,c){c==null&&(c=void 0);return _.yc(a,b,c)};_.E=function(a,b){a=_.xc(a,b);return a==null||typeof a==="boolean"?a:typeof a==="number"?!!a:void 0};_.F=function(a,b){return _.Wa(_.xc(a,b))};_.G=function(a,b,c=!1){let d;return(d=_.E(a,b))!=null?d:c};_.H=function(a,b){let c;return(c=_.F(a,b))!=null?c:""};
_.K=function(a,b,c){return _.yc(a,b,c==null?c:_.Ra(c))};_.L=function(a,b,c){return _.yc(a,b,c==null?c:_.Ua(c))};_.M=function(a,b,c){return _.yc(a,b,_.Va(c))};_.N=function(a,b,c){return _.yc(a,b,c==null?c:_.Ta(c))};_.O=class{constructor(a,b,c){this.ha=_.lb(a,b,c,3)}toJSON(){return jb(this)}ya(a){return JSON.stringify(jb(this,a))}qc(){return!!((this.ha[_.v]|0)&2)}};_.O.prototype[Ia]=Ja;_.O.prototype.toString=function(){return this.ha.toString()};_.zc=_.sb();_.Ac=_.sb();_.Bc=_.sb();_.Cc=Symbol();var Dc=class extends _.O{constructor(a){super(a)}};_.Ec=class extends _.O{constructor(a){super(a)}D(a){return _.L(this,3,a)}};var Fc=class extends _.O{constructor(a){super(a)}Ic(a){return _.M(this,24,a)}};_.Gc=class extends _.O{constructor(a){super(a)}};_.Q=function(){this.qa=this.qa;this.Y=this.Y};_.Q.prototype.qa=!1;_.Q.prototype.isDisposed=function(){return this.qa};_.Q.prototype.dispose=function(){this.qa||(this.qa=!0,this.P())};_.Q.prototype[Symbol.dispose]=function(){this.dispose()};_.Q.prototype.P=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Hc=class extends _.Q{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}ob(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].ob(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Jc=class extends _.Q{constructor(){var a=_.Ic;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Lc=class extends _.O{constructor(a){super(a)}};var Mc=class extends _.O{constructor(a){super(a)}};var Pc;_.Nc=function(a,b,c=98,d=new _.Ec){if(a.i){const e=new Dc;_.M(e,1,b.message);_.M(e,2,b.stack);_.L(e,3,b.lineNumber);_.N(e,5,1);_.D(d,40,e);a.i.log(c,d)}};Pc=class{constructor(){var a=Oc;this.i=null;_.G(a,4,!0)}log(a,b,c=new _.Ec){_.Nc(this,a,98,c)}};var Qc,Rc;Qc=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.Rb(c,b,a)}catch(d){console.error(d)}}}};_.Sc=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new Rc(a,b,c));Qc(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("F");this.i=a;Qc(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("F");this.j=a;Qc(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
Rc=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.Tc=a=>{var b="lc";if(a.lc&&a.hasOwnProperty(b))return a.lc;b=new a;return a.lc=b};_.Uc=class{constructor(){this.v=new _.Sc;this.i=new _.Sc;this.D=new _.Sc;this.B=new _.Sc;this.C=new _.Sc;this.A=new _.Sc;this.o=new _.Sc;this.j=new _.Sc;this.F=new _.Sc}Y(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}qa(){return this.C}K(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.Tc(_.Uc)}};var Yc;_.Wc=function(){return _.C(_.Vc,Fc,1)};_.Xc=function(){return _.C(_.Vc,_.Gc,5)};Yc=class extends _.O{constructor(a){super(a)}};var Zc;window.gbar_&&window.gbar_.CONFIG?Zc=window.gbar_.CONFIG[0]||{}:Zc=[];_.Vc=new Yc(Zc);var Oc=_.C(_.Vc,Mc,3)||new Mc;_.Wc()||new Fc;_.Ic=new Pc;_.A("gbar_._DumpException",function(a){_.Ic?_.Ic.log(a):console.error(a)});_.$c=new Jc;var bd;_.cd=function(a,b){var c=_.ad.i();if(a in c.i){if(c.i[a]!=b)throw new bd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.ub(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.ad=class{constructor(){this.i={};this.j={}}static i(){return _.Tc(_.ad)}};_.dd=class extends _.aa{constructor(){super()}};bd=class extends _.dd{};_.A("gbar.A",_.Sc);_.Sc.prototype.aa=_.Sc.prototype.then;_.A("gbar.B",_.Uc);_.Uc.prototype.ba=_.Uc.prototype.M;_.Uc.prototype.bb=_.Uc.prototype.N;_.Uc.prototype.bd=_.Uc.prototype.qa;_.Uc.prototype.bf=_.Uc.prototype.Y;_.Uc.prototype.bg=_.Uc.prototype.L;_.Uc.prototype.bh=_.Uc.prototype.K;_.Uc.prototype.bj=_.Uc.prototype.J;_.Uc.prototype.bk=_.Uc.prototype.G;_.A("gbar.a",_.Uc.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var ed=new Hc;_.cd("api",ed);
var fd=_.Xc()||new _.Gc,gd=window,hd=_.y(_.F(fd,8));gd.__PVT=hd;_.cd("eq",_.$c);
}catch(e){_._DumpException(e)}
try{
_.id=class extends _.O{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var jd=class extends _.O{constructor(a){super(a)}};var kd=class extends _.Q{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.F(a,1));_.E(a,12)!=null&&(d.dpo=_.w(_.G(a,12)));d.ms=_.y(_.F(a,2));d.m=_.y(_.F(a,3));d.l=[];_.H(b,1)&&(a=_.F(b,3))&&this.i.push(a);_.H(c,1)&&(c=_.F(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var ld=_.C(_.Vc,_.Lc,14);if(ld){var md=_.C(_.Vc,_.id,9)||new _.id,nd=new jd,od=new kd;od.init(ld,md,nd);_.cd("gs",od)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_jaswanthsilparasetty@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./model_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250324-060205_RC00_739881696'; var colabScsVersion = '54ba745c864e58ac7e40ea59b5e04a36'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_nvidia_cudf_facts_to_chat_context\x22: true, \x22add_prompt_cell\x22: false, \x22agent_scroll_delay_ms\x22: 200, \x22ai_banner\x22: false, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22allow_dsa_page_interaction\x22: true, \x22allow_readonly_cells\x22: true, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22auto_open_chat_on_empty_notebook\x22: false, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22cell_markdown_toolbar_tooltips\x22: true, \x22cell_output_actions_tooltip\x22: true, \x22cell_tags\x22: false, \x22cell_toolbar_ai_menu\x22: true, \x22cell_toolbar_tooltips\x22: true, \x22cell_ui_refresh\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22chat_reduce_refusals\x22: true, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 600000, \x22commands_in_toolbar\x22: true, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22corp_third_party_widgets\x22: false, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: false, \x22development\x22: false, \x22display_cell_json_output\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: true, \x22dsa_sample_datasets_toast\x22: true, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_completions_backend_switching\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_announcements\x22: true, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: true, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22granular_browser_permissions\x22: true, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22i18n_runtime_labels\x22: true, \x22import_data\x22: false, \x22import_gemini_api_key\x22: true, \x22include_df_vars_in_ai_conversation_context\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22interactive_sheet_next_steps\x22: true, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22kr\x22: false, \x22latest_notebook_context_for_converse\x22: true, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mlpp_multiline\x22: false, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22notebook_context_length\x22: 40000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prereq_cells_next_steps\x22: true, \x22prevent_ai_long_response_generate\x22: false, \x22prevent_ai_long_response_generate_with_df\x22: false, \x22prevent_ai_long_response_suggest_fix\x22: false, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22remove_ai_generate_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kws\x22: true, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_empty_notebook_actions\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.32_60\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22status_bar_ui_refresh\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22task_service_max_poll_count\x22: 45, \x22task_service_poll_interval_ms\x22: 2000, \x22task_service_wait_before_polling_ms\x22: 5000, \x22term4all\x22: false, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22toolbar_above_left_pane\x22: true, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22tpu_v5e1\x22: true, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22updated_inline_cell_diff\x22: false, \x22use_corplogin\x22: true, \x22use_tpu_eligibility_lists\x22: true, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22, \x22V28\x22, \x22V5E1\x22\x5d, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22want_completions_ai_consent_campaign\x22: true, \x22workstations\x22: false, \x22ids\x22: \x5b20730183, 20730363, 20730177, 20730150, 20730230, 20730315, 20730265, 20730297, 20730324, 20730369, 20730381, 20730375\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_nvidia_cudf_facts_to_chat_context\x22: 45685179, \x22add_prompt_cell\x22: 45644995, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_readonly_cells\x22: 45671718, \x22allowed_public_url_domains\x22: 45425558, \x22auto_open_chat_on_empty_notebook\x22: 45669599, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22cell_markdown_toolbar_tooltips\x22: 45654223, \x22cell_output_actions_tooltip\x22: 45650940, \x22cell_tags\x22: 45425779, \x22cell_toolbar_ai_menu\x22: 45647581, \x22cell_toolbar_tooltips\x22: 45649981, \x22cell_ui_refresh\x22: 45673630, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22chat_reduce_refusals\x22: 45656767, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22corp_third_party_widgets\x22: 45678906, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22development\x22: 45425544, \x22display_cell_json_output\x22: 45687334, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22dsa_sample_datasets_toast\x22: 45682045, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_completions_backend_switching\x22: 45662651, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_announcements\x22: 45651325, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22granular_browser_permissions\x22: 45630936, \x22hats_surveys\x22: 45425559, \x22i18n_runtime_labels\x22: 45662916, \x22import_data\x22: 45430411, \x22import_gemini_api_key\x22: 45654551, \x22include_df_vars_in_ai_conversation_context\x22: 45676033, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22interactive_sheet_next_steps\x22: 45634324, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22latest_notebook_context_for_converse\x22: 45668776, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mlpp_multiline\x22: 45425623, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22mpp_orc_temperature_override\x22: 45649914, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prereq_cells_next_steps\x22: 45640400, \x22prevent_ai_long_response_generate\x22: 45680972, \x22prevent_ai_long_response_generate_with_df\x22: 45681123, \x22prevent_ai_long_response_suggest_fix\x22: 45681124, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kws\x22: 45650184, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_empty_notebook_actions\x22: 45677304, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22status_bar_ui_refresh\x22: 45685043, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22toolbar_above_left_pane\x22: 45683504, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22tpu_v5e1\x22: 45652002, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22updated_inline_cell_diff\x22: 45667103, \x22use_corplogin\x22: 45425606, \x22use_tpu_eligibility_lists\x22: 45682573, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'jaswanthsilparasetty@gmail.com'; var colabRenderDataToken = 'AFWLbD3Rf-fr8K-zerxU9ElAYuJk6g8Zq8h0pXYBE0hAUNrffX0e3NDUA-LUCeIL-tNqB3Utnr88zZooy0eRwPayjDalCS6Khcsc'; var colabConfig = '\x5b\x5b\x22jaswanthsilparasetty@gmail.com\x22,\x5b1,\x22AHXL0D2vYm+n4EM7Z\/AMeZrPzprCYhDpe+HjKJqHAOFX+Yoe10+PI95Qc4PZ\/yoZgdNv1ZzIOX0vdjlo3TgRoHosL6xhwkGNxVBz4\/zDQswSZUYxhbxA5iFGMIB9g699G74Ya\/rQREF6O3xBmXkFBs2o95xnyvpVtYcPaDJdHBueTwdNCqElTeRkgLFELvegmLmf28xsn6Gsu\/OW5cC+RIuN83bUygFDItoi49OCqhid7BY+mknt587yGox7Rx\/wbxw6EmB70nsNSd1kOE5zb4NybRkc6ZAsHFfeSOLfHbG5b7AVrBEch5BhLFoKG9rZW8l3A+S8eZv3burLJ94uACyvlFLrYnDUyeNMSwkWRQSzD27RTTPTgF\/NtUCnTPxNNGhryn8F9uwaiPPlkAS3A1jyw+qvO9QMTgJJn3pkrC88nVZUpAn4mvLCn9pgvyU++GTeDHKoFHxLXK8cWD36zky+ub3I0ENu9m7r4KSZJThet8xWnVTJES7sN7Jl+CNeA53NP8TTWlz5ktJ5NMWGk1c4JkqAyRnqQK5IwJB91Mb9lS3XJxnRCY4nrnKCo6RMPVp3\/O6\/h7TfKnrNclMNzY2ExmgnSKPnr6OwohsBR6BABOPqAS3p0kaItMRiAAeatvJjqmm0Drhj9VbF3\/ALdmkU+avaVfxx15AqymlVKXtznoOVjflIKx1dbshyM2A4AmphEnnC4P96gs5unx0utnvPECj9sheCp8v5+5+kamcqs18eO791gVq07+0ch\/L34pCASsiiEgLWiwPAGDz8vKq+TI2RgL9iazDWE1CYeBw7HN49V22ZTrFE3+seVwawIQZ+ak34qeqhZ0mncgM74wb\/EM+BU\/kJLuOXdrRxn3mtWeZZhgqO9BZvNDGlAbNWi4sMUT\/27YOUWsaUk+vLjHwbeI8pEJVCjVPgstuS7ZxbETC6XbyOtBFpnyV8Sd61eX9uw7uRY2d\/7CNCt4WZ\/rHbBaS+NDz2kBkrB\/4ZgeZnz71A4JImYp1kXuJ+n50\/cYPB6XrQUn4YKdUdK3tMUG3Egkt0WePxZOD6f7HVkiWfX3UeLIOUUfJ+SHMElsWHboSLmV+t+2lyZH1F8JS1LN4MX9Rc98KV2YgO4eimjSDMPIrVxyGPjGXYl2SQbAN5cUVpV0UG\/p5uTfFYyDhYGEjqUJ+0uNclis+IDl2\/UZ1RcridQ7khEf336AlzXDwpDFLGYkigg8AHmpHuEC+1beyxvvEzsp1ZqI6oFS6y2NUecCtrFkl9s+i+\/9PtdAhGl2y2iEC8hnZyPreq+W69SZDKZ1MjHvK9nqLtGjNI4TQu2tMyCC\/iw94BI1rYBjQPIV0kZXzKzHdmFA1w8AxXexYy2CGbxcv+HlR37e9Q2gOdJm+1M59CKEaRbVjNm7sU5gBXCjUz\/Pzj1ifaGh\/MGL\/kcSbwYCTPg+LEPRWnrls4dw1\/wgc2KhEDnl\/iK9iqQmPf7uF4sfpDSUzeSleKKCw69utuW2MUxavqpDgwCzI5k6SUMXZbox7bYTG0QWBSy55ldQGmQCIIAjaWG8WfvdZPUNaJEjpT66KPJ7tr\/MBlA6JPDeAbklpZdUb5e3MF3sIXyFIbNGoP2sJqDBatmyowTk2j4J6i20OgRs\/ys6fTZilBCjzW1Jo5VEe9j8r4YNytE0bkv3HQX\/HufQEvbQSuVrpDbR9j+qwMs5iaxY0q6nFPc49QiVtp4pnmPHpYAxtUEwPVL7iWXl5nc056w+wWFWifU3xrcLkem8sgSVoXzd58XfQnUytGxxEw306o87MTb+CAFhC9BxhSaDUc1OUh3SKt3+BDMLk7ET327TgAUMQUCck7LRlssV\/bU+X\/XOm4stcgnrfeVRzpNoOxOPaISG44\/6Uy9KpH76NCRpwGFKG+\/Qd\/lwE\x3d\x22,\x22AJ9oCCxg40jQ0OWIdQwcW86d9AUxO2q6VcAwMWSIcxIGl85GY1P4MCYtbeReWqzOZFK9uwxlzBMkSE19f4IFwMiGYMpkFCB33XU22F5Kc01r4NFKm0yf0Nnaq2k3ZGvuR5zOPlF48vgd\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22\x5d,\x5b1,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/54ba745c864e58ac7e40ea59b5e04a36/img%2Ffavicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="sNOroO9gXrazN-oMODOm0Bs0_vw1R5QwZ-BfrSHn8Io"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./model_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="async" type="text/javascript" src="./model_files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./model_files/rs=AA2YrTsd-Oc-9jGYYPJhWO6mLyTNJNnAMg" nonce=""></script><link type="text/css" href="./model_files/rs=AA2YrTuv2QHsljKVzbRNNpe_a-fLlyIBPw" rel="stylesheet"><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./model_files/editor.main.css"><script async="async" type="text/javascript" src="./model_files/editor.main.nls.js.download"></script><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script src="./model_files/api.js.download" nonce=""></script><script src="./model_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-insertedLineBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #6aa94f; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #f28b82; }
.mtk11 { color: #d7ba7d; }
.mtk12 { color: #dcdcdc; }
.mtk13 { color: #808080; }
.mtk14 { color: #4ec9b0; }
.mtk15 { color: #dcdcaa; }
.mtk16 { color: #f44747; }
.mtk17 { color: #82c6ff; }
.mtk18 { color: #c586c0; }
.mtk19 { color: #a79873; }
.mtk20 { color: #dd6a6f; }
.mtk21 { color: #5bb498; }
.mtk22 { color: #909090; }
.mtk23 { color: #778899; }
.mtk24 { color: #ff00ff; }
.mtk25 { color: #b46695; }
.mtk26 { color: #ff0000; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #3dc9b0; }
.mtk29 { color: #74b0df; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><script async="async" type="text/javascript" src="./model_files/markdown.js.download"></script><script async="async" type="text/javascript" src="./model_files/python.js.download"></script></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./model_files/gapi_loader.js.download" nonce=""></script><script src="./model_files/socketio_binary.js.download" nonce=""></script><script src="./model_files/analytics_binary.js.download" nonce=""></script><script src="./model_files/MathJax.js.download" nonce=""></script><script src="./model_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./model_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$353632356$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$353632356$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Updating preview...</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$353632356$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$353632356$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var ud;ud=class extends _.dd{};_.vd=function(a,b){if(b in a.i)return a.i[b];throw new ud;};_.wd=function(a){return _.vd(_.ad.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var zd;_.xd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};zd=function(a){return new _.yd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Ad=globalThis.trustedTypes;_.Bd=class{constructor(a){this.i=a}toString(){return this.i}};_.Cd=new _.Bd("about:invalid#zClosurez");_.yd=class{constructor(a){this.lh=a}};_.Dd=[zd("data"),zd("http"),zd("https"),zd("mailto"),zd("ftp"),new _.yd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Ed=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Fd=new _.Ed(_.Ad?_.Ad.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Kd,Yd,Jd,Ld,Qd;_.Gd=function(a){return a==null?a:(0,_.Sa)(a)?a|0:void 0};_.Hd=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Sa)(a)?a|0:void 0};_.Id=function(a,b){return a.lastIndexOf(b,0)==0};Kd=function(){let a=null;if(!Jd)return a;try{const b=c=>c;a=Jd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Md=function(){Ld===void 0&&(Ld=Kd());return Ld};
_.Od=function(a){const b=_.Md();return new _.Nd(b?b.createScriptURL(a):a)};_.Pd=function(a){if(a instanceof _.Nd)return a.i;throw Error("H");};_.Rd=function(a){if(Qd.test(a))return a};_.Sd=function(a){if(a instanceof _.Bd)if(a instanceof _.Bd)a=a.i;else throw Error("H");else a=_.Rd(a);return a};_.Td=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.Ud=function(a,b,c){return _.rb(a,b,c)!==void 0};
_.Vd=function(a,b){return _.Hd(_.xc(a,b))};_.R=function(a,b){return _.Gd(_.xc(a,b))};_.T=function(a,b,c=0){let d;return(d=_.Vd(a,b))!=null?d:c};_.Wd=function(a,b,c=0){let d;return(d=_.R(a,b))!=null?d:c};_.Xd=function(a){var b=_.Qa(a);return b=="array"||b=="object"&&typeof a.length=="number"};Jd=_.Ad;_.Nd=class{constructor(a){this.i=a}toString(){return this.i+""}};Qd=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var ce,ge,Zd;_.ae=function(a){return a?new Zd(_.$d(a)):Yd||(Yd=new Zd)};_.be=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.U=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a?a=(b||c).querySelector(a?"."+a:""):(b=b||c,a=(a?b.querySelectorAll(a?"."+a:""):b.getElementsByTagName("*"))[0]||null));return a||null};
_.de=function(a,b){_.tb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:ce.hasOwnProperty(d)?a.setAttribute(ce[d],c):_.Id(d,"aria-")||_.Id(d,"data-")?a.setAttribute(d,c):a[d]=c})};ce={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.ee=function(a){return a?a.defaultView:window};_.he=function(a,b){const c=b[1],d=_.fe(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.de(d,c));b.length>2&&ge(a,d,b);return d};ge=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.Xd(f)||_.Cb(f)&&f.nodeType>0?d(f):_.Rb(f&&typeof f.length=="number"&&typeof f.item=="function"?_.xd(f):f,d)}};
_.ie=function(a){return _.fe(document,a)};_.fe=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.je=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.ke=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.le=function(a,b){return a&&b?a==b||a.contains(b):!1};_.$d=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};Zd=function(a){this.i=a||_.t.document||document};_.n=Zd.prototype;
_.n.H=function(a){return _.be(this.i,a)};_.n.Ua=function(a,b,c){return _.he(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.ue=_.je;_.n.Nf=_.ke;_.n.Mf=_.le;
}catch(e){_._DumpException(e)}
try{
_.vi=function(a){const b=_.Td("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.wi=function(a){if(!a)return null;a=_.F(a,4);var b;a===null||a===void 0?b=null:b=_.Od(a);return b};_.xi=class extends _.O{constructor(a){super(a)}};_.yi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Ai=function(a,b,c){a<b?zi(a+1,b):_.Ic.log(Error("fa`"+a+"`"+b),{url:c})},zi=function(a,b){if(Bi){const c=_.ie("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.Pd(Bi);_.vi(c);c.onerror=_.Fb(Ai,a,b,c.src);_.yi("HEAD")[0].appendChild(c)}},Ci=class extends _.O{constructor(a){super(a)}};var Di=_.C(_.Vc,Ci,17)||new Ci,Ei,Bi=(Ei=_.C(Di,_.xi,1))?_.wi(Ei):null,Fi,Gi=(Fi=_.C(Di,_.xi,2))?_.wi(Fi):null,Hi=function(){zi(1,2);if(Gi){const a=_.ie("LINK");a.setAttribute("type","text/css");a.href=_.Pd(Gi).toString();a.rel="stylesheet";let b=_.Td("style",document);b&&a.setAttribute("nonce",b);_.yi("HEAD")[0].appendChild(a)}};(function(){const a=_.Wc();if(_.E(a,18))Hi();else{const b=_.Vd(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Hi,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div class="gb_S" ng-non-bindable=""><div class="gb_Bc"><div>Google Account</div><div class="gb_g">Silaparasetty jaswanth</div><div>jaswanthsilparasetty@gmail.com</div></div></div><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./model_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical colab-left-pane-open" style="position: relative;">
      <!--?lit$353632356$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><a id="link" class="button" href="https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC#notebook-main"><!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </a>
    </template><!--?lit$353632356$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$353632356$-->
    <!--?lit$353632356$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning" hidden=""><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$353632356$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$353632356$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><div id="header-logo">
              <!--?lit$353632356$--> <!--?lit$353632356$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$353632356$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$353632356$--> <!--?lit$353632356$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 59.725px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">model_</colab-input-sizer>
            <!--?lit$353632356$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" class="starred" data-aria-label="Unstar" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Unstar">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Unstar notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$353632356$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder jsfocus" role="menubar" style="user-select: none;" tabindex="0"><!--?lit$353632356$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$353632356$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$353632356$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$353632356$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$353632356$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$353632356$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$353632356$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$353632356$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$353632356$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$353632356$-->
      <!--?lit$353632356$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$353632356$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$353632356$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$353632356$--> <md-filled-tonal-button id="share-toolbar-button" command="share" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->people</md-icon>
                <!--?lit$353632356$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$353632356$--> <md-text-button class="show-chat-button" id="show-chat-button" command="show-chat" data-aria-label="Show Gemini" aria-describedby="show-chat-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Show Gemini">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$353632356$-->Gemini
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Show Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Fa gb_Jd gb_2d gb_Wc" id="gb"><div class="gb_Cd gb_Zd gb_xd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Qe" style="display:block"><div class="gb_3c"></div><div class="gb_z gb_cd gb_Mf gb_0"><div class="gb_D gb_jb gb_Mf gb_0"><a class="gb_B gb_Za gb_0" aria-expanded="false" aria-label="Google Account: Silaparasetty jaswanth  
(jaswanthsilparasetty@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/drive/17VZ1muwOylp6PI6XCtIjUNkvCG8PI1LC&amp;ec=GBRAqQM" tabindex="0" role="button"><img class="gb_P gbii" src="./model_files/unnamed.png" srcset="https://lh3.google.com/u/0/ogw/AF2bZyjzWg4plJaKUt2GYZqA9i9QT2d7yG_XOhF6hRZl2gHy5Q=s32-c-mo 1x, https://lh3.google.com/u/0/ogw/AF2bZyjzWg4plJaKUt2GYZqA9i9QT2d7yG_XOhF6hRZl2gHy5Q=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""><div class="gb_Q gb_R" aria-hidden="true"><svg class="gb_Ka" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_La" cx="7" cy="7" r="7"></circle><path class="gb_Na" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div aria-hidden="true" style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"><iframe role="presentation" frameborder="0" scrolling="no" name="account" src="./model_files/saved_resource.html" style="height: 100%; width: 100%; color-scheme: light; visibility: hidden;"></iframe></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.pd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.pd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("D`"+b))}};
}catch(e){_._DumpException(e)}
try{
var qd=document.querySelector(".gb_J .gb_B"),rd=document.querySelector("#gb.gb_Sc");qd&&!rd&&_.pd(_.$c,qd,"click");
}catch(e){_._DumpException(e)}
try{
_.Xg=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].fa()&&a.i[b].B())return a.i[b];return null};_.Yg=function(a,b){a.i[b.J()]=b};var Zg=new class extends _.Q{constructor(){var a=_.Ic;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.Xg(this)&&_.Xg(this).J()==a||this.i[a].R(!0))}Pa(a){this.j=a;for(const b in this.i)this.i[b].fa()&&this.i[b].Pa(a)}fc(a){return a in this.i?this.i[a]:null}};_.cd("dd",Zg);
}catch(e){_._DumpException(e)}
try{
_.pi=function(a,b){return _.K(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var qi=document.querySelector(".gb_z .gb_B"),ri=document.querySelector("#gb.gb_Sc");qi&&!ri&&_.pd(_.$c,qi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink toolbar-above-left-pane"><!----> <!--?lit$353632356$--> <colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
        <!--?lit$353632356$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$353632356$--><span class="screenreader-only"><!--?lit$353632356$-->Show command palette <!--?lit$353632356$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$353632356$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$353632356$-->Commands
          </colab-toolbar-button>
          <span class="colab-separator"></span>
    <!--?lit$353632356$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
        <!--?lit$353632356$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$353632356$--><span class="screenreader-only"><!--?lit$353632356$-->Insert code cell below <!--?lit$353632356$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$353632356$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$353632356$-->Code
          </colab-toolbar-button>
          <!--?lit$353632356$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
        <!--?lit$353632356$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$353632356$--><span class="screenreader-only"><!--?lit$353632356$-->Add text cell <!--?lit$353632356$--></span>
      </md-text-button>
      <!--?lit$353632356$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$353632356$-->Text
          </colab-toolbar-button>
        
    <!--?lit$353632356$-->
    <!--?lit$353632356$-->
    <!--?lit$353632356$-->
    <!--?lit$353632356$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$353632356$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$353632356$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$353632356$--><!--?lit$353632356$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$353632356$--> <!--?lit$353632356$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Focus the last run cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Focus the last run cell">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Focus the last run cell"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connected to
Python 3 Google Compute Engine backend
RAM: 1.38 GB/12.67 GB
Disk: 37.13 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
        <!--?lit$353632356$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$353632356$--><span class="screenreader-only"><!--?lit$353632356$-->Connected to
Python 3 Google Compute Engine backend
RAM: 1.38 GB/12.67 GB
Disk: 37.13 GB/107.72 GB <!--?lit$353632356$--></span>
      </md-text-button>
      <!--?lit$353632356$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connected to
Python 3 Google Compute Engine backend
RAM: 1.38 GB/12.67 GB
Disk: 37.13 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Connected to</div><!----><!----><div><!--?lit$353632356$-->Python 3 Google Compute Engine backend</div><!----><!----><div><!--?lit$353632356$-->RAM: 1.38 GB/12.67 GB</div><!----><!----><div><!--?lit$353632356$-->Disk: 37.13 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$353632356$--> <div id="connect-button-resource-display">
        <!--?lit$353632356$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$353632356$-->RAM</div>
      <!--?lit$353632356$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        <!--?lit$353632356$--><colab-usage-sparkline class="disks" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$353632356$-->Disk</div>
      <!--?lit$353632356$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
      </div>
      </colab-toolbar-button>
      <!--?lit$353632356$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$353632356$-->
    <span class="collapsed-options">
      <!--?lit$353632356$--><span class="colab-separator"></span>
      <!--?lit$353632356$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$353632356$--> <md-icon-button class="show-chat-button" id="show-chat-button-toolbar" command="show-chat" data-aria-label="Show Gemini" aria-describedby="show-chat-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show Gemini">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button-toolbar" id="show-chat-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Show Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$353632356$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$353632356$--><colab-left-pane role="complementary" aria-label="left pane" class="colab-left-pane-open"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$353632356$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard" aria-label="Table of contents" aria-pressed="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$353632356$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$353632356$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard" aria-label="Find and replace" aria-pressed="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$353632356$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$353632356$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard" aria-label="Code snippets" aria-pressed="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->code</md-icon>
    </md-icon-button> <!--?lit$353632356$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$353632356$--><md-icon-button toggle="" command="show-variables" data-aria-label="Variables" title="Variables" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard" aria-label="Variables" aria-pressed="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
    </md-icon-button> <!--?lit$353632356$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$353632356$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard" aria-label="Secrets" aria-pressed="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$353632356$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$353632356$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value="" selected=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard selected" aria-label="Files" aria-pressed="true">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="icon icon--selected"><slot name="selected"><slot></slot></slot></span>
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->folder</md-icon>
    </md-icon-button> <!--?lit$353632356$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$353632356$--><md-icon-button command="show-terminal" data-aria-label="Terminal" title="Terminal" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terminal">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->terminal</md-icon>
    </md-icon-button> <!--?lit$353632356$-->
      </div></div>
      </div><colab-resizer class="ew-resize">
          <div class="resizer-contents">
            <div class="colab-left-pane-header layout horizontal noshrink">
              <h3 class="left-pane-content-title">Files</h3>
              <!--?lit$353632356$--><md-icon-button class="colab-left-pane-move" data-aria-label="Move left pane to a tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move left pane to a tab">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface hovered"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>tab</md-icon>
    </md-icon-button> <!--?lit$353632356$--><md-icon-button class="colab-left-pane-close" data-aria-label="Close left pane" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close left pane">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
            </div>
            <div class="left-pane-container"><colab-file-browser class="layout vertical"><colab-file-tree><!----> <!--?lit$353632356$--><colab-agent-promo-banner><template shadowrootmode="open"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <div><!--?lit$353632356$-->Analyze your files with code written by Gemini</div>
      <md-text-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
        <!--?lit$353632356$-->Upload
      </md-text-button></template>
            </colab-agent-promo-banner>
        <div class="file-tree-buttons">
          <label for="file-tree-upload-input">
            <md-icon-button class="colab-icon file-tree-upload-button" title="Upload to session storage" data-aria-label="Upload to session storage" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Upload to session storage">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
              <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload_file</md-icon>
            </md-icon-button>
          </label>
          <input id="file-tree-upload-input" type="file" multiple="">
          <md-icon-button class="file-tree-refresh" title="Refresh" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard ">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>refresh</md-icon>
          </md-icon-button>
          <md-icon-button toggle="" class="mount-drive-button" title="Unmount Drive" data-aria-label="Mount Drive" aria-label-selected="Unmount Drive" style="display: flex;" value="" selected=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard selected" aria-label="Unmount Drive" aria-pressed="true">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="icon icon--selected"><slot name="selected"><slot></slot></slot></span>
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$-->
    <path d="M20,6H12L10,4H4A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H20a2,2,0,0,0,2-2V8A2,2,0,0,0,20,6ZM13.57,9.32,13,8.4l.34-.6h3.11l3.69,6.5H16.38M12.11,17l-.67,1.2h-1L9,15.42,12.72,9l2,3.46h0M19.3,18.2H12.09l.67-1.2,1.15-2h6.64l.34.6Z"></path></svg></md-icon>
            <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$-->
    <path d="M12.72,9l2,3.46h0l-.26.47,2,2h4.1l.34.6L19.45,18l1.69,1.69A2,2,0,0,0,22,18V8a2,2,0,0,0-2-2H12L10,4H5.5l6.4,6.4Zm.66-1.17h3.11l3.69,6.5H16.38l-2.81-5L13,8.4Z"></path>
    <path d="M22.19,22.19,1.81,1.81.4,3.22,2.25,5.07A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H17.17l3.61,3.61Zm-11.73-4L9,15.42l1.3-2.26,2.35,2.36.17.17L12.11,17l-.67,1.2Zm1.63,0,.67-1.2.51-.9,2.1,2.1Z"></path></svg></md-icon>
          </md-icon-button>
          <md-icon-button toggle="" id="hidden-files-toggle" data-aria-label="Show hidden files" aria-label-selected="Hide hidden files" title="Show hidden files" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show hidden files" aria-pressed="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>visibility_off</md-icon>
            <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>visibility</md-icon>
          </md-icon-button>
        </div>
        <div class="parent-link"><div class="file-title-row">
          <!--?lit$353632356$-->
                <div class="file-icon colab-icon" style="margin-left: 0px;"></div>
              
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->folder_open</md-icon>
          <span class="file-tree-name" title="Up one level">
            <!--?lit$353632356$-->..
          </span>
          <input class="file-tree-name-input" value="..">
          <md-icon-button class="file-item-menu" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="More actions for file: .." value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions for file: .." aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div></div>
        <div class="files-root"><colab-file-view filename="content" draggable="true"><!----><!--?lit$353632356$--><!--?--><!--?lit$353632356$-->
        <div class="child-files"><colab-file-view filename="drive" class="collapsed" draggable="true"><!----><!--?lit$353632356$-->
        <div class="file-title-row">
          <!--?lit$353632356$--> <md-icon class="file-icon colab-icon directory-icon" style="margin-left: 0px;" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->folder</md-icon>
          <span class="file-tree-name" title="drive">
            <!--?lit$353632356$-->drive
          </span>
          <input class="file-tree-name-input" value="drive">
          <md-icon-button class="file-item-menu" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="More actions for folder: drive" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions for folder: drive" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div>
      <!--?lit$353632356$-->
        <div class="child-files"></div>
        <div class="overflow-ellipsis" title="Directory is too large to display all files." style="margin-left: 0px;">
          …
        </div>
      <!--?--></colab-file-view><colab-file-view filename="sample_data" class="collapsed" draggable="true"><!----><!--?lit$353632356$-->
        <div class="file-title-row">
          <!--?lit$353632356$--> <md-icon class="file-icon colab-icon directory-icon" style="margin-left: 0px;" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->folder</md-icon>
          <span class="file-tree-name" title="sample_data">
            <!--?lit$353632356$-->sample_data
          </span>
          <input class="file-tree-name-input" value="sample_data">
          <md-icon-button class="file-item-menu" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="More actions for folder: sample_data" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions for folder: sample_data" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div>
      <!--?lit$353632356$-->
        <div class="child-files"></div>
        <div class="overflow-ellipsis" title="Directory is too large to display all files." style="margin-left: 0px;">
          …
        </div>
      <!--?--></colab-file-view></div>
        <div class="overflow-ellipsis" title="Directory is too large to display all files." style="margin-left: -20px;">
          …
        </div>
      <!--?--></colab-file-view></div>
        <div class="files-drag-to-upload layout horizontal">
          <md-icon class="layout noshrink" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload_file</md-icon>
          <div> <!--?lit$353632356$-->Drop files to upload them to session storage. </div>
        </div>
        <div class="files-uploading"></div>
        <div class="colab-usage-bar-container"><colab-usage-bar aria-describedby="file-browser-disk-display-kernel-tooltip" id="file-browser-disk-display-kernel" class="file-browser-disk-display usage-bar-with-suffix" tabindex="0" style="display: flex;"><template shadowrootmode="open"><!---->
        <div class="header">
          <div><!--?lit$353632356$-->Disk </div>
          <div class="suffix"><!--?lit$353632356$-->70.58 GB available</div>
        </div>
        <!--?lit$353632356$-->
      <div class="progress-container">
        <md-linear-progress class="  " value="0.3447321326026903"><template shadowrootmode="open"><!---->
      <div role="progressbar" aria-valuemin="0" class="progress   " aria-valuemax="1" aria-valuenow="0.3447321326026903"><!--?lit$353632356$-->
      <div class="dots" hidden=""></div>
      <div class="inactive-track" style="transform: scaleX(1);"></div>
      <div class="bar primary-bar" style="transform: scaleX(0.344732);">
        <div class="bar-inner"></div>
      </div>
      <div class="bar secondary-bar">
        <div class="bar-inner"></div>
      </div>
    </div>
    </template></md-linear-progress>
      </div>
    
      </template></colab-usage-bar><colab-tooltip-trigger aria-hidden="true" id="file-browser-disk-display-kernel-tooltip"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Disk: 37.13 GB/107.72 GB</div><!----><!--?--></template></colab-tooltip-trigger></div></colab-file-tree></colab-file-browser></div>
          </div>
        <div class="resizer-thumb"></div></colab-resizer></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$353632356$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$353632356$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-0I49QF0yrQ-d" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$353632356$--><div class="indicator"></div>
      </div>
      <!--?lit$353632356$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-0I49QF0yrQ-d"><!--?lit$353632356$--><!--?lit$353632356$-->Notebook<!--?--></span>
            <!--?lit$353632356$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$353632356$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook" tabindex="-1">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$353632356$-->
              <div class="notebook-content ">
                <!--?lit$353632356$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code icon-scrolling focused" id="cell-Ld2awn1K03mr" role="region" aria-label="Cell 0: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" aria-disabled="true">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->arrow_upward</md-icon>
        <!--?lit$353632356$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Move cell up</div><!----><!----><div><!--?lit$353632356$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->arrow_downward</md-icon>
        <!--?lit$353632356$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Move cell down</div><!----><!----><div><!--?lit$353632356$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$353632356$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-Ld2awn1K03mr" anchor="ai-menu-anchor-Ld2awn1K03mr" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$353632356$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$353632356$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$353632356$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$353632356$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$353632356$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$353632356$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$353632356$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$353632356$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$353632356$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$353632356$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$353632356$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$353632356$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$353632356$-->Explain code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-Ld2awn1K03mr-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-Ld2awn1K03mr" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-Ld2awn1K03mr" id="ai-menu-anchor-Ld2awn1K03mr-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->link</md-icon>
        <!--?lit$353632356$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copy link to cell"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Copy link to cell</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-add-comment-tooltip" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->comment</md-icon>
        <!--?lit$353632356$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Add a comment
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Add a comment</div><!----><!----><div><!--?lit$353632356$-->Ctrl+Alt+M</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->settings</md-icon>
        <!--?lit$353632356$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Open editor settings"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Open editor settings</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->edit</md-icon>
        <!--?lit$353632356$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
        <!--?lit$353632356$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mirror cell in tab"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Mirror cell in tab</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->delete</md-icon>
        <!--?lit$353632356$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Delete cell</div><!----><!----><div><!--?lit$353632356$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$353632356$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale focused">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
5:40 PM (37 minutes ago)
executed in 0.801s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->5:40 PM (37 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 0.801s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="152" data-mode-id="notebook-python" style="height: 257px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/3" style="width: 981px; height: 257px;"><div data-mprt="3" class="overflow-guard" style="width: 981px; height: 257px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 257px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 257px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 257px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 975px; height: 257px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 257px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 975px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:975px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:38px;width:177px;height:19px;"></div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:38px;width:177px;height:19px;"></div></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 257px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 975px; height: 257px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;np</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;pd</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;tensorflow&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;tf</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;tensorflow.keras.models&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;Sequential</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;tensorflow.keras.layers&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;LSTM</span><span class="mtk12">,</span><span class="mtk1">&nbsp;GRU</span><span class="mtk12">,</span><span class="mtk1">&nbsp;Dense</span><span class="mtk12">,</span><span class="mtk1">&nbsp;Dropout</span><span class="mtk12">,</span><span class="mtk1">&nbsp;Bidirectional</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.model_selection&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;train_test_split</span><span class="mtk12">,</span><span class="mtk1">&nbsp;KFold</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.preprocessing&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;StandardScaler</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.metrics&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;</span><span class="mtk12 bracket-highlighting-0">(</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;mean_squared_error</span><span class="mtk12">,</span><span class="mtk1">&nbsp;precision_score</span><span class="mtk12">,</span><span class="mtk1">&nbsp;recall_score</span><span class="mtk12">,</span><span class="mtk1">&nbsp;f1_score</span><span class="mtk12">,</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;confusion_matrix</span><span class="mtk12">,</span><span class="mtk1">&nbsp;classification_report</span><span class="mtk12">,</span><span class="mtk1">&nbsp;roc_auc_score</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;matplotlib.pyplot&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;plt</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;seaborn&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;sns</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 975px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 961px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 961px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="321" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 257px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 257px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 257px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 981px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 981px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 257px;"><div class="minimap-shadow-hidden" style="height: 257px;"></div><canvas width="0" height="321" style="position: absolute; left: 0px; width: 0px; height: 257px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="321" style="position: absolute; left: 0px; width: 0px; height: 257px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1408px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 647.46px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-YtFNI3PCPZby" role="region" aria-label="Cell 1: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
5:44 PM (33 minutes ago)
executed in 267.731s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->5:44 PM (33 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 267.731s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="151" data-mode-id="notebook-python" style="height: 1321px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/4" style="width: 981px; height: 1321px;"><div data-mprt="3" class="overflow-guard" style="width: 981px; height: 1321px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 1321px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 1321px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 1321px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div><div style="position:absolute;top:1083px;width:100%;height:19px;"></div><div style="position:absolute;top:1102px;width:100%;height:19px;"></div><div style="position:absolute;top:1121px;width:100%;height:19px;"></div><div style="position:absolute;top:1140px;width:100%;height:19px;"></div><div style="position:absolute;top:1159px;width:100%;height:19px;"></div><div style="position:absolute;top:1178px;width:100%;height:19px;"></div><div style="position:absolute;top:1197px;width:100%;height:19px;"></div><div style="position:absolute;top:1216px;width:100%;height:19px;"></div><div style="position:absolute;top:1235px;width:100%;height:19px;"></div><div style="position:absolute;top:1254px;width:100%;height:19px;"></div><div style="position:absolute;top:1273px;width:100%;height:19px;"></div><div style="position:absolute;top:1292px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 975px; height: 1321px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1321px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 975px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:975px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div><div style="position:absolute;top:1083px;width:100%;height:19px;"></div><div style="position:absolute;top:1102px;width:100%;height:19px;"></div><div style="position:absolute;top:1121px;width:100%;height:19px;"></div><div style="position:absolute;top:1140px;width:100%;height:19px;"></div><div style="position:absolute;top:1159px;width:100%;height:19px;"></div><div style="position:absolute;top:1178px;width:100%;height:19px;"></div><div style="position:absolute;top:1197px;width:100%;height:19px;"></div><div style="position:absolute;top:1216px;width:100%;height:19px;"></div><div style="position:absolute;top:1235px;width:100%;height:19px;"></div><div style="position:absolute;top:1254px;width:100%;height:19px;"></div><div style="position:absolute;top:1273px;width:100%;height:19px;"></div><div style="position:absolute;top:1292px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 1321px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 975px; height: 1321px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;pd</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;np</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.model_selection&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;train_test_split</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.preprocessing&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;StandardScaler</span><span class="mtk12">,</span><span class="mtk1">&nbsp;LabelEncoder</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;google.colab&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;files</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;io</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Upload&nbsp;the&nbsp;dataset</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">uploaded&nbsp;=&nbsp;files.upload</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Load&nbsp;the&nbsp;dataset</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">uploaded&nbsp;=&nbsp;files.upload</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Upload&nbsp;the&nbsp;file&nbsp;again</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;pd.read_csv</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">io.BytesIO</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk1">uploaded</span><span class="mtk12 bracket-highlighting-2">[</span><span class="mtk14">list</span><span class="mtk12 bracket-highlighting-3">(</span><span class="mtk1">uploaded.keys</span><span class="mtk12 bracket-highlighting-4">(</span><span class="mtk12 bracket-highlighting-4">)</span><span class="mtk12 bracket-highlighting-3">)</span><span class="mtk12 bracket-highlighting-3">[</span><span class="mtk6">0</span><span class="mtk12 bracket-highlighting-3">]</span><span class="mtk12 bracket-highlighting-2">]</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Read&nbsp;dynamically</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Convert&nbsp;categorical&nbsp;variables&nbsp;to&nbsp;numerical&nbsp;(exce</span><span class="mtk8">pt&nbsp;target)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;pd.get_dummies</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk12">,</span><span class="mtk1">&nbsp;columns=</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Vehicle_Type'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Route_Info'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Weather_Conditions'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Road_Conditions'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">df.dtypes</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Check&nbsp;data&nbsp;types</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">df.select_dtypes</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk1">include=</span><span class="mtk12 bracket-highlighting-2">[</span><span class="mtk5">'object'</span><span class="mtk12 bracket-highlighting-2">]</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk1">.head</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Show&nbsp;first&nbsp;few&nbsp;rows&nbsp;of&nbsp;non-numeric&nbsp;columns</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;df.drop</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">columns=</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Make_and_Model'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;✅&nbsp;Remove&nbsp;the&nbsp;column</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;pd.get_dummies</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk12">,</span><span class="mtk1">&nbsp;drop_first=</span><span class="mtk9">True</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;✅&nbsp;Convert&nbsp;categorical&nbsp;data&nbsp;into&nbsp;numerical&nbsp;format</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">df.dtypes</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;✅&nbsp;Should&nbsp;show&nbsp;only&nbsp;numeric&nbsp;data&nbsp;types</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">df.head</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;✅&nbsp;Check&nbsp;if&nbsp;all&nbsp;values&nbsp;are&nbsp;numbers</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.preprocessing&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;StandardScaler</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk1">scaler&nbsp;=&nbsp;StandardScaler</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;df.drop</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">columns=</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Maintenance_Required'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Features</span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk1">y&nbsp;=&nbsp;df</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk5">'Maintenance_Required'</span><span class="mtk12 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Target</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;scaler.fit_transform</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">X.astype</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk14">float</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;✅&nbsp;Convert&nbsp;to&nbsp;float&nbsp;before&nbsp;scaling</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">X.shape</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Should&nbsp;be&nbsp;(samples,&nbsp;features)</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">y.shape</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Should&nbsp;be&nbsp;(samples,)</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Encode&nbsp;the&nbsp;target&nbsp;column&nbsp;'Maintenance_Required'</span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span class="mtk1">label_encoder&nbsp;=&nbsp;LabelEncoder</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span class="mtk1">df</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk5">'Maintenance_Required'</span><span class="mtk12 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;label_encoder.fit_transform</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Maintenance_Required'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Handle&nbsp;missing&nbsp;values</span></span></div><div style="top:874px;height:19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;df.fillna</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk6">0</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:893px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:912px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Separate&nbsp;features&nbsp;and&nbsp;target</span></span></div><div style="top:931px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;df.drop</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">'Maintenance_Required'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;axis=</span><span class="mtk6">1</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:950px;height:19px;" class="view-line"><span><span class="mtk1">y&nbsp;=&nbsp;df</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk5">'Maintenance_Required'</span><span class="mtk12 bracket-highlighting-0">]</span></span></div><div style="top:969px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:988px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Normalize&nbsp;the&nbsp;features</span></span></div><div style="top:1007px;height:19px;" class="view-line"><span><span class="mtk1">scaler&nbsp;=&nbsp;StandardScaler</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:1026px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;scaler.fit_transform</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">X</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:1045px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1064px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Reshape&nbsp;data&nbsp;for&nbsp;LSTM/GRU&nbsp;(samples,&nbsp;timesteps,&nbsp;f</span><span class="mtk8">eatures)</span></span></div><div style="top:1083px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;X.reshape</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk1">X.shape</span><span class="mtk12 bracket-highlighting-2">[</span><span class="mtk6">0</span><span class="mtk12 bracket-highlighting-2">]</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">1</span><span class="mtk12">,</span><span class="mtk1">&nbsp;X.shape</span><span class="mtk12 bracket-highlighting-2">[</span><span class="mtk6">1</span><span class="mtk12 bracket-highlighting-2">]</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:1102px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1121px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Split&nbsp;the&nbsp;data&nbsp;into&nbsp;training&nbsp;and&nbsp;testing&nbsp;sets</span></span></div><div style="top:1140px;height:19px;" class="view-line"><span><span class="mtk1">X_train</span><span class="mtk12">,</span><span class="mtk1">&nbsp;X_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_train</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_test&nbsp;=&nbsp;train_test_split</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">X</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y</span><span class="mtk12">,</span><span class="mtk1">&nbsp;test_size=</span><span class="mtk6">0.2</span><span class="mtk12">,</span><span class="mtk1">&nbsp;random_state=</span><span class="mtk6">42</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:1159px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1178px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;X.reshape</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk1">X.shape</span><span class="mtk12 bracket-highlighting-2">[</span><span class="mtk6">0</span><span class="mtk12 bracket-highlighting-2">]</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">1</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">-1</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;✅&nbsp;Automatically&nbsp;adjusts&nbsp;features&nbsp;dimension</span></span></div><div style="top:1197px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1216px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1235px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1254px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1273px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"Data&nbsp;preprocessing&nbsp;completed&nbsp;successfully!"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:1292px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 961px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 961px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="1651" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 1321px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 1321px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 1321px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 981px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 981px;"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 1321px;"><div class="minimap-shadow-hidden" style="height: 1321px;"></div><canvas width="0" height="1651" style="position: absolute; left: 0px; width: 0px; height: 1321px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="1651" style="position: absolute; left: 0px; width: 0px; height: 1321px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1408px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 647.46px; max-height: 330.25px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 1 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 1000px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./model_files/outputframe.html" class="" style="height: 1000px;"></iframe></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-y4cmvzHi7i6p" role="region" aria-label="Cell 2: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
5:49 PM (29 minutes ago)
executed in 205.968s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->5:49 PM (29 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 205.968s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;LSTM&nbsp;Model</span></span><br><span><span class="mtk1">lstm_model&nbsp;=&nbsp;Sequential</span><span class="mtk12">()</span></span><br><span><span class="mtk1">lstm_model.add</span><span class="mtk12">(</span><span class="mtk1">Bidirectional</span><span class="mtk12">(</span><span class="mtk1">LSTM</span><span class="mtk12">(</span><span class="mtk6">100</span><span class="mtk12">,</span><span class="mtk1">&nbsp;return_sequences=</span><span class="mtk9">True</span><span class="mtk12">),</span><span class="mtk1">&nbsp;input_shape=</span><span class="mtk12">(</span><span class="mtk1">X_train.shape</span><span class="mtk12">[</span><span class="mtk6">1</span><span class="mtk12">],</span><span class="mtk1">&nbsp;X_train.shape</span><span class="mtk12">[</span><span class="mtk6">2</span><span class="mtk12">])))</span></span><br><span><span class="mtk1">lstm_model.add</span><span class="mtk12">(</span><span class="mtk1">Dropout</span><span class="mtk12">(</span><span class="mtk6">0.3</span><span class="mtk12">))</span></span><br><span><span class="mtk1">lstm_model.add</span><span class="mtk12">(</span><span class="mtk1">Bidirectional</span><span class="mtk12">(</span><span class="mtk1">LSTM</span><span class="mtk12">(</span><span class="mtk6">50</span><span class="mtk12">)))</span></span><br><span><span class="mtk1">lstm_model.add</span><span class="mtk12">(</span><span class="mtk1">Dropout</span><span class="mtk12">(</span><span class="mtk6">0.3</span><span class="mtk12">))</span></span><br><span><span class="mtk1">lstm_model.add</span><span class="mtk12">(</span><span class="mtk1">Dense</span><span class="mtk12">(</span><span class="mtk6">1</span><span class="mtk12">,</span><span class="mtk1">&nbsp;activation=</span><span class="mtk5">'sigmoid'</span><span class="mtk12">))</span></span><br><span><span></span></span><br><span><span class="mtk1">lstm_model.</span><span class="mtk15">compile</span><span class="mtk12">(</span><span class="mtk1">loss=</span><span class="mtk5">'binary_crossentropy'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;optimizer=</span><span class="mtk5">'adam'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;metrics=</span><span class="mtk12">[</span><span class="mtk5">'accuracy'</span><span class="mtk12">])</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Train&nbsp;the&nbsp;LSTM&nbsp;model</span></span><br><span><span class="mtk1">history_lstm&nbsp;=&nbsp;lstm_model.fit</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;X_train</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_train</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;epochs=</span><span class="mtk6">10</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;batch_size=</span><span class="mtk6">64</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;validation_data=</span><span class="mtk12">(</span><span class="mtk1">X_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_test</span><span class="mtk12">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;verbose=</span><span class="mtk6">1</span></span><br><span><span class="mtk12">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-2973 output_text"><pre>Epoch 1/10
<span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">26s</span><span> 18ms/step - accuracy: 0.8886 - loss: 0.2388 - val_accuracy: 0.9980 - val_loss: 0.0063
Epoch 2/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">18s</span><span> 16ms/step - accuracy: 0.9994 - loss: 0.0025 - val_accuracy: 0.9991 - val_loss: 0.0042
Epoch 3/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">22s</span><span> 17ms/step - accuracy: 0.9996 - loss: 0.0018 - val_accuracy: 0.9998 - val_loss: 0.0016
Epoch 4/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">19s</span><span> 16ms/step - accuracy: 0.9997 - loss: 8.7745e-04 - val_accuracy: 0.9997 - val_loss: 0.0019
Epoch 5/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">21s</span><span> 16ms/step - accuracy: 0.9996 - loss: 9.7152e-04 - val_accuracy: 0.9998 - val_loss: 0.0021
Epoch 6/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">20s</span><span> 16ms/step - accuracy: 0.9997 - loss: 8.4976e-04 - val_accuracy: 0.9997 - val_loss: 0.0020
Epoch 7/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">18s</span><span> 16ms/step - accuracy: 0.9999 - loss: 5.9784e-04 - val_accuracy: 0.9998 - val_loss: 0.0020
Epoch 8/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">21s</span><span> 16ms/step - accuracy: 0.9997 - loss: 5.5885e-04 - val_accuracy: 0.9997 - val_loss: 0.0024
Epoch 9/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">18s</span><span> 15ms/step - accuracy: 0.9998 - loss: 5.3552e-04 - val_accuracy: 0.9996 - val_loss: 0.0025
Epoch 10/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">23s</span><span> 17ms/step - accuracy: 0.9998 - loss: 3.7467e-04 - val_accuracy: 0.9998 - val_loss: 0.0021
</span></pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-kINu8DfTLliy" role="region" aria-label="Cell 3: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
5:54 PM (24 minutes ago)
executed in 254.341s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->5:54 PM (24 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 254.341s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;GRU&nbsp;Model</span></span><br><span><span class="mtk1">gru_model&nbsp;=&nbsp;Sequential</span><span class="mtk12">()</span></span><br><span><span class="mtk1">gru_model.add</span><span class="mtk12">(</span><span class="mtk1">Bidirectional</span><span class="mtk12">(</span><span class="mtk1">GRU</span><span class="mtk12">(</span><span class="mtk6">100</span><span class="mtk12">,</span><span class="mtk1">&nbsp;return_sequences=</span><span class="mtk9">True</span><span class="mtk12">),</span><span class="mtk1">&nbsp;input_shape=</span><span class="mtk12">(</span><span class="mtk1">X_train.shape</span><span class="mtk12">[</span><span class="mtk6">1</span><span class="mtk12">],</span><span class="mtk1">&nbsp;X_train.shape</span><span class="mtk12">[</span><span class="mtk6">2</span><span class="mtk12">])))</span></span><br><span><span class="mtk1">gru_model.add</span><span class="mtk12">(</span><span class="mtk1">Dropout</span><span class="mtk12">(</span><span class="mtk6">0.3</span><span class="mtk12">))</span></span><br><span><span class="mtk1">gru_model.add</span><span class="mtk12">(</span><span class="mtk1">Bidirectional</span><span class="mtk12">(</span><span class="mtk1">GRU</span><span class="mtk12">(</span><span class="mtk6">50</span><span class="mtk12">)))</span></span><br><span><span class="mtk1">gru_model.add</span><span class="mtk12">(</span><span class="mtk1">Dropout</span><span class="mtk12">(</span><span class="mtk6">0.3</span><span class="mtk12">))</span></span><br><span><span class="mtk1">gru_model.add</span><span class="mtk12">(</span><span class="mtk1">Dense</span><span class="mtk12">(</span><span class="mtk6">1</span><span class="mtk12">,</span><span class="mtk1">&nbsp;activation=</span><span class="mtk5">'sigmoid'</span><span class="mtk12">))</span></span><br><span><span></span></span><br><span><span class="mtk1">gru_model.</span><span class="mtk15">compile</span><span class="mtk12">(</span><span class="mtk1">loss=</span><span class="mtk5">'binary_crossentropy'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;optimizer=</span><span class="mtk5">'adam'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;metrics=</span><span class="mtk12">[</span><span class="mtk5">'accuracy'</span><span class="mtk12">])</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Train&nbsp;the&nbsp;GRU&nbsp;model</span></span><br><span><span class="mtk1">history_gru&nbsp;=&nbsp;gru_model.fit</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;X_train</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_train</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;epochs=</span><span class="mtk6">10</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;batch_size=</span><span class="mtk6">64</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;validation_data=</span><span class="mtk12">(</span><span class="mtk1">X_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_test</span><span class="mtk12">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;verbose=</span><span class="mtk6">1</span></span><br><span><span class="mtk12">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 3 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-2859 output_text"><pre>Epoch 1/10
<span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">25s</span><span> 17ms/step - accuracy: 0.8877 - loss: 0.2241 - val_accuracy: 0.9994 - val_loss: 0.0044
Epoch 2/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">18s</span><span> 15ms/step - accuracy: 0.9994 - loss: 0.0033 - val_accuracy: 0.9988 - val_loss: 0.0047
Epoch 3/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">22s</span><span> 17ms/step - accuracy: 0.9992 - loss: 0.0030 - val_accuracy: 0.9997 - val_loss: 0.0019
Epoch 4/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">18s</span><span> 15ms/step - accuracy: 0.9996 - loss: 0.0017 - val_accuracy: 0.9998 - val_loss: 0.0016
Epoch 5/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">20s</span><span> 15ms/step - accuracy: 0.9996 - loss: 0.0010 - val_accuracy: 0.9997 - val_loss: 0.0019
Epoch 6/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">21s</span><span> 15ms/step - accuracy: 0.9996 - loss: 0.0013 - val_accuracy: 0.9998 - val_loss: 0.0015
Epoch 7/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">20s</span><span> 15ms/step - accuracy: 0.9998 - loss: 4.7163e-04 - val_accuracy: 0.9998 - val_loss: 0.0018
Epoch 8/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">19s</span><span> 17ms/step - accuracy: 0.9999 - loss: 3.6067e-04 - val_accuracy: 0.9996 - val_loss: 0.0029
Epoch 9/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">19s</span><span> 15ms/step - accuracy: 0.9998 - loss: 7.8863e-04 - val_accuracy: 0.9998 - val_loss: 0.0021
Epoch 10/10
</span><span style="font-weight: bold;">1150/1150</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">22s</span><span> 17ms/step - accuracy: 0.9998 - loss: 5.5479e-04 - val_accuracy: 0.9997 - val_loss: 0.0021
</span></pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-rSuJw4U16B1Y" role="region" aria-label="Cell 4: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
5:54 PM (24 minutes ago)
executed in 5.234s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->5:54 PM (24 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 5.234s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;Evaluate&nbsp;LSTM&nbsp;Model</span></span><br><span><span class="mtk1">lstm_predictions&nbsp;=&nbsp;lstm_model.predict</span><span class="mtk12">(</span><span class="mtk1">X_test</span><span class="mtk12">)</span></span><br><span><span class="mtk1">lstm_predictions&nbsp;=&nbsp;</span><span class="mtk12">(</span><span class="mtk1">lstm_predictions&nbsp;&gt;&nbsp;</span><span class="mtk6">0.5</span><span class="mtk12">)</span><span class="mtk1">.astype</span><span class="mtk12">(</span><span class="mtk14">int</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Evaluate&nbsp;GRU&nbsp;Model</span></span><br><span><span class="mtk1">gru_predictions&nbsp;=&nbsp;gru_model.predict</span><span class="mtk12">(</span><span class="mtk1">X_test</span><span class="mtk12">)</span></span><br><span><span class="mtk1">gru_predictions&nbsp;=&nbsp;</span><span class="mtk12">(</span><span class="mtk1">gru_predictions&nbsp;&gt;&nbsp;</span><span class="mtk6">0.5</span><span class="mtk12">)</span><span class="mtk1">.astype</span><span class="mtk12">(</span><span class="mtk14">int</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Metrics&nbsp;for&nbsp;LSTM</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"LSTM&nbsp;Model&nbsp;Evaluation:"</span><span class="mtk12">)</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Confusion&nbsp;Matrix:\n"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;confusion_matrix</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;lstm_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Classification&nbsp;Report:\n"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;classification_report</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;lstm_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Precision:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;precision_score</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;lstm_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Recall:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;recall_score</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;lstm_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"F1-Score:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;f1_score</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;lstm_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"ROC-AUC&nbsp;Score:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;roc_auc_score</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;lstm_predictions</span><span class="mtk12">))</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Metrics&nbsp;for&nbsp;GRU</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"\nGRU&nbsp;Model&nbsp;Evaluation:"</span><span class="mtk12">)</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Confusion&nbsp;Matrix:\n"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;confusion_matrix</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;gru_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Classification&nbsp;Report:\n"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;classification_report</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;gru_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Precision:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;precision_score</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;gru_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Recall:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;recall_score</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;gru_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"F1-Score:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;f1_score</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;gru_predictions</span><span class="mtk12">))</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"ROC-AUC&nbsp;Score:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;roc_auc_score</span><span class="mtk12">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;gru_predictions</span><span class="mtk12">))</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 4 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-66 output_text"><pre><span style="font-weight: bold;">575/575</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">2s</span><span> 3ms/step
</span><span style="font-weight: bold;">575/575</span><span> </span><span style="color: var(--ansi-green);">━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="font-weight: bold;">2s</span><span> 3ms/step
LSTM Model Evaluation:
Confusion Matrix:
 [[ 4311     0]
 [    4 14085]]
Classification Report:
               precision    recall  f1-score   support

           0       1.00      1.00      1.00      4311
           1       1.00      1.00      1.00     14089

    accuracy                           1.00     18400
   macro avg       1.00      1.00      1.00     18400
weighted avg       1.00      1.00      1.00     18400

Precision: 1.0
Recall: 0.9997160905671091
F1-Score: 0.999858025129552
ROC-AUC Score: 0.9998580452835546

GRU Model Evaluation:
Confusion Matrix:
 [[ 4310     1]
 [    4 14085]]
Classification Report:
               precision    recall  f1-score   support

           0       1.00      1.00      1.00      4311
           1       1.00      1.00      1.00     14089

    accuracy                           1.00     18400
   macro avg       1.00      1.00      1.00     18400
weighted avg       1.00      1.00      1.00     18400

Precision: 0.9999290075252023
Recall: 0.9997160905671091
F1-Score: 0.9998225377107365
ROC-AUC Score: 0.9997420629128749
</span></pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-4tVwmwxsBYRi" role="region" aria-label="Cell 5: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale hovered">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
6:00 PM (18 minutes ago)
executed in 349.974s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->6:00 PM (18 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 349.974s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;np</span></span><br><span><span class="mtk18">import</span><span class="mtk1">&nbsp;tensorflow&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;tf</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;tensorflow.keras.models&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;Sequential</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;tensorflow.keras.layers&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;Dense</span><span class="mtk12">,</span><span class="mtk1">&nbsp;Dropout</span><span class="mtk12">,</span><span class="mtk1">&nbsp;LSTM</span><span class="mtk12">,</span><span class="mtk1">&nbsp;GRU</span><span class="mtk12">,</span><span class="mtk1">&nbsp;Bidirectional</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;tensorflow.keras.callbacks&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;EarlyStopping</span><span class="mtk12">,</span><span class="mtk1">&nbsp;ReduceLROnPlateau</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.model_selection&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;KFold</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Callbacks&nbsp;for&nbsp;efficient&nbsp;training</span></span><br><span><span class="mtk1">early_stopping&nbsp;=&nbsp;EarlyStopping</span><span class="mtk12">(</span><span class="mtk1">monitor=</span><span class="mtk5">'val_loss'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;patience=</span><span class="mtk6">2</span><span class="mtk12">,</span><span class="mtk1">&nbsp;min_delta=</span><span class="mtk6">0.001</span><span class="mtk12">,</span><span class="mtk1">&nbsp;restore_best_weights=</span><span class="mtk9">True</span><span class="mtk12">)</span></span><br><span><span class="mtk1">reduce_lr&nbsp;=&nbsp;ReduceLROnPlateau</span><span class="mtk12">(</span><span class="mtk1">monitor=</span><span class="mtk5">'val_loss'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;factor=</span><span class="mtk6">0.5</span><span class="mtk12">,</span><span class="mtk1">&nbsp;patience=</span><span class="mtk6">1</span><span class="mtk12">,</span><span class="mtk1">&nbsp;min_delta=</span><span class="mtk6">0.001</span><span class="mtk12">,</span><span class="mtk1">&nbsp;verbose=</span><span class="mtk6">0</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;K-Fold&nbsp;Cross-Validation</span></span><br><span><span class="mtk1">kfold&nbsp;=&nbsp;KFold</span><span class="mtk12">(</span><span class="mtk1">n_splits=</span><span class="mtk6">5</span><span class="mtk12">,</span><span class="mtk1">&nbsp;shuffle=</span><span class="mtk9">True</span><span class="mtk12">,</span><span class="mtk1">&nbsp;random_state=</span><span class="mtk6">42</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">build_model</span><span class="mtk1">(</span><span class="mtk4">cell_type</span><span class="mtk1">=</span><span class="mtk5">'LSTM'</span><span class="mtk1">)</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">"""&nbsp;Builds&nbsp;an&nbsp;optimized&nbsp;LSTM&nbsp;or&nbsp;GRU&nbsp;model.&nbsp;"""</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;model&nbsp;=&nbsp;Sequential</span><span class="mtk12">([</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bidirectional</span><span class="mtk12">(</span><span class="mtk1">LSTM</span><span class="mtk12">(</span><span class="mtk6">32</span><span class="mtk12">,</span><span class="mtk1">&nbsp;return_sequences=</span><span class="mtk9">True</span><span class="mtk12">)</span><span class="mtk1">&nbsp;</span><span class="mtk18">if</span><span class="mtk1">&nbsp;cell_type&nbsp;==&nbsp;</span><span class="mtk5">'LSTM'</span><span class="mtk1">&nbsp;</span><span class="mtk18">else</span><span class="mtk1">&nbsp;GRU</span><span class="mtk12">(</span><span class="mtk6">32</span><span class="mtk12">,</span><span class="mtk1">&nbsp;return_sequences=</span><span class="mtk9">True</span><span class="mtk12">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input_shape=</span><span class="mtk12">(</span><span class="mtk1">X.shape</span><span class="mtk12">[</span><span class="mtk6">1</span><span class="mtk12">],</span><span class="mtk1">&nbsp;X.shape</span><span class="mtk12">[</span><span class="mtk6">2</span><span class="mtk12">])),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dropout</span><span class="mtk12">(</span><span class="mtk6">0.3</span><span class="mtk12">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bidirectional</span><span class="mtk12">(</span><span class="mtk1">LSTM</span><span class="mtk12">(</span><span class="mtk6">16</span><span class="mtk12">)</span><span class="mtk1">&nbsp;</span><span class="mtk18">if</span><span class="mtk1">&nbsp;cell_type&nbsp;==&nbsp;</span><span class="mtk5">'LSTM'</span><span class="mtk1">&nbsp;</span><span class="mtk18">else</span><span class="mtk1">&nbsp;GRU</span><span class="mtk12">(</span><span class="mtk6">16</span><span class="mtk12">)),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dropout</span><span class="mtk12">(</span><span class="mtk6">0.3</span><span class="mtk12">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dense</span><span class="mtk12">(</span><span class="mtk6">1</span><span class="mtk12">,</span><span class="mtk1">&nbsp;activation=</span><span class="mtk5">'sigmoid'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">])</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;model.</span><span class="mtk15">compile</span><span class="mtk12">(</span><span class="mtk1">loss=</span><span class="mtk5">'binary_crossentropy'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;optimizer=</span><span class="mtk5">'adam'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;metrics=</span><span class="mtk12">[</span><span class="mtk5">'accuracy'</span><span class="mtk12">])</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">return</span><span class="mtk1">&nbsp;model</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Function&nbsp;to&nbsp;Train&nbsp;and&nbsp;Evaluate&nbsp;using&nbsp;K-Fold</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">train_and_evaluate</span><span class="mtk1">(</span><span class="mtk4">cell_type</span><span class="mtk1">=</span><span class="mtk5">'LSTM'</span><span class="mtk1">)</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;scores&nbsp;=&nbsp;</span><span class="mtk12">[]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">with</span><span class="mtk1">&nbsp;tf.device</span><span class="mtk12">(</span><span class="mtk5">'/GPU:0'</span><span class="mtk12">):</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Use&nbsp;GPU&nbsp;if&nbsp;available</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">for</span><span class="mtk1">&nbsp;train_idx</span><span class="mtk12">,</span><span class="mtk1">&nbsp;val_idx&nbsp;</span><span class="mtk17">in</span><span class="mtk1">&nbsp;kfold.split</span><span class="mtk12">(</span><span class="mtk1">X</span><span class="mtk12">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X_train_fold</span><span class="mtk12">,</span><span class="mtk1">&nbsp;X_val_fold&nbsp;=&nbsp;X</span><span class="mtk12">[</span><span class="mtk1">train_idx</span><span class="mtk12">],</span><span class="mtk1">&nbsp;X</span><span class="mtk12">[</span><span class="mtk1">val_idx</span><span class="mtk12">]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y_train_fold</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_val_fold&nbsp;=&nbsp;y.iloc</span><span class="mtk12">[</span><span class="mtk1">train_idx</span><span class="mtk12">],</span><span class="mtk1">&nbsp;y.iloc</span><span class="mtk12">[</span><span class="mtk1">val_idx</span><span class="mtk12">]</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model&nbsp;=&nbsp;build_model</span><span class="mtk12">(</span><span class="mtk1">cell_type</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model.fit</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X_train_fold</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_train_fold</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;epochs=</span><span class="mtk6">10</span><span class="mtk12">,</span><span class="mtk1">&nbsp;batch_size=</span><span class="mtk6">64</span><span class="mtk12">,</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Fewer&nbsp;epochs,&nbsp;larger&nbsp;batch&nbsp;size</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;validation_data=</span><span class="mtk12">(</span><span class="mtk1">X_val_fold</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_val_fold</span><span class="mtk12">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;callbacks=</span><span class="mtk12">[</span><span class="mtk1">early_stopping</span><span class="mtk12">,</span><span class="mtk1">&nbsp;reduce_lr</span><span class="mtk12">],</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;verbose=</span><span class="mtk6">0</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scores.append</span><span class="mtk12">(</span><span class="mtk1">model.evaluate</span><span class="mtk12">(</span><span class="mtk1">X_val_fold</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_val_fold</span><span class="mtk12">,</span><span class="mtk1">&nbsp;verbose=</span><span class="mtk6">0</span><span class="mtk12">)[</span><span class="mtk6">1</span><span class="mtk12">])</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">return</span><span class="mtk1">&nbsp;np.mean</span><span class="mtk12">(</span><span class="mtk1">scores</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Run&nbsp;Optimized&nbsp;Training</span></span><br><span><span class="mtk1">lstm_acc&nbsp;=&nbsp;train_and_evaluate</span><span class="mtk12">(</span><span class="mtk5">'LSTM'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">gru_acc&nbsp;=&nbsp;train_and_evaluate</span><span class="mtk12">(</span><span class="mtk5">'GRU'</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"LSTM&nbsp;Accuracy:&nbsp;</span><span class="mtk12">{</span><span class="mtk1">lstm_acc</span><span class="mtk6">:.4f</span><span class="mtk12">}</span><span class="mtk5">"</span><span class="mtk12">)</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"GRU&nbsp;Accuracy:&nbsp;</span><span class="mtk12">{</span><span class="mtk1">gru_acc</span><span class="mtk6">:.4f</span><span class="mtk12">}</span><span class="mtk5">"</span><span class="mtk12">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 5 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>/usr/local/lib/python3.11/dist-packages/keras/src/layers/rnn/bidirectional.py:107: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(**kwargs)
</pre></div><div class="stream output-id-2 output_text"><pre>LSTM Accuracy: 0.9998
GRU Accuracy: 0.9997
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-le01NDg5ELrf" role="region" aria-label="Cell 6: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
6:00 PM (18 minutes ago)
executed in 0.091s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->6:00 PM (18 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 0.091s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;Save&nbsp;the&nbsp;best&nbsp;model&nbsp;based&nbsp;on&nbsp;validation&nbsp;accuracy</span></span><br><span><span class="mtk18">if</span><span class="mtk1">&nbsp;lstm_acc&nbsp;&gt;&nbsp;gru_acc</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;best_model&nbsp;=&nbsp;build_model</span><span class="mtk12">(</span><span class="mtk5">'LSTM'</span><span class="mtk12">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Recreate&nbsp;the&nbsp;best&nbsp;model</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;best_model.save</span><span class="mtk12">(</span><span class="mtk5">'best_predictive_maintenance_model.h5'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"LSTM&nbsp;Model&nbsp;Saved&nbsp;as&nbsp;Best&nbsp;Model."</span><span class="mtk12">)</span></span><br><span><span class="mtk18">else</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;best_model&nbsp;=&nbsp;build_model</span><span class="mtk12">(</span><span class="mtk5">'GRU'</span><span class="mtk12">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Recreate&nbsp;the&nbsp;best&nbsp;model</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;best_model.save</span><span class="mtk12">(</span><span class="mtk5">'best_predictive_maintenance_model.h5'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"GRU&nbsp;Model&nbsp;Saved&nbsp;as&nbsp;Best&nbsp;Model."</span><span class="mtk12">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 6 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>WARNING:absl:You are saving your model as an HDF5 file via `model.save()` or `keras.saving.save_model(model)`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')` or `keras.saving.save_model(model, 'my_model.keras')`. 
</pre></div><div class="stream output-id-2 output_text"><pre>LSTM Model Saved as Best Model.
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-PViK-JfyETn3" role="region" aria-label="Cell 7: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
6:00 PM (18 minutes ago)
executed in 0.663s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->6:00 PM (18 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 0.663s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;Plot&nbsp;training&nbsp;and&nbsp;validation&nbsp;accuracy&nbsp;for&nbsp;LSTM</span></span><br><span><span class="mtk1">plt.plot</span><span class="mtk12">(</span><span class="mtk1">history_lstm.history</span><span class="mtk12">[</span><span class="mtk5">'accuracy'</span><span class="mtk12">],</span><span class="mtk1">&nbsp;label=</span><span class="mtk5">'LSTM&nbsp;Training&nbsp;Accuracy'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.plot</span><span class="mtk12">(</span><span class="mtk1">history_lstm.history</span><span class="mtk12">[</span><span class="mtk5">'val_accuracy'</span><span class="mtk12">],</span><span class="mtk1">&nbsp;label=</span><span class="mtk5">'LSTM&nbsp;Validation&nbsp;Accuracy'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.title</span><span class="mtk12">(</span><span class="mtk5">'LSTM&nbsp;Model&nbsp;Accuracy'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.xlabel</span><span class="mtk12">(</span><span class="mtk5">'Epochs'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.ylabel</span><span class="mtk12">(</span><span class="mtk5">'Accuracy'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.legend</span><span class="mtk12">()</span></span><br><span><span class="mtk1">plt.show</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Plot&nbsp;training&nbsp;and&nbsp;validation&nbsp;accuracy&nbsp;for&nbsp;GRU</span></span><br><span><span class="mtk1">plt.plot</span><span class="mtk12">(</span><span class="mtk1">history_gru.history</span><span class="mtk12">[</span><span class="mtk5">'accuracy'</span><span class="mtk12">],</span><span class="mtk1">&nbsp;label=</span><span class="mtk5">'GRU&nbsp;Training&nbsp;Accuracy'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.plot</span><span class="mtk12">(</span><span class="mtk1">history_gru.history</span><span class="mtk12">[</span><span class="mtk5">'val_accuracy'</span><span class="mtk12">],</span><span class="mtk1">&nbsp;label=</span><span class="mtk5">'GRU&nbsp;Validation&nbsp;Accuracy'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.title</span><span class="mtk12">(</span><span class="mtk5">'GRU&nbsp;Model&nbsp;Accuracy'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.xlabel</span><span class="mtk12">(</span><span class="mtk5">'Epochs'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.ylabel</span><span class="mtk12">(</span><span class="mtk5">'Accuracy'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.legend</span><span class="mtk12">()</span></span><br><span><span class="mtk1">plt.show</span><span class="mtk12">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 7 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 927px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./model_files/outputframe(1).html" class="" style="height: 927px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-Vv9celKpEaO5" role="region" aria-label="Cell 8: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
6:00 PM (18 minutes ago)
executed in 29.747s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->6:00 PM (18 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 29.747s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;sqlite3</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;datetime&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;datetime</span><span class="mtk12">,</span><span class="mtk1">&nbsp;timedelta</span></span><br><span><span class="mtk18">import</span><span class="mtk1">&nbsp;time</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Initialize&nbsp;database</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">init_db</span><span class="mtk1">()</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;conn&nbsp;=&nbsp;sqlite3.connect</span><span class="mtk12">(</span><span class="mtk5">':memory:'</span><span class="mtk12">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Using&nbsp;in-memory&nbsp;database&nbsp;for&nbsp;Colab</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor&nbsp;=&nbsp;conn.cursor</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Create&nbsp;tables</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span><span class="mtk5">'''</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;CREATE&nbsp;TABLE&nbsp;assets&nbsp;(</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id&nbsp;INTEGER&nbsp;PRIMARY&nbsp;KEY&nbsp;AUTOINCREMENT,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;TEXT&nbsp;NOT&nbsp;NULL,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_maintenance_date&nbsp;DATE,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maintenance_interval_days&nbsp;INTEGER&nbsp;NOT&nbsp;NULL</span><span class="mtk5">,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;status&nbsp;TEXT&nbsp;NOT&nbsp;NULL</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;)</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;'''</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span><span class="mtk5">'''</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;CREATE&nbsp;TABLE&nbsp;alerts&nbsp;(</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id&nbsp;INTEGER&nbsp;PRIMARY&nbsp;KEY&nbsp;AUTOINCREMENT,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;asset_id&nbsp;INTEGER&nbsp;NOT&nbsp;NULL,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message&nbsp;TEXT&nbsp;NOT&nbsp;NULL,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity&nbsp;TEXT&nbsp;NOT&nbsp;NULL,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;created_at&nbsp;TIMESTAMP&nbsp;DEFAULT&nbsp;CURRENT_TIMES</span><span class="mtk5">TAMP,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resolved&nbsp;BOOLEAN&nbsp;DEFAULT&nbsp;0,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN&nbsp;KEY&nbsp;(asset_id)&nbsp;REFERENCES&nbsp;assets&nbsp;(</span><span class="mtk5">id)</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;)</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;'''</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Add&nbsp;some&nbsp;sample&nbsp;assets</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;today&nbsp;=&nbsp;datetime.now</span><span class="mtk12">()</span><span class="mtk1">.date</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.executemany</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'INSERT&nbsp;INTO&nbsp;assets&nbsp;(name,&nbsp;next_maintenance_date,&nbsp;</span><span class="mtk5">maintenance_interval_days,&nbsp;status)&nbsp;VALUES&nbsp;(?,&nbsp;?,&nbsp;?</span><span class="mtk5">,&nbsp;?)'</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">[</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">(</span><span class="mtk5">'HVAC&nbsp;System'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;today&nbsp;+&nbsp;timedelta</span><span class="mtk12">(</span><span class="mtk1">days=</span><span class="mtk6">2</span><span class="mtk12">),</span><span class="mtk1">&nbsp;</span><span class="mtk6">30</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'operational'</span><span class="mtk12">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">(</span><span class="mtk5">'Generator'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;today&nbsp;-&nbsp;timedelta</span><span class="mtk12">(</span><span class="mtk1">days=</span><span class="mtk6">5</span><span class="mtk12">),</span><span class="mtk1">&nbsp;</span><span class="mtk6">90</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'operational'</span><span class="mtk12">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">(</span><span class="mtk5">'Elevator'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;today&nbsp;+&nbsp;timedelta</span><span class="mtk12">(</span><span class="mtk1">days=</span><span class="mtk6">30</span><span class="mtk12">),</span><span class="mtk1">&nbsp;</span><span class="mtk6">180</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'operational'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;conn.commit</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">return</span><span class="mtk1">&nbsp;conn</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Alerting&nbsp;and&nbsp;maintenance&nbsp;check&nbsp;function</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">check_maintenance</span><span class="mtk1">(</span><span class="mtk4">conn</span><span class="mtk1">)</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor&nbsp;=&nbsp;conn.cursor</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;today&nbsp;=&nbsp;datetime.now</span><span class="mtk12">()</span><span class="mtk1">.date</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"\nRunning&nbsp;maintenance&nbsp;check..."</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Check&nbsp;for&nbsp;overdue&nbsp;maintenance</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'SELECT&nbsp;*&nbsp;FROM&nbsp;assets&nbsp;WHERE&nbsp;next_maintenance_date&nbsp;</span><span class="mtk5">&lt;&nbsp;?&nbsp;AND&nbsp;status&nbsp;=&nbsp;"operational"'</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">(</span><span class="mtk1">today</span><span class="mtk12">,)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;overdue_assets&nbsp;=&nbsp;cursor.fetchall</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">for</span><span class="mtk1">&nbsp;asset&nbsp;</span><span class="mtk17">in</span><span class="mtk1">&nbsp;overdue_assets</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"ALERT:&nbsp;Maintenance&nbsp;overdue&nbsp;for&nbsp;</span><span class="mtk12">{</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">1</span><span class="mtk12">]}</span><span class="mtk5">&nbsp;(was&nbsp;due&nbsp;on&nbsp;</span><span class="mtk12">{</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">2</span><span class="mtk12">]}</span><span class="mtk5">)"</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'INSERT&nbsp;INTO&nbsp;alerts&nbsp;(asset_id,&nbsp;message,&nbsp;severity)&nbsp;</span><span class="mtk5">VALUES&nbsp;(?,&nbsp;?,&nbsp;?)'</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">(</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">0</span><span class="mtk12">],</span><span class="mtk1">&nbsp;</span><span class="mtk9">f</span><span class="mtk5">'Maintenance&nbsp;overdue&nbsp;for&nbsp;</span><span class="mtk12">{</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">1</span><span class="mtk12">]}</span><span class="mtk5">'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'high'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Check&nbsp;for&nbsp;upcoming&nbsp;maintenance&nbsp;(within&nbsp;7&nbsp;days)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;seven_days_later&nbsp;=&nbsp;today&nbsp;+&nbsp;timedelta</span><span class="mtk12">(</span><span class="mtk1">days=</span><span class="mtk6">7</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'SELECT&nbsp;*&nbsp;FROM&nbsp;assets&nbsp;WHERE&nbsp;next_maintenance_date&nbsp;</span><span class="mtk5">BETWEEN&nbsp;?&nbsp;AND&nbsp;?&nbsp;AND&nbsp;status&nbsp;=&nbsp;"operational"'</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">(</span><span class="mtk1">today</span><span class="mtk12">,</span><span class="mtk1">&nbsp;seven_days_later</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;upcoming_assets&nbsp;=&nbsp;cursor.fetchall</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">for</span><span class="mtk1">&nbsp;asset&nbsp;</span><span class="mtk17">in</span><span class="mtk1">&nbsp;upcoming_assets</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"INFO:&nbsp;Maintenance&nbsp;coming&nbsp;up&nbsp;for&nbsp;</span><span class="mtk12">{</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">1</span><span class="mtk12">]}</span><span class="mtk5">&nbsp;on&nbsp;</span><span class="mtk12">{</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">2</span><span class="mtk12">]}</span><span class="mtk5">"</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'INSERT&nbsp;INTO&nbsp;alerts&nbsp;(asset_id,&nbsp;message,&nbsp;severity)&nbsp;</span><span class="mtk5">VALUES&nbsp;(?,&nbsp;?,&nbsp;?)'</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">(</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">0</span><span class="mtk12">],</span><span class="mtk1">&nbsp;</span><span class="mtk9">f</span><span class="mtk5">'Maintenance&nbsp;scheduled&nbsp;for&nbsp;</span><span class="mtk12">{</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">1</span><span class="mtk12">]}</span><span class="mtk5">&nbsp;on&nbsp;</span><span class="mtk12">{</span><span class="mtk1">asset</span><span class="mtk12">[</span><span class="mtk6">2</span><span class="mtk12">]}</span><span class="mtk5">'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'medium'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;conn.commit</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Display&nbsp;current&nbsp;alerts</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span><span class="mtk5">'SELECT&nbsp;*&nbsp;FROM&nbsp;alerts&nbsp;WHERE&nbsp;resolved&nbsp;=&nbsp;0&nbsp;ORDER&nbsp;BY&nbsp;</span><span class="mtk5">created_at&nbsp;DESC'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;active_alerts&nbsp;=&nbsp;cursor.fetchall</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">if</span><span class="mtk1">&nbsp;active_alerts</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"\nActive&nbsp;Alerts:"</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">for</span><span class="mtk1">&nbsp;alert&nbsp;</span><span class="mtk17">in</span><span class="mtk1">&nbsp;active_alerts</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"[</span><span class="mtk12">{</span><span class="mtk1">alert</span><span class="mtk12">[</span><span class="mtk6">4</span><span class="mtk12">]}</span><span class="mtk5">]&nbsp;</span><span class="mtk12">{</span><span class="mtk1">alert</span><span class="mtk12">[</span><span class="mtk6">2</span><span class="mtk12">]}</span><span class="mtk5">&nbsp;(Severity:&nbsp;</span><span class="mtk12">{</span><span class="mtk1">alert</span><span class="mtk12">[</span><span class="mtk6">3</span><span class="mtk12">]}</span><span class="mtk5">)"</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">else</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"\nNo&nbsp;active&nbsp;alerts"</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">return</span><span class="mtk1">&nbsp;active_alerts</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Main&nbsp;simulation&nbsp;loop</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">run_cmms_simulation</span><span class="mtk1">()</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;conn&nbsp;=&nbsp;init_db</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">try</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Simulate&nbsp;30&nbsp;days&nbsp;of&nbsp;operation&nbsp;with&nbsp;daily&nbsp;checks</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">for</span><span class="mtk1">&nbsp;day&nbsp;</span><span class="mtk17">in</span><span class="mtk1">&nbsp;</span><span class="mtk15">range</span><span class="mtk12">(</span><span class="mtk6">30</span><span class="mtk12">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"\n===&nbsp;Day&nbsp;</span><span class="mtk12">{</span><span class="mtk1">day&nbsp;+&nbsp;</span><span class="mtk6">1</span><span class="mtk12">}</span><span class="mtk5">&nbsp;==="</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;current_date&nbsp;=&nbsp;datetime.now</span><span class="mtk12">()</span><span class="mtk1">.date</span><span class="mtk12">()</span><span class="mtk1">&nbsp;+&nbsp;timedelta</span><span class="mtk12">(</span><span class="mtk1">days=day</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"System&nbsp;date:&nbsp;</span><span class="mtk12">{</span><span class="mtk1">current_date</span><span class="mtk12">}</span><span class="mtk5">"</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Run&nbsp;maintenance&nbsp;check</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alerts&nbsp;=&nbsp;check_maintenance</span><span class="mtk12">(</span><span class="mtk1">conn</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Resolve&nbsp;some&nbsp;alerts&nbsp;automatically&nbsp;(simulation)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">if</span><span class="mtk1">&nbsp;alerts</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor&nbsp;=&nbsp;conn.cursor</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'UPDATE&nbsp;alerts&nbsp;SET&nbsp;resolved&nbsp;=&nbsp;1&nbsp;WHERE&nbsp;id&nbsp;=&nbsp;?'</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">(</span><span class="mtk1">alerts</span><span class="mtk12">[</span><span class="mtk6">0</span><span class="mtk12">][</span><span class="mtk6">0</span><span class="mtk12">],)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;conn.commit</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"Resolved&nbsp;alert&nbsp;ID&nbsp;</span><span class="mtk12">{</span><span class="mtk1">alerts</span><span class="mtk12">[</span><span class="mtk6">0</span><span class="mtk12">][</span><span class="mtk6">0</span><span class="mtk12">]}</span><span class="mtk5">"</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Advance&nbsp;time&nbsp;(in&nbsp;simulation)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time.sleep</span><span class="mtk12">(</span><span class="mtk6">1</span><span class="mtk12">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Just&nbsp;for&nbsp;visualization&nbsp;in&nbsp;Colab</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">finally</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;conn.close</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Run&nbsp;the&nbsp;simulation</span></span><br><span><span class="mtk1">run_cmms_simulation</span><span class="mtk12">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 8 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-30 output_text"><pre>
=== Day 1 ===
System date: 2025-03-31

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:07] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 1

=== Day 2 ===
System date: 2025-04-01

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:08] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 3

=== Day 3 ===
System date: 2025-04-02

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:09] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 5

=== Day 4 ===
System date: 2025-04-03

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:10] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 7

=== Day 5 ===
System date: 2025-04-04

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:11] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 9

=== Day 6 ===
System date: 2025-04-05

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:12] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 11

=== Day 7 ===
System date: 2025-04-06

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:13] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 13

=== Day 8 ===
System date: 2025-04-07

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:14] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 15

=== Day 9 ===
System date: 2025-04-08

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:15] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 17

=== Day 10 ===
System date: 2025-04-09

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:16] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 19

=== Day 11 ===
System date: 2025-04-10

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:17] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 21

=== Day 12 ===
System date: 2025-04-11

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:18] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 23

=== Day 13 ===
System date: 2025-04-12

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:19] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 25

=== Day 14 ===
System date: 2025-04-13

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:20] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 27

=== Day 15 ===
System date: 2025-04-14

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:21] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 29

=== Day 16 ===
System date: 2025-04-15

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:22] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 31

=== Day 17 ===
System date: 2025-04-16

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:23] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 33

=== Day 18 ===
System date: 2025-04-17

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:24] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 35

=== Day 19 ===
System date: 2025-04-18

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:25] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 37

=== Day 20 ===
System date: 2025-04-19

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:26] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 39

=== Day 21 ===
System date: 2025-04-20

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:27] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 41

=== Day 22 ===
System date: 2025-04-21

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:28] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 43

=== Day 23 ===
System date: 2025-04-22

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:29] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:29] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 45

=== Day 24 ===
System date: 2025-04-23

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:30] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:30] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:29] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 47

=== Day 25 ===
System date: 2025-04-24

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:31] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:31] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:30] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:29] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 49

=== Day 26 ===
System date: 2025-04-25

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:32] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:32] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:31] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:30] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:29] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 51

=== Day 27 ===
System date: 2025-04-26

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:33] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:33] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:32] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:31] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:30] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:29] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 53

=== Day 28 ===
System date: 2025-04-27

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:34] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:34] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:33] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:32] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:31] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:30] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:29] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 55

=== Day 29 ===
System date: 2025-04-28

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:35] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:35] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:34] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:33] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:32] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:31] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:30] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:29] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 57

=== Day 30 ===
System date: 2025-04-29

Running maintenance check...
ALERT: Maintenance overdue for Generator (was due on 2025-03-26)
INFO: Maintenance coming up for HVAC System on 2025-04-02

Active Alerts:
[2025-03-31 12:30:36] Maintenance overdue for Generator (Severity: high)
[2025-03-31 12:30:36] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:35] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:34] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:33] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:32] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:31] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:30] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:29] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:28] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:27] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:26] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:25] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:24] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:23] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:22] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:21] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:20] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:19] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:18] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:17] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:16] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:15] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:14] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:13] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:12] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:11] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:10] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:09] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:08] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
[2025-03-31 12:30:07] Maintenance scheduled for HVAC System on 2025-04-02 (Severity: medium)
Resolved alert ID 59
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-6RJBv-TIElmf" role="region" aria-label="Cell 9: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
6:00 PM (18 minutes ago)
executed in 2.515s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->6:00 PM (18 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 2.515s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk17">!</span><span class="mtk1">pip&nbsp;install&nbsp;twilio</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 9 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Requirement already satisfied: twilio in /usr/local/lib/python3.11/dist-packages (9.5.1)
Requirement already satisfied: requests&gt;=2.0.0 in /usr/local/lib/python3.11/dist-packages (from twilio) (2.32.3)
Requirement already satisfied: PyJWT&lt;3.0.0,&gt;=2.0.0 in /usr/local/lib/python3.11/dist-packages (from twilio) (2.10.1)
Requirement already satisfied: aiohttp&gt;=3.8.4 in /usr/local/lib/python3.11/dist-packages (from twilio) (3.11.14)
Requirement already satisfied: aiohttp-retry&gt;=2.8.3 in /usr/local/lib/python3.11/dist-packages (from twilio) (2.9.1)
Requirement already satisfied: aiohappyeyeballs&gt;=2.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp&gt;=3.8.4-&gt;twilio) (2.6.1)
Requirement already satisfied: aiosignal&gt;=1.1.2 in /usr/local/lib/python3.11/dist-packages (from aiohttp&gt;=3.8.4-&gt;twilio) (1.3.2)
Requirement already satisfied: attrs&gt;=17.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp&gt;=3.8.4-&gt;twilio) (25.3.0)
Requirement already satisfied: frozenlist&gt;=1.1.1 in /usr/local/lib/python3.11/dist-packages (from aiohttp&gt;=3.8.4-&gt;twilio) (1.5.0)
Requirement already satisfied: multidict&lt;7.0,&gt;=4.5 in /usr/local/lib/python3.11/dist-packages (from aiohttp&gt;=3.8.4-&gt;twilio) (6.2.0)
Requirement already satisfied: propcache&gt;=0.2.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp&gt;=3.8.4-&gt;twilio) (0.3.0)
Requirement already satisfied: yarl&lt;2.0,&gt;=1.17.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp&gt;=3.8.4-&gt;twilio) (1.18.3)
Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in /usr/local/lib/python3.11/dist-packages (from requests&gt;=2.0.0-&gt;twilio) (3.4.1)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in /usr/local/lib/python3.11/dist-packages (from requests&gt;=2.0.0-&gt;twilio) (3.10)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests&gt;=2.0.0-&gt;twilio) (2.3.0)
Requirement already satisfied: certifi&gt;=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests&gt;=2.0.0-&gt;twilio) (2025.1.31)
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-tYmHcgvCFOhp" role="region" aria-label="Cell 10: Code cell: " style="" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
6:00 PM (18 minutes ago)
executed in 0.705s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->6:00 PM (18 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 0.705s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;sqlite3</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;datetime&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;datetime</span><span class="mtk12">,</span><span class="mtk1">&nbsp;timedelta</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;twilio.rest&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;Client&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;For&nbsp;SMS&nbsp;alerts</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;=====&nbsp;CONFIGURATION&nbsp;=====</span></span><br><span><span class="mtk1">TWILIO_ACCOUNT_SID&nbsp;=&nbsp;</span><span class="mtk5">'ACde33f7ef6b3ce42cc34696f0502d6ffc'</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Replace&nbsp;with&nbsp;your&nbsp;Twilio&nbsp;SID</span></span><br><span><span class="mtk1">TWILIO_AUTH_TOKEN&nbsp;=&nbsp;</span><span class="mtk5">'3a5478300f322442df47490cbf9f0a32'</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Replace&nbsp;with&nbsp;your&nbsp;Twilio&nbsp;token</span></span><br><span><span class="mtk1">TWILIO_PHONE_NUMBER&nbsp;=&nbsp;</span><span class="mtk5">'+19414156754'</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Your&nbsp;Twilio&nbsp;phone&nbsp;number</span></span><br><span><span class="mtk1">OWNER_PHONE_NUMBER&nbsp;=&nbsp;</span><span class="mtk5">'6301272493'</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Indian&nbsp;phone&nbsp;number&nbsp;(without&nbsp;+91)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;=====&nbsp;SAMPLE&nbsp;VEHICLE&nbsp;DATA&nbsp;=====</span></span><br><span><span class="mtk1">VEHICLES&nbsp;=&nbsp;</span><span class="mtk12">[</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">{</span><span class="mtk5">"name"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Toyota&nbsp;Camry"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"last_service"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk5">"2023-10-01"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"service_interval_days"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk6">30</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"owner_phone"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;OWNER_PHONE_NUMBER</span><span class="mtk12">},</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">{</span><span class="mtk5">"name"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Ford&nbsp;F-150"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"last_service"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk5">"2023-09-15"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"service_interval_days"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk6">60</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"owner_phone"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;OWNER_PHONE_NUMBER</span><span class="mtk12">},</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">{</span><span class="mtk5">"name"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Tesla&nbsp;Model&nbsp;3"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"last_service"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk5">"2023-11-01"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"service_interval_days"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;</span><span class="mtk6">90</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"owner_phone"</span><span class="mtk12">:</span><span class="mtk1">&nbsp;OWNER_PHONE_NUMBER</span><span class="mtk12">},</span></span><br><span><span class="mtk12">]</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;=====&nbsp;FORMAT&nbsp;PHONE&nbsp;NUMBERS&nbsp;TO&nbsp;E.164&nbsp;=====</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">format_phone_number</span><span class="mtk1">(</span><span class="mtk4">phone</span><span class="mtk1">)</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">"""Ensure&nbsp;phone&nbsp;number&nbsp;is&nbsp;in&nbsp;E.164&nbsp;format&nbsp;for&nbsp;Indi</span><span class="mtk5">a."""</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;phone&nbsp;=&nbsp;phone.strip</span><span class="mtk12">()</span><span class="mtk1">.replace</span><span class="mtk12">(</span><span class="mtk5">"&nbsp;"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">""</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">if</span><span class="mtk1">&nbsp;</span><span class="mtk17">not</span><span class="mtk1">&nbsp;phone.startswith</span><span class="mtk12">(</span><span class="mtk5">"+"</span><span class="mtk12">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phone&nbsp;=&nbsp;</span><span class="mtk5">"+91"</span><span class="mtk1">&nbsp;+&nbsp;phone&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Append&nbsp;India&nbsp;country&nbsp;code&nbsp;if&nbsp;missing</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">return</span><span class="mtk1">&nbsp;phone</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;=====&nbsp;DATABASE&nbsp;SETUP&nbsp;=====</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">setup_database</span><span class="mtk1">()</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;conn&nbsp;=&nbsp;sqlite3.connect</span><span class="mtk12">(</span><span class="mtk5">':memory:'</span><span class="mtk12">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Temporary&nbsp;DB&nbsp;for&nbsp;testing</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor&nbsp;=&nbsp;conn.cursor</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Create&nbsp;VEHICLES&nbsp;table</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span><span class="mtk5">'''</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;CREATE&nbsp;TABLE&nbsp;vehicles&nbsp;(</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id&nbsp;INTEGER&nbsp;PRIMARY&nbsp;KEY&nbsp;AUTOINCREMENT,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;TEXT&nbsp;NOT&nbsp;NULL,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_service_date&nbsp;DATE,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_service_date&nbsp;DATE,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service_interval_days&nbsp;INTEGER,</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;owner_phone&nbsp;TEXT</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;)</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;'''</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Insert&nbsp;sample&nbsp;vehicles</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;today&nbsp;=&nbsp;datetime.now</span><span class="mtk12">()</span><span class="mtk1">.date</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">for</span><span class="mtk1">&nbsp;vehicle&nbsp;</span><span class="mtk17">in</span><span class="mtk1">&nbsp;VEHICLES</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_service&nbsp;=&nbsp;datetime.strptime</span><span class="mtk12">(</span><span class="mtk1">vehicle</span><span class="mtk12">[</span><span class="mtk5">"last_service"</span><span class="mtk12">],</span><span class="mtk1">&nbsp;</span><span class="mtk5">"%Y-%m-%d"</span><span class="mtk12">)</span><span class="mtk1">.date</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_service&nbsp;=&nbsp;last_service&nbsp;+&nbsp;timedelta</span><span class="mtk12">(</span><span class="mtk1">days=vehicle</span><span class="mtk12">[</span><span class="mtk5">"service_interval_days"</span><span class="mtk12">])</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span><span class="mtk5">'''</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INSERT&nbsp;INTO&nbsp;vehicles&nbsp;(name,&nbsp;last_service_d</span><span class="mtk5">ate,&nbsp;next_service_date,&nbsp;service_interval_days,&nbsp;own</span><span class="mtk5">er_phone)</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VALUES&nbsp;(?,&nbsp;?,&nbsp;?,&nbsp;?,&nbsp;?)</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vehicle</span><span class="mtk12">[</span><span class="mtk5">"name"</span><span class="mtk12">],</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_service</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_service</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vehicle</span><span class="mtk12">[</span><span class="mtk5">"service_interval_days"</span><span class="mtk12">],</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format_phone_number</span><span class="mtk12">(</span><span class="mtk1">vehicle</span><span class="mtk12">[</span><span class="mtk5">"owner_phone"</span><span class="mtk12">])</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">))</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;conn.commit</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">return</span><span class="mtk1">&nbsp;conn</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;=====&nbsp;SMS&nbsp;ALERT&nbsp;FUNCTION&nbsp;=====</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">send_sms</span><span class="mtk1">(</span><span class="mtk4">to_number</span><span class="mtk1">,&nbsp;</span><span class="mtk4">message</span><span class="mtk1">)</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">try</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client&nbsp;=&nbsp;Client</span><span class="mtk12">(</span><span class="mtk1">TWILIO_ACCOUNT_SID</span><span class="mtk12">,</span><span class="mtk1">&nbsp;TWILIO_AUTH_TOKEN</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sms&nbsp;=&nbsp;client.messages.create</span><span class="mtk12">(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;body=message</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from_=TWILIO_PHONE_NUMBER</span><span class="mtk12">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to=format_phone_number</span><span class="mtk12">(</span><span class="mtk1">to_number</span><span class="mtk12">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Ensure&nbsp;correct&nbsp;format</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"📲&nbsp;SMS&nbsp;sent&nbsp;to&nbsp;</span><span class="mtk12">{</span><span class="mtk1">to_number</span><span class="mtk12">}</span><span class="mtk5">"</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">return</span><span class="mtk1">&nbsp;</span><span class="mtk9">True</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">except</span><span class="mtk1">&nbsp;Exception&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;e</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"❌&nbsp;SMS&nbsp;failed:&nbsp;</span><span class="mtk12">{</span><span class="mtk1">e</span><span class="mtk12">}</span><span class="mtk5">"</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">return</span><span class="mtk1">&nbsp;</span><span class="mtk9">False</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;=====&nbsp;CHECK&nbsp;FOR&nbsp;DUE&nbsp;SERVICES&nbsp;=====</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">check_vehicle_service</span><span class="mtk1">(</span><span class="mtk4">db</span><span class="mtk1">)</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">with</span><span class="mtk1">&nbsp;db</span><span class="mtk12">:</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Ensures&nbsp;commit&nbsp;and&nbsp;close</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor&nbsp;=&nbsp;db.cursor</span><span class="mtk12">()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;today&nbsp;=&nbsp;datetime.now</span><span class="mtk12">()</span><span class="mtk1">.date</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Get&nbsp;vehicles&nbsp;due&nbsp;for&nbsp;service</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span><span class="mtk5">'''</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SELECT&nbsp;name,&nbsp;next_service_date,&nbsp;owner_phon</span><span class="mtk5">e</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FROM&nbsp;vehicles</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHERE&nbsp;next_service_date&nbsp;&lt;=&nbsp;?</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk12">(</span><span class="mtk1">today</span><span class="mtk12">,))</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;due_vehicles&nbsp;=&nbsp;cursor.fetchall</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk18">for</span><span class="mtk1">&nbsp;name</span><span class="mtk12">,</span><span class="mtk1">&nbsp;due_date</span><span class="mtk12">,</span><span class="mtk1">&nbsp;phone&nbsp;</span><span class="mtk17">in</span><span class="mtk1">&nbsp;due_vehicles</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert_msg&nbsp;=&nbsp;</span><span class="mtk9">f</span><span class="mtk5">"🔧&nbsp;SERVICE&nbsp;REQUIRED:&nbsp;</span><span class="mtk12">{</span><span class="mtk1">name</span><span class="mtk12">}</span><span class="mtk5">&nbsp;is&nbsp;overdue&nbsp;for&nbsp;service!&nbsp;(Due&nbsp;on:&nbsp;</span><span class="mtk12">{</span><span class="mtk1">due_date</span><span class="mtk12">}</span><span class="mtk5">)"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk9">f</span><span class="mtk5">"🚨&nbsp;</span><span class="mtk12">{</span><span class="mtk1">alert_msg</span><span class="mtk12">}</span><span class="mtk5">"</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Send&nbsp;SMS&nbsp;alert</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_sms</span><span class="mtk12">(</span><span class="mtk1">phone</span><span class="mtk12">,</span><span class="mtk1">&nbsp;alert_msg</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Update&nbsp;next&nbsp;service&nbsp;date&nbsp;(for&nbsp;simulation)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new_due_date&nbsp;=&nbsp;today&nbsp;+&nbsp;timedelta</span><span class="mtk12">(</span><span class="mtk1">days=</span><span class="mtk6">30</span><span class="mtk12">)</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Reset&nbsp;for&nbsp;next&nbsp;interval</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute</span><span class="mtk12">(</span><span class="mtk5">'''</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UPDATE&nbsp;vehicles</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SET&nbsp;last_service_date&nbsp;=&nbsp;?,&nbsp;next_servic</span><span class="mtk5">e_date&nbsp;=&nbsp;?</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHERE&nbsp;name&nbsp;=&nbsp;?</span></span><br><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk12">(</span><span class="mtk1">today</span><span class="mtk12">,</span><span class="mtk1">&nbsp;new_due_date</span><span class="mtk12">,</span><span class="mtk1">&nbsp;name</span><span class="mtk12">))</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;=====&nbsp;RUN&nbsp;THE&nbsp;SYSTEM&nbsp;=====</span></span><br><span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">main</span><span class="mtk1">()</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"🚘&nbsp;Starting&nbsp;Vehicle&nbsp;Maintenance&nbsp;Alert&nbsp;</span><span class="mtk5">System...\n"</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;db&nbsp;=&nbsp;setup_database</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Simulate&nbsp;a&nbsp;maintenance&nbsp;check</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"🔍&nbsp;Checking&nbsp;vehicle&nbsp;service&nbsp;status...\n"</span><span class="mtk12">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;check_vehicle_service</span><span class="mtk12">(</span><span class="mtk1">db</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"\n✅&nbsp;Done!&nbsp;Check&nbsp;your&nbsp;phone&nbsp;for&nbsp;SMS&nbsp;alerts."</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk18">if</span><span class="mtk1">&nbsp;</span><span class="mtk4">__name__</span><span class="mtk1">&nbsp;==&nbsp;</span><span class="mtk5">"__main__"</span><span class="mtk12">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;main</span><span class="mtk12">()</span></span><br><span><span></span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 10 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-3 output_text"><pre>🚘 Starting Vehicle Maintenance Alert System...

🔍 Checking vehicle service status...

🚨 🔧 SERVICE REQUIRED: Toyota Camry is overdue for service! (Due on: 2023-10-31)
📲 SMS sent to +916301272493
🚨 🔧 SERVICE REQUIRED: Ford F-150 is overdue for service! (Due on: 2023-11-14)
📲 SMS sent to +916301272493
🚨 🔧 SERVICE REQUIRED: Tesla Model 3 is overdue for service! (Due on: 2024-01-30)
📲 SMS sent to +916301272493

✅ Done! Check your phone for SMS alerts.
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell text" id="cell-Ce5CGc0oI5fx" role="region" aria-label="Cell 11: Text cell: ===== CONFIGURATION =====" style="opacity: 1;" tabindex="-1"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p>import sqlite3
from datetime import datetime, timedelta
from twilio.rest import Client  # For SMS alerts</p>
<div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 2 child cells under ===== CONFIGURATION ===== (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 2 child cells under ===== CONFIGURATION ===== (Press &lt;Shift&gt; to also collapse sibling sections)" style="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 2 child cells under ===== CONFIGURATION ===== (Press &lt;Shift&gt; to also collapse sibling sections)">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>===== CONFIGURATION =====</h1></div>
<p>TWILIO_ACCOUNT_SID = 'ACde33f7ef6b3ce42cc34696f0502d6ffc'  # Replace with your Twilio SID
TWILIO_AUTH_TOKEN = '3a5478300f322442df47490cbf9f0a32'    # Replace with your Twilio token
TWILIO_PHONE_NUMBER = '+19414156754'             # Your Twilio phone number
OWNER_PHONE_NUMBER = '6301272493'                # Indian phone number (without +91)</p>
<h1>===== SAMPLE VEHICLE DATA =====</h1>
<p>VEHICLES = [
    {"name": "Toyota Camry", "last_service": "2025-05-01", "service_interval_days": 30, "owner_phone": OWNER_PHONE_NUMBER},
    {"name": "Ford F-150", "last_service": "2025-05-15", "service_interval_days": 60, "owner_phone": OWNER_PHONE_NUMBER},
    {"name": "Mahindra XUV-700", "last_service": "2025-06-01", "service_interval_days": 90, "owner_phone": OWNER_PHONE_NUMBER},
]</p>
<h1>===== FORMAT PHONE NUMBERS TO E.164 =====</h1>
<p>def format_phone_number(phone):
    """Ensure phone number is in E.164 format for India."""
    phone = phone.strip().replace(" ", "")
    if not phone.startswith("+"):
        phone = "+91" + phone  # Append India country code if missing
    return phone</p>
<h1>===== DATABASE SETUP =====</h1>
<p>def setup_database():
    conn = sqlite3.connect(':memory:')  # Temporary DB for testing
    cursor = conn.cursor()</p>
<pre><code><span><span class="mtk1">#&nbsp;Create&nbsp;VEHICLES&nbsp;table</span></span><br><span><span class="mtk1">cursor.execute('''</span></span><br><span><span class="mtk1">CREATE&nbsp;TABLE&nbsp;vehicles&nbsp;(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;id&nbsp;INTEGER&nbsp;PRIMARY&nbsp;KEY&nbsp;AUTOINCREMENT,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;TEXT&nbsp;NOT&nbsp;NULL,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;last_service_date&nbsp;DATE,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;next_service_date&nbsp;DATE,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;service_interval_days&nbsp;INTEGER,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;owner_phone&nbsp;TEXT</span></span><br><span><span class="mtk1">)</span></span><br><span><span class="mtk1">''')</span></span><br><span><span></span></span><br><span><span class="mtk1">#&nbsp;Insert&nbsp;sample&nbsp;vehicles</span></span><br><span><span class="mtk1">today&nbsp;=&nbsp;datetime.now().date()</span></span><br><span><span class="mtk1">for&nbsp;vehicle&nbsp;in&nbsp;VEHICLES:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;last_service&nbsp;=&nbsp;datetime.strptime(vehicle["last</span><span class="mtk1">_service"],&nbsp;"%Y-%m-%d").date()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;next_service&nbsp;=&nbsp;last_service&nbsp;+&nbsp;timedelta(days=v</span><span class="mtk1">ehicle["service_interval_days"])</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute('''</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;INSERT&nbsp;INTO&nbsp;vehicles&nbsp;(name,&nbsp;last_service_date,</span><span class="mtk1">&nbsp;next_service_date,&nbsp;service_interval_days,&nbsp;owner_p</span><span class="mtk1">hone)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;VALUES&nbsp;(?,&nbsp;?,&nbsp;?,&nbsp;?,&nbsp;?)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;''',&nbsp;(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vehicle["name"],</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_service,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_service,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vehicle["service_interval_days"],</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format_phone_number(vehicle["owner_phone"]</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;))</span></span><br><span><span></span></span><br><span><span class="mtk1">conn.commit()</span></span><br><span><span class="mtk1">return&nbsp;conn</span></span></code></pre><h1>===== SMS ALERT FUNCTION =====</h1>
<p>def send_sms(to_number, message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=format_phone_number(to_number)  # Ensure correct format
        )
        print(f"📲 SMS sent to {to_number}")
        return True
    except Exception as e:
        print(f"❌ SMS failed: {e}")
        return False</p>
<h1>===== CHECK FOR DUE SERVICES =====</h1>
<p>def check_vehicle_service(db):
    with db:  # Ensures commit and close
        cursor = db.cursor()
        today = datetime.now().date()</p>
<pre><code><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;Get&nbsp;vehicles&nbsp;due&nbsp;for&nbsp;service</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute('''</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;SELECT&nbsp;name,&nbsp;next_service_date,&nbsp;owner_phone</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;FROM&nbsp;vehicles</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;WHERE&nbsp;next_service_date&nbsp;&lt;=&nbsp;?</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;''',&nbsp;(today,))</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;due_vehicles&nbsp;=&nbsp;cursor.fetchall()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;for&nbsp;name,&nbsp;due_date,&nbsp;phone&nbsp;in&nbsp;due_vehicles:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert_msg&nbsp;=&nbsp;f"🔧&nbsp;SERVICE&nbsp;REQUIRED:&nbsp;{name}&nbsp;</span><span class="mtk1">is&nbsp;overdue&nbsp;for&nbsp;service!&nbsp;(Due&nbsp;on:&nbsp;{due_date})"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f"🚨&nbsp;{alert_msg}")</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;Send&nbsp;SMS&nbsp;alert</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_sms(phone,&nbsp;alert_msg)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;Update&nbsp;next&nbsp;service&nbsp;date&nbsp;(for&nbsp;simulation</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new_due_date&nbsp;=&nbsp;today&nbsp;+&nbsp;timedelta(days=30)&nbsp;</span><span class="mtk1">&nbsp;#&nbsp;Reset&nbsp;for&nbsp;next&nbsp;interval</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute('''</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UPDATE&nbsp;vehicles</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SET&nbsp;last_service_date&nbsp;=&nbsp;?,&nbsp;next_service_da</span><span class="mtk1">te&nbsp;=&nbsp;?</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHERE&nbsp;name&nbsp;=&nbsp;?</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;''',&nbsp;(today,&nbsp;new_due_date,&nbsp;name))</span></span></code></pre><h1>===== RUN THE SYSTEM =====</h1>
<p>def main():
    print("🚘 Starting Vehicle Maintenance Alert System...\n")
    db = setup_database()</p>
<pre><code><span><span class="mtk1">#&nbsp;Simulate&nbsp;a&nbsp;maintenance&nbsp;check</span></span><br><span><span class="mtk1">print("🔍&nbsp;Checking&nbsp;vehicle&nbsp;service&nbsp;status...\n")</span></span><br><span><span class="mtk1">check_vehicle_service(db)</span></span><br><span><span></span></span><br><span><span class="mtk1">print("\n✅&nbsp;Done!&nbsp;Check&nbsp;your&nbsp;phone&nbsp;for&nbsp;SMS&nbsp;</span><span class="mtk1">alerts.")</span></span></code></pre><p>if <strong>name</strong> == "<strong>main</strong>":
    main()</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$-->
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>subdirectory_arrow_right</md-icon>
          <span>2 cells hidden</span>
        </div>
      </div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-sHFOl-HAMZFV" tabindex="-1" role="region" aria-label="Cell 12: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
6:03 PM (14 minutes ago)
executed in 0.076s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->6:03 PM (14 minutes ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 0.076s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;tensorflow.keras.models&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;Sequential</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;tensorflow.keras.layers&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;Dense</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Define&nbsp;a&nbsp;simple&nbsp;model</span></span><br><span><span class="mtk1">model&nbsp;=&nbsp;Sequential</span><span class="mtk12">([</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;Dense</span><span class="mtk12">(</span><span class="mtk6">64</span><span class="mtk12">,</span><span class="mtk1">&nbsp;activation=</span><span class="mtk5">'relu'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;input_shape=</span><span class="mtk12">(</span><span class="mtk6">10</span><span class="mtk12">,)),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;Dense</span><span class="mtk12">(</span><span class="mtk6">1</span><span class="mtk12">,</span><span class="mtk1">&nbsp;activation=</span><span class="mtk5">'sigmoid'</span><span class="mtk12">)</span></span><br><span><span class="mtk12">])</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Save&nbsp;the&nbsp;model</span></span><br><span><span class="mtk1">model.save</span><span class="mtk12">(</span><span class="mtk5">'/content/drive/MyDrive/ml_model_for_project.h5'</span><span class="mtk12">)</span></span><br><span><span class="mtk15">print</span><span class="mtk12">(</span><span class="mtk5">"Model&nbsp;saved&nbsp;successfully!"</span><span class="mtk12">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$353632356$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 12 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>/usr/local/lib/python3.11/dist-packages/keras/src/layers/core/dense.py:87: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
WARNING:absl:You are saving your model as an HDF5 file via `model.save()` or `keras.saving.save_model(model)`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')` or `keras.saving.save_model(model, 'my_model.keras')`. 
</pre></div><div class="stream output-id-2 output_text"><pre>Model saved successfully!
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-5QKcsTCxMdGf" tabindex="-1" role="region" aria-label="Cell 13: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$353632356$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$353632356$--><span class="execution-count"><!--?lit$353632356$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$353632356$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$353632356$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$353632356$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Silaparasetty jaswanth
6:04 PM (1 hour ago)
executed in 0.317s"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$353632356$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$353632356$-->executed by Silaparasetty jaswanth</div><!----><!----><div><!--?lit$353632356$-->6:04 PM (1 hour ago)</div><!----><!----><div><!--?lit$353632356$-->executed in 0.317s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$353632356$--><!--?-->
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="142" data-mode-id="notebook-python" style="height: 105px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/25" style="width: 981px; height: 105px;"><div data-mprt="3" class="overflow-guard" style="width: 981px; height: 105px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 105px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 105px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 105px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 975px; height: 105px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 105px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 975px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:38px;width:177px;height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="current-line" style="width:975px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 975px; height: 105px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;tensorflow.keras.models&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;load_model</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1">model&nbsp;=&nbsp;load_model</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">'</span><span class="mtk5 detected-link">/content/drive/MyDrive/ml_model_for_project.h5</span><span class="mtk5">'</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"Model&nbsp;loaded&nbsp;successfully!"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 76px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 961px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 961px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="131" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 105px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 105px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 105px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 981px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 76px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 981px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 105px;"><div class="minimap-shadow-hidden" style="height: 105px;"></div><canvas width="0" height="131" style="position: absolute; left: 0px; width: 0px; height: 105px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="131" style="position: absolute; left: 0px; width: 0px; height: 105px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1408px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 647.46px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 13 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$353632356$--><!----><div><!--?lit$353632356$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>WARNING:absl:No training configuration found in the save file, so the model was *not* compiled. Compile it manually.
</pre></div><div class="stream output-id-2 output_text"><pre>Model loaded successfully!
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$353632356$-->Text
        </md-outlined-button>
        <!--?lit$353632356$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$353632356$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$353632356$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$353632356$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style=""></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer class="sn-resize no-tabs" style="height: 33.3%"><div class="resizer-thumb"></div>
        <!--?lit$353632356$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$353632356$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$353632356$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$353632356$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$353632356$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer class="sn-resize no-tabs" style="height: 33.3%"><div class="resizer-thumb"></div>
        <!--?lit$353632356$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$353632356$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./model_files/outputframe(2).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./model_files/outputframe(3).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar" style="min-height: inherit;"><template shadowrootmode="open"><!----><!--?lit$353632356$--> <div class="connect-status">
        <md-icon status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$--><svg viewBox="0 0 24 24"><!--?lit$353632356$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
        <div aria-atomic="true" aria-live="polite"><!--?lit$353632356$-->Connected to Python 3 Google Compute Engine backend</div>
      </div>
      <md-icon-button class="visible-on-closed" title="Connected" disabled="" value="" data-aria-label="Connected"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Connected" disabled="">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$353632356$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <!--?lit$353632356$--><!--?lit$353632356$-->
      <md-icon-button title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$353632356$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$353632356$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$353632356$--><span class="icon"><slot></slot></span>
        <!--?lit$353632356$-->
        <!--?lit$353632356$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu colab-styled-scroller" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 591px; visibility: visible; left: 68px; top: 62px; display: none;"><!--?lit$353632356$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Locate in Drive<!--?lit$353632356$--></div></div><div command="open-in-playground" class="goog-menuitem" role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Open in playground mode<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class="goog-menuitem" role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->New notebook in Drive<!--?lit$353632356$--></div></div><div command="open" class="goog-menuitem" role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Open notebook<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class="goog-menuitem" role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Upload notebook<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class="goog-menuitem" role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Rename<!--?lit$353632356$--></div></div><div command="move-notebook" class="goog-menuitem" role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Move<!--?lit$353632356$--></div></div><div command="trash" class="goog-menuitem" role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Move to trash<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class="goog-menuitem" role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Save a copy in Drive<!--?lit$353632356$--></div></div><div command="copy-to-gist" class="goog-menuitem" role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Save a copy as a GitHub Gist<!--?lit$353632356$--></div></div><div command="copy-to-github" class="goog-menuitem" role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Save a copy in GitHub<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class="goog-menuitem" role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Save<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class="goog-menuitem" role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Save and pin revision<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class="goog-menuitem" role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Revision history<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$353632356$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class="goog-menuitem" role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Print<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="user-select: none; left: 395.8px; top: 533.8px; display: none;"><!--?lit$353632356$--><div command="download-ipynb" class="goog-menuitem" role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Download .ipynb<!--?lit$353632356$--></div></div><div command="download-python" class="goog-menuitem" role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Download .py<!--?lit$353632356$--></div></div></div><div class="goog-menu colab-styled-scroller" id="edit-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 591px; visibility: visible; left: 106.85px; top: 62px; display: none;"><!--?lit$353632356$--><div command="undo" class="goog-menuitem" role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">Undo delete cell<span class="goog-menuitem-accel">Ctrl+M Z</span></div></div><div command="redo" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":r" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;">Redo<span class="goog-menuitem-accel">Ctrl+Shift+Y</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Select all cells<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Shift+A</span></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Cut cell or selection<!--?lit$353632356$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Copy cell or selection<!--?lit$353632356$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Paste<!--?lit$353632356$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Delete selected cells<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+M D</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Find and replace<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+H</span></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Find next<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+G</span></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Find previous<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Shift+G</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Notebook settings<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Clear all outputs<!--?lit$353632356$--></div></div></div><div class="goog-menu colab-styled-scroller" id="view-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 591px; visibility: visible; left: 148.512px; top: 62px; display: none;"><!--?lit$353632356$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----> </div><!--?lit$353632356$-->Table of contents<!--?lit$353632356$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Notebook info<!--?lit$353632356$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Executed code history<!--?lit$353632356$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$353632356$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1e" style="user-select: none;"></div><div command="collapse-sections" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1f" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Collapse sections<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+]</span></div></div><div command="expand-sections" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1g" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Expand sections<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+[</span></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none; display: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Save collapsed section layout<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1i" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Show/hide code<!--?lit$353632356$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Show/hide output<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+M O</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1l" style="user-select: none;"></div><div command="focus-next-tab" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1m" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Focus next tab<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Shift+]</span></div></div><div command="focus-previous-tab" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1n" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Focus previous tab<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Shift+[</span></div></div><div command="move-tab-to-next" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1o" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Move tab to next pane<!--?lit$353632356$--></div></div><div command="move-tab-to-prev" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1p" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Move tab to previous pane<!--?lit$353632356$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$353632356$--><div command="hide-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option" role="menuitemradio" id=":1b" style="user-select: none;" aria-checked="false"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"></div><!--?lit$353632356$-->Hide comments<!--?lit$353632356$--></div></div><div command="show-minimized-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option" role="menuitemradio" id=":1c" style="user-select: none;" aria-checked="false"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"></div><!--?lit$353632356$-->Minimize comments<!--?lit$353632356$--></div></div><div command="show-expanded-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option goog-option-selected" role="menuitemradio" id=":1d" style="user-select: none;" aria-checked="true"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$353632356$-->Expand comments<!--?lit$353632356$--></div></div></div><div class="goog-menu colab-styled-scroller" id="insert-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 591px; visibility: visible; left: 195.488px; top: 62px; display: none;"><!--?lit$353632356$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Code cell<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+M B</span></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Text cell<!--?lit$353632356$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Section header cell<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1u" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Scratch code cell<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Alt+N</span></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Code snippets<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Alt+P</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1x" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Add a form field<!--?lit$353632356$--></div></div></div><div class="goog-menu colab-styled-scroller" id="runtime-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 591px; visibility: visible; left: 249.975px; top: 62px; display: none;"><!--?lit$353632356$--><div command="runall" class="goog-menuitem" role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Run all<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+F9</span></div></div><div command="runbefore" class="goog-menuitem" role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Run before<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+F8</span></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Run the focused cell<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Enter</span></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Run selection<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Shift+Enter</span></div></div><div command="runafter" class="goog-menuitem" role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Run cell and below<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+F10</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":25" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Interrupt execution<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+M I</span></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":27" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Restart session<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+M .</span></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Restart session and run all<!--?lit$353632356$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Disconnect and delete runtime<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2a" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Change runtime type<!--?lit$353632356$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Manage sessions<!--?lit$353632356$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->View resources<!--?lit$353632356$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->View runtime logs<!--?lit$353632356$--></div></div></div><div class="goog-menu colab-styled-scroller" id="tools-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 591px; visibility: visible; left: 320.038px; top: 62px; display: none;"><!--?lit$353632356$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Command palette<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Shift+P</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Settings<!--?lit$353632356$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Keyboard shortcuts<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+M H</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2l" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Diff notebooks<!--?lit$353632356$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$353632356$-->(opens in a new tab)</span></div></div></div><div class="goog-menu colab-styled-scroller" id="help-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 591px; visibility: visible; left: 370.638px; top: 62px; display: none;"><!--?lit$353632356$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Frequently asked questions<!--?lit$353632356$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->View release notes<!--?lit$353632356$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Search code snippets<!--?lit$353632356$--><span class="goog-menuitem-accel">Ctrl+Alt+P</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2r" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Report a bug<!--?lit$353632356$--></div></div><div command="report-abuse" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":2t" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Report Drive abuse<!--?lit$353632356$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->Send feedback<!--?lit$353632356$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$353632356$-->View terms of service<!--?lit$353632356$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$353632356$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$353632356$--><button id="button" class="button">
      <!--?lit$353632356$-->
      <span class="touch"></span>
      <!--?lit$353632356$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$353632356$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$353632356$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;">arg_s, Load code into the current frontend.

Usage:\  
&amp;nbsp;&amp;nbsp;%load \[options\] source

&amp;nbsp;&amp;nbsp;where source can be a filename, URL, input history range, macro, or
element in the user namespace

Options:

&amp;nbsp;&amp;nbsp;-r &amp;lt;lines&amp;gt;: Specify lines or ranges of lines to load from the source.  
&amp;nbsp;&amp;nbsp;Ranges could be specified as x-y (x..y) or in python-style x:y
(x..(y-1)). Both limits x and y can be left blank (meaning the
beginning and end of the file, respectively).

&amp;nbsp;&amp;nbsp;-s &amp;lt;symbols&amp;gt;: Specify function or classes to load from python source.

&amp;nbsp;&amp;nbsp;-y : Don't ask confirmation for loading source above 200 000 characters.

&amp;nbsp;&amp;nbsp;-n : Include the user's namespace when searching for source code.

This magic command can either take a local filename, a URL, an history
range (see %history) or a macro as argument, it will prompt for
confirmation before loading source with more than 200 000 characters, unless
-y flag is passed or if the frontend does not support raw\_input:

```
%load myscript.py
```

%load 7-27
%load myMacro  
%load http://www.example.com/myscript.py
%load -r 5-10 myscript.py  
%load -r 10-20,30,40: foo.py
%load -s MyClass,wonder\_function myscript.py
%load -n MyClass
%load -n my\_module.wonder\_function, hint</div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxyf95c54f36a4056f1ca27c02f7f79c7056ddf6f4d0.43525489" name="apiproxyf95c54f36a4056f1ca27c02f7f79c7056ddf6f4d0.43525489" src="./model_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-z4mt99g9zzaw" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./model_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./model_files/saved_resource(1).html"></iframe></div><iframe src="./model_files/bscframe.html" style="display: none;"></iframe><iframe id="apiproxy583da18b27e1110ffab69ea4612a753e36ea96520.200516577" name="apiproxy583da18b27e1110ffab69ea4612a753e36ea96520.200516577" src="./model_files/proxy(1).html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe></body></html>