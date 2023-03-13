# HD OSD tool

This tool lets you configure your OSD, supporting larger grid sizes than the standard Ardupilot one.

<style>
    body{
       box-sizing: border-box;
       -moz-box-sizing: border-box;
       -webkit-box-sizing: border-box;

   } 
   div.box{
       /* 50x18 & 53x20 */
       width: 24px; 
       height: 36px;

       background-color:lightskyblue transparent ;

       border: 1px solid grey;
       border-style: none none solid solid;
       box-sizing: border-box;
       -moz-box-sizing: border-box;
       -webkit-box-sizing: border-box;

       float: left;
       font-size: smaller;
       color: white;
       position: relative;
   }
   div.box_50x18{
       /* 50x18 & 53x20 */
       width: 24px; 
       height: 36px;
   }
   div.box_53x20{
       /* 50x18 & 53x20 */
       width: 24px; 
       height: 36px;
   }
   div.box_60x22{
       /* 60x22 */
       width: 21px;
       height: 30px; 
   }
   div.ground{
       background-color:peru transparent;
   }
   div.end{
       clear: right;
       /* WS */
       /* margin-left: 0px; */
       /* DJI */
       /* margin-left: 20px; */
   }
   div.start{
       clear: left;
   }  
   div.used{
       background-color: rgba(128, 255, 0, 0.4);
       color: rgba(232, 247, 217, 0.4);
       border: 2px solid rgba(255, 78, 78, 0.7);

       font-weight: bold;
       font-size: larger;
       font-size: 3ex;

       -webkit-text-stroke: 1px black; /* outline */
       text-align: left;

       padding: 2px;
       z-index: 1000;
   }
   div.occupied{
       background-color: rgba(30, 40, 31, 0.4) ;
       z-index: 1001;
   }
   div.bottom{
       position: absolute; 
       bottom: 0px;
   }
   div.maincontainer{
       /* width: 1282px; */
       width: 100%;
       border: 1px solid black;
       float: left;
   }
   div.background{
       width: 1280px;
       height: 720px;
       z-index: 0;
       background-image: url("https://imgz.org/iCRSQqkC.jpg");
       background-repeat: no-repeat;
       border: none;
       float: left;
       clear: left;
       display: inline-block;
   }
   div.grid{
       padding-top: 30px;
       padding-left: 40px;
   }
   div.grid50x18{
       padding-top: 35px;
       padding-left: 40px;
   }
   div.grid53x20{
       padding-top: 0px;
       padding-left: 0px;
   }
   div.grid60x22{
       padding-top: 30px;
       padding-left: 10px;
   }
   div.newline{
       float:left;
       clear:both;
   }
   div.error{
       clear:both;
       color:black;
       border: 1px solid red;
       background-color: darksalmon;
       padding: 20px;
       font-weight: heavy;
       display: none;
       width: 300px;
   }
   div.param{
       border: 1px solid black;
       float: left;
       clear: both;
       padding: 3px;
       width: 100%;
   }

   /* override main css of stavros frontend */
   .content main{
       margin: 1px
   }
</style>
<div  style="float: left;">
   <table>
       <tr>
           <td colspan="2">
           <b>TIP: use OSDn_TXT_RES=3 to extend the grid from 50x18 to 60x22.*</b>
           <p>To use the tool:</p>
<ol>
           <li>Create a parameter backup using Parachute or Mission Planner.</li>
           <li>Paste your configuration in the textbox below. Your OSD items will be displayed.</li>
           <li>Resize your browser window to your needs (strg +/- | cmd +/-).</li>
           <li>Add OSD elements from the list on the right or re-arrange them as you like.</li>
           <li>Copy the generated parachute command to the CLI or the Mission Planner config to a textfile and restore.</li>
</ol>
           </td>
       </tr>
       <tr>
           <td>
               Show coordinates: 
           </td>
           <td>
               <input type="checkbox" id="showCoords" value="true" onClick="drawOSD();" unchecked><br>
           </td>
       </tr>
       <tr>
           <td>
               Grid: 
           </td>
           <td>
               <select id="chooseGrid" onchange="switchGrid();"><option value="60x22">60x22 (WTF-OS)</option><option value="53x20">53x20 (Walksnail)</option><option value="50x18">50x18 (DJI-FPV)</option></select><br>
           </td>
       </tr>
       <tr>
           <td>
               Background:
           </td>
           <td>
               <select id="chooseBackground" onchange="switchBackground();">
                   <option value="iCRSQqkC">4:3</option>
                   <option value="i5iVNkQY">4:3 DJI Elements</option>
                   <option value="i5jr5EsY">16:9</option>
                   <option value="iCQ6ahqs">16:9 DJI Elements</option>
               </select>
           </td>
       </tr>
       <tr>
           <td>
               Paste your Parachute config:
           </td>
           <td>
               <textarea id="config" oninput="compute();" style="width:500px;height:50px">
                   {parameters: {OSD1_ACC_LAT_EN: {value: 0, index: 1276, type: 2},OSD1_ACC_LAT_X: {value: 0, index: 1277, type: 2},OSD1_ACC_LAT_Y: {value: 0, index: 1278, type: 2},OSD1_ACC_LONG_EN: {value: 0, index: 1273, type: 2},OSD1_ACC_LONG_X: {value: 0, index: 1274, type: 2},OSD1_ACC_LONG_Y: {value: 0, index: 1275, type: 2},OSD1_ACC_VERT_EN: {value: 0, index: 1279, type: 2},OSD1_ACC_VERT_X: {value: 0, index: 1280, type: 2},OSD1_ACC_VERT_Y: {value: 0, index: 1281, type: 2},OSD1_ALTITUDE_EN: {value: 0, index: 1049, type: 2},OSD1_ALTITUDE_X: {value: 42, index: 1050, type: 2},OSD1_ALTITUDE_Y: {value: 9, index: 1051, type: 2},OSD1_AOA_EN: {value: 0, index: 1285, type: 2},OSD1_AOA_X: {value: 0, index: 1286, type: 2},OSD1_AOA_Y: {value: 0, index: 1287, type: 2},OSD1_ARMING_EN: {value: 0, index: 1196, type: 2},OSD1_ARMING_X: {value: 5, index: 1197, type: 2},OSD1_ARMING_Y: {value: 5, index: 1198, type: 2},OSD1_ASPD1_EN: {value: 0, index: 1172, type: 2},OSD1_ASPD1_X: {value: 5, index: 1173, type: 2},OSD1_ASPD1_Y: {value: 5, index: 1174, type: 2},OSD1_ASPD2_EN: {value: 0, index: 1169, type: 2},OSD1_ASPD2_X: {value: 4, index: 1170, type: 2},OSD1_ASPD2_Y: {value: 4, index: 1171, type: 2},OSD1_ASPD_DEM_EN: {value: 0, index: 1270, type: 2},OSD1_ASPD_DEM_X: {value: 0, index: 1271, type: 2},OSD1_ASPD_DEM_Y: {value: 0, index: 1272, type: 2},OSD1_ASPEED_EN: {value: 0, index: 1094, type: 2},OSD1_ASPEED_X: {value: 0, index: 1095, type: 2},OSD1_ASPEED_Y: {value: 9, index: 1096, type: 2},OSD1_ATEMP_EN: {value: 0, index: 1160, type: 2},OSD1_ATEMP_X: {value: 0, index: 1161, type: 2},OSD1_ATEMP_Y: {value: 0, index: 1162, type: 2},OSD1_AUTO_FLP_EN: {value: 0, index: 1282, type: 2},OSD1_AUTO_FLP_X: {value: 0, index: 1283, type: 2},OSD1_AUTO_FLP_Y: {value: 0, index: 1284, type: 2},OSD1_AVGCELLV_EN: {value: 0, index: 1217, type: 2},OSD1_AVGCELLV_X: {value: 7, index: 1218, type: 2},OSD1_AVGCELLV_Y: {value: 0, index: 1219, type: 2},OSD1_AVG_EFFA_EN: {value: 0, index: 1312, type: 2},OSD1_AVG_EFFA_X: {value: 22, index: 1313, type: 2},OSD1_AVG_EFFA_Y: {value: 10, index: 1314, type: 2},OSD1_AVG_EFFG_EN: {value: 0, index: 1309, type: 2},OSD1_AVG_EFFG_X: {value: 22, index: 1310, type: 2},OSD1_AVG_EFFG_Y: {value: 10, index: 1311, type: 2},OSD1_BAT2REM_EN: {value: 0, index: 1321, type: 2},OSD1_BAT2REM_X: {value: 0, index: 1322, type: 2},OSD1_BAT2REM_Y: {value: 0, index: 1323, type: 2},OSD1_BAT2USED_EN: {value: 0, index: 1166, type: 2},OSD1_BAT2USED_X: {value: 0, index: 1167, type: 2},OSD1_BAT2USED_Y: {value: 0, index: 1168, type: 2},OSD1_BAT2_VLT_EN: {value: 0, index: 1163, type: 2},OSD1_BAT2_VLT_X: {value: 0, index: 1164, type: 2},OSD1_BAT2_VLT_Y: {value: 0, index: 1165, type: 2},OSD1_BATREM_EN: {value: 0, index: 1318, type: 2},OSD1_BATREM_X: {value: 23, index: 1319, type: 2},OSD1_BATREM_Y: {value: 3, index: 1320, type: 2},OSD1_BATTBAR_EN: {value: 0, index: 1193, type: 2},OSD1_BATTBAR_X: {value: 23, index: 1194, type: 2},OSD1_BATTBAR_Y: {value: 13, index: 1195, type: 2},OSD1_BATUSED_EN: {value: 0, index: 1061, type: 2},OSD1_BATUSED_X: {value: 41, index: 1062, type: 2},OSD1_BATUSED_Y: {value: 1, index: 1063, type: 2},OSD1_BAT_PCT_EN: {value: 0, index: 1300, type: 2},OSD1_BAT_PCT_X: {value: 0, index: 1301, type: 2},OSD1_BAT_PCT_Y: {value: 0, index: 1302, type: 2},OSD1_BAT_VOLT_EN: {value: 0, index: 1052, type: 2},OSD1_BAT_VOLT_X: {value: 1, index: 1053, type: 2},OSD1_BAT_VOLT_Y: {value: 0, index: 1054, type: 2},OSD1_BTEMP_EN: {value: 0, index: 1157, type: 2},OSD1_BTEMP_X: {value: 0, index: 1158, type: 2},OSD1_BTEMP_Y: {value: 0, index: 1159, type: 2},OSD1_CALLSIGN_EN: {value: 0, index: 1205, type: 2},OSD1_CALLSIGN_X: {value: 0, index: 1206, type: 2},OSD1_CALLSIGN_Y: {value: 0, index: 1207, type: 2},OSD1_CELLVOLT_EN: {value: 0, index: 1190, type: 2},OSD1_CELLVOLT_X: {value: 6, index: 1191, type: 2},OSD1_CELLVOLT_Y: {value: 0, index: 1192, type: 2},OSD1_CHAN_MAX: {value: 2100, index: 1048, type: 4},OSD1_CHAN_MIN: {value: 900, index: 1047, type: 4},OSD1_CLIMBEFF_EN: {value: 0, index: 1151, type: 2},OSD1_CLIMBEFF_X: {value: 0, index: 1152, type: 2},OSD1_CLIMBEFF_Y: {value: 0, index: 1153, type: 2},OSD1_CLK_EN: {value: 0, index: 1175, type: 2},OSD1_CLK_X: {value: 0, index: 1176, type: 2},OSD1_CLK_Y: {value: 0, index: 1177, type: 2},OSD1_COMPASS_EN: {value: 0, index: 1088, type: 2},OSD1_COMPASS_X: {value: 25, index: 1089, type: 2},OSD1_COMPASS_Y: {value: 0, index: 1090, type: 2},OSD1_CRSFANT_EN: {value: 0, index: 1297, type: 2},OSD1_CRSFANT_X: {value: 0, index: 1298, type: 2},OSD1_CRSFANT_Y: {value: 0, index: 1299, type: 2},OSD1_CRSFPWR_EN: {value: 0, index: 1288, type: 2},OSD1_CRSFPWR_X: {value: 0, index: 1289, type: 2},OSD1_CRSFPWR_Y: {value: 0, index: 1290, type: 2},OSD1_CRSFRSSI_EN: {value: 0, index: 1291, type: 2},OSD1_CRSFRSSI_X: {value: 0, index: 1292, type: 2},OSD1_CRSFRSSI_Y: {value: 0, index: 1293, type: 2},OSD1_CRSFSNR_EN: {value: 0, index: 1294, type: 2},OSD1_CRSFSNR_X: {value: 0, index: 1295, type: 2},OSD1_CRSFSNR_Y: {value: 0, index: 1296, type: 2},OSD1_CRSSHAIR_EN: {value: 0, index: 1181, type: 2},OSD1_CRSSHAIR_X: {value: 0, index: 1182, type: 2},OSD1_CRSSHAIR_Y: {value: 0, index: 1183, type: 2},OSD1_CRS_HADJ_EN: {value: 0, index: 1339, type: 2},OSD1_CRS_HADJ_X: {value: 0, index: 1340, type: 2},OSD1_CRS_HADJ_Y: {value: 0, index: 1341, type: 2},OSD1_CRS_HEAD_EN: {value: 0, index: 1336, type: 2},OSD1_CRS_HEAD_X: {value: 0, index: 1337, type: 2},OSD1_CRS_HEAD_Y: {value: 0, index: 1338, type: 2},OSD1_CURRENT2_EN: {value: 0, index: 1208, type: 2},OSD1_CURRENT2_X: {value: 0, index: 1209, type: 2},OSD1_CURRENT2_Y: {value: 0, index: 1210, type: 2},OSD1_CURRENT_EN: {value: 0, index: 1058, type: 2},OSD1_CURRENT_X: {value: 42, index: 1059, type: 2},OSD1_CURRENT_Y: {value: 0, index: 1060, type: 2},OSD1_EFFA_EN: {value: 0, index: 1315, type: 2},OSD1_EFFA_X: {value: 22, index: 1316, type: 2},OSD1_EFFA_Y: {value: 10, index: 1317, type: 2},OSD1_EFFG_EN: {value: 0, index: 1154, type: 2},OSD1_EFFG_X: {value: 22, index: 1155, type: 2},OSD1_EFFG_Y: {value: 10, index: 1156, type: 2},OSD1_ENABLE: {value: 1, index: 1046, type: 2},OSD1_ESCAAMPS_EN: {value: 0, index: 1109, type: 2},OSD1_ESCAAMPS_X: {value: 24, index: 1110, type: 2},OSD1_ESCAAMPS_Y: {value: 14, index: 1111, type: 2},OSD1_ESCARPM_EN: {value: 0, index: 1103, type: 2},OSD1_ESCARPM_X: {value: 22, index: 1104, type: 2},OSD1_ESCARPM_Y: {value: 12, index: 1105, type: 2},OSD1_ESCHAMPS_EN: {value: 0, index: 1106, type: 2},OSD1_ESCHAMPS_X: {value: 24, index: 1107, type: 2},OSD1_ESCHAMPS_Y: {value: 14, index: 1108, type: 2},OSD1_ESCHRPM_EN: {value: 0, index: 1115, type: 2},OSD1_ESCHRPM_X: {value: 22, index: 1116, type: 2},OSD1_ESCHRPM_Y: {value: 12, index: 1117, type: 2},OSD1_ESCTAMPS_EN: {value: 0, index: 1112, type: 2},OSD1_ESCTAMPS_X: {value: 24, index: 1113, type: 2},OSD1_ESCTAMPS_Y: {value: 14, index: 1114, type: 2},OSD1_ESCTEMP_EN: {value: 0, index: 1100, type: 2},OSD1_ESCTEMP_X: {value: 42, index: 1101, type: 2},OSD1_ESCTEMP_Y: {value: 2, index: 1102, type: 2},OSD1_FENCE_EN: {value: 0, index: 1223, type: 2},OSD1_FENCE_X: {value: 14, index: 1224, type: 2},OSD1_FENCE_Y: {value: 9, index: 1225, type: 2},OSD1_FLTIME_EN: {value: 0, index: 1148, type: 2},OSD1_FLTIME_X: {value: 23, index: 1149, type: 2},OSD1_FLTIME_Y: {value: 10, index: 1150, type: 2},OSD1_FLTMODE_EN: {value: 0, index: 1067, type: 2},OSD1_FLTMODE_X: {value: 25, index: 1068, type: 2},OSD1_FLTMODE_Y: {value: 17, index: 1069, type: 2},OSD1_FONT: {value: 0, index: 1263, type: 2},OSD1_GNDTRVL_EN: {value: 0, index: 1142, type: 2},OSD1_GNDTRVL_X: {value: 22, index: 1143, type: 2},OSD1_GNDTRVL_Y: {value: 11, index: 1144, type: 2},OSD1_GPSLAT_EN: {value: 0, index: 1118, type: 2},OSD1_GPSLAT_X: {value: 9, index: 1119, type: 2},OSD1_GPSLAT_Y: {value: 13, index: 1120, type: 2},OSD1_GPSLONG_EN: {value: 0, index: 1121, type: 2},OSD1_GPSLONG_X: {value: 9, index: 1122, type: 2},OSD1_GPSLONG_Y: {value: 14, index: 1123, type: 2},OSD1_GSPEED_EN: {value: 0, index: 1073, type: 2},OSD1_GSPEED_X: {value: 0, index: 1074, type: 2},OSD1_GSPEED_Y: {value: 11, index: 1075, type: 2},OSD1_HDOP_EN: {value: 0, index: 1133, type: 2},OSD1_HDOP_X: {value: 0, index: 1134, type: 2},OSD1_HDOP_Y: {value: 0, index: 1135, type: 2},OSD1_HEADING_EN: {value: 0, index: 1082, type: 2},OSD1_HEADING_X: {value: 13, index: 1083, type: 2},OSD1_HEADING_Y: {value: 0, index: 1084, type: 2},OSD1_HOMEDIR_EN: {value: 0, index: 1187, type: 2},OSD1_HOMEDIR_X: {value: 5, index: 1188, type: 2},OSD1_HOMEDIR_Y: {value: 5, index: 1189, type: 2},OSD1_HOMEDIST_EN: {value: 0, index: 1184, type: 2},OSD1_HOMEDIST_X: {value: 14, index: 1185, type: 2},OSD1_HOMEDIST_Y: {value: 1, index: 1186, type: 2},OSD1_HOME_EN: {value: 0, index: 1079, type: 2},OSD1_HOME_X: {value: 22, index: 1080, type: 2},OSD1_HOME_Y: {value: 1, index: 1081, type: 2},OSD1_HORIZON_EN: {value: 0, index: 1076, type: 2},OSD1_HORIZON_X: {value: 25, index: 1077, type: 2},OSD1_HORIZON_Y: {value: 7, index: 1078, type: 2},OSD1_LINK_Q_EN: {value: 0, index: 1259, type: 2},OSD1_LINK_Q_X: {value: 5, index: 1260, type: 2},OSD1_LINK_Q_Y: {value: 1, index: 1261, type: 2},OSD1_LOIT_RAD_EN: {value: 0, index: 1345, type: 2},OSD1_LOIT_RAD_X: {value: 0, index: 1346, type: 2},OSD1_LOIT_RAD_Y: {value: 0, index: 1347, type: 2},OSD1_MESSAGE_EN: {value: 0, index: 1070, type: 2},OSD1_MESSAGE_X: {value: 10, index: 1071, type: 2},OSD1_MESSAGE_Y: {value: 15, index: 1072, type: 2},OSD1_NRG_CONS_EN: {value: 0, index: 1264, type: 2},OSD1_NRG_CONS_X: {value: 0, index: 1265, type: 2},OSD1_NRG_CONS_Y: {value: 0, index: 1266, type: 2},OSD1_NRG_REM_EN: {value: 0, index: 1306, type: 2},OSD1_NRG_REM_X: {value: 0, index: 1307, type: 2},OSD1_NRG_REM_Y: {value: 0, index: 1308, type: 2},OSD1_PEAK_PR_EN: {value: 0, index: 1333, type: 2},OSD1_PEAK_PR_X: {value: 0, index: 1334, type: 2},OSD1_PEAK_PR_Y: {value: 0, index: 1335, type: 2},OSD1_PEAK_RR_EN: {value: 0, index: 1330, type: 2},OSD1_PEAK_RR_X: {value: 0, index: 1331, type: 2},OSD1_PEAK_RR_Y: {value: 0, index: 1332, type: 2},OSD1_PGNDTRVL_EN: {value: 0, index: 1348, type: 2},OSD1_PGNDTRVL_X: {value: 22, index: 1349, type: 2},OSD1_PGNDTRVL_Y: {value: 11, index: 1350, type: 2},OSD1_PITCH_EN: {value: 0, index: 1127, type: 2},OSD1_PITCH_X: {value: 7, index: 1128, type: 2},OSD1_PITCH_Y: {value: 17, index: 1129, type: 2},OSD1_PLUSCODE_EN: {value: 0, index: 1202, type: 2},OSD1_PLUSCODE_X: {value: 0, index: 1203, type: 2},OSD1_PLUSCODE_Y: {value: 0, index: 1204, type: 2},OSD1_POWER_EN: {value: 0, index: 1199, type: 2},OSD1_POWER_X: {value: 1, index: 1200, type: 2},OSD1_POWER_Y: {value: 1, index: 1201, type: 2},OSD1_RC_FS_EN: {value: 0, index: 1342, type: 2},OSD1_RC_FS_X: {value: 0, index: 1343, type: 2},OSD1_RC_FS_Y: {value: 0, index: 1344, type: 2},OSD1_RC_THR_EN: {value: 0, index: 1267, type: 2},OSD1_RC_THR_X: {value: 0, index: 1268, type: 2},OSD1_RC_THR_Y: {value: 0, index: 1269, type: 2},OSD1_RESTVOLT_EN: {value: 0, index: 1220, type: 2},OSD1_RESTVOLT_X: {value: 24, index: 1221, type: 2},OSD1_RESTVOLT_Y: {value: 2, index: 1222, type: 2},OSD1_RNGF_EN: {value: 0, index: 1226, type: 2},OSD1_RNGF_X: {value: 0, index: 1227, type: 2},OSD1_RNGF_Y: {value: 0, index: 1228, type: 2},OSD1_ROLL_EN: {value: 0, index: 1124, type: 2},OSD1_ROLL_X: {value: 12, index: 1125, type: 2},OSD1_ROLL_Y: {value: 17, index: 1126, type: 2},OSD1_RSSI_EN: {value: 0, index: 1055, type: 2},OSD1_RSSI_X: {value: 0, index: 1056, type: 2},OSD1_RSSI_Y: {value: 4, index: 1057, type: 2},OSD1_R_AVG_CV_EN: {value: 0, index: 1303, type: 2},OSD1_R_AVG_CV_X: {value: 24, index: 1304, type: 2},OSD1_R_AVG_CV_Y: {value: 3, index: 1305, type: 2},OSD1_SATS_EN: {value: 0, index: 1064, type: 2},OSD1_SATS_X: {value: 0, index: 1065, type: 2},OSD1_SATS_Y: {value: 3, index: 1066, type: 2},OSD1_SIDEBARS_EN: {value: 0, index: 1178, type: 2},OSD1_SIDEBARS_X: {value: 0, index: 1179, type: 2},OSD1_SIDEBARS_Y: {value: 0, index: 1180, type: 2},OSD1_STATS_EN: {value: 0, index: 1145, type: 2},OSD1_STATS_X: {value: 0, index: 1146, type: 2},OSD1_STATS_Y: {value: 0, index: 1147, type: 2},OSD1_TEMP_EN: {value: 0, index: 1130, type: 2},OSD1_TEMP_X: {value: 0, index: 1131, type: 2},OSD1_TEMP_Y: {value: 0, index: 1132, type: 2},OSD1_TER_HGT_EN: {value: 0, index: 1214, type: 2},OSD1_TER_HGT_X: {value: 23, index: 1215, type: 2},OSD1_TER_HGT_Y: {value: 7, index: 1216, type: 2},OSD1_THR_OUT_EN: {value: 0, index: 1085, type: 2},OSD1_THR_OUT_X: {value: 0, index: 1086, type: 2},OSD1_THR_OUT_Y: {value: 11, index: 1087, type: 2},OSD1_TUNED_PN_EN: {value: 0, index: 1324, type: 2},OSD1_TUNED_PN_X: {value: 0, index: 1325, type: 2},OSD1_TUNED_PN_Y: {value: 0, index: 1326, type: 2},OSD1_TUNED_PV_EN: {value: 0, index: 1327, type: 2},OSD1_TUNED_PV_X: {value: 0, index: 1328, type: 2},OSD1_TUNED_PV_Y: {value: 17, index: 1329, type: 2},OSD1_TXT_RES: {value: 1, index: 1262, type: 2},OSD1_VSPEED_EN: {value: 0, index: 1097, type: 2},OSD1_VSPEED_X: {value: 42, index: 1098, type: 2},OSD1_VSPEED_Y: {value: 10, index: 1099, type: 2},OSD1_VTX_PWR_EN: {value: 0, index: 1211, type: 2},OSD1_VTX_PWR_X: {value: 0, index: 1212, type: 2},OSD1_VTX_PWR_Y: {value: 0, index: 1213, type: 2},OSD1_WAYPOINT_EN: {value: 0, index: 1136, type: 2},OSD1_WAYPOINT_X: {value: 0, index: 1137, type: 2},OSD1_WAYPOINT_Y: {value: 0, index: 1138, type: 2},OSD1_WIND_EN: {value: 0, index: 1091, type: 2},OSD1_WIND_X: {value: 0, index: 1092, type: 2},OSD1_WIND_Y: {value: 10, index: 1093, type: 2},OSD1_XTRACK_EN: {value: 0, index: 1139, type: 2},OSD1_XTRACK_X: {value: 0, index: 1140, type: 2},OSD1_XTRACK_Y: {value: 0, index: 1141, type: 2},},}
               </textarea>
           </td>
       </tr>
       <tr>
           <td colspan="2">
               <div id="error" class="newline error"></div>
           </td>
       </tr>
   </table>
</div>
<div id="maincontainer">
   <div style="float: left; border: none; float: left; clear: both; width: 1520px;">
      <div class="background" id="background" style="position:relative">
          <div id="grid" class="grid grid60x22"></div>
      </div>
      <div id="availableparameters" style="position: relative; overflow-y: scroll; height: 720px; width:auto; float: right; border: none;"></div>
      <div id="parachute_command"  style=" border: 1px solid black; float: left; clear:both; padding:20px"></div> 
  </div>        
</div>

<script src="https://unpkg.com/json5@2/dist/index.min.js"></script>
<script type="text/javascript">

function switchBackground(){
   document.getElementById('background').style.backgroundImage = "url(https://imgz.org/"+document.getElementById('chooseBackground').value+".jpg)";
}

function switchGrid(){
   gridSpec['x'] = document.getElementById('chooseGrid').value.split('x')[0];
   gridSpec['y'] = document.getElementById('chooseGrid').value.split('x')[1];
   document.getElementById('grid').setAttribute('class','grid grid'+document.getElementById('chooseGrid').value);
   compute();
}

function allowDrop(ev) {
   ev.preventDefault();
}

function drag(ev) {
   var source = ev.source || ev.srcElement;

   if(source.innerHTML != ""){
       var paramName = makeParamName(source.innerHTML);
       ev.dataTransfer.setData("paramName", paramName);
       ev.dataTransfer.setData("sourceid", source.id);
   }else{
       // alert("empty data");
   }
}

function remove(ev) {
   ev.preventDefault();
   var target = ev.target || ev.srcElement;
   var param = ev.dataTransfer.getData("paramName");
   var sourceid = ev.dataTransfer.getData("sourceid");
   
   console.log("removing param: "+param+" from "+sourceid);
   
   if(sourceid){
       document.getElementById(sourceid).innerHTML="";
   }

   osd_config[param]=parseInt(0);
   delete osd_config[param.replace('_EN','_X')];
   delete osd_config[param.replace('_EN','_Y')];
   osd_update[param]=parseInt(0);
   delete osd_update[param.replace('_EN','_X')]; //=parseInt(0);
   delete osd_update[param.replace('_EN','_Y')]; //=parseInt(0);

   generateOutput();
   generateCoordinates();
   drawOSD();
}

function drop(ev) {
   ev.preventDefault();
   var target = ev.target || ev.srcElement;
   var param = ev.dataTransfer.getData("paramName");
   var sourceid = ev.dataTransfer.getData("sourceid");
   var targetid = ev.target.id;

   osd_config[param]=parseInt(1);
   osd_config[param.replace('_EN','_X')]=parseInt(ev.target.id.split("x")[0]);
   osd_config[param.replace('_EN','_Y')]=parseInt(ev.target.id.split("x")[1]);

   osd_update[param]=parseInt(1);
   osd_update[param.replace('_EN','_X')]=parseInt(ev.target.id.split("x")[0]);
   osd_update[param.replace('_EN','_Y')]=parseInt(ev.target.id.split("x")[1]);

   generateCoordinates();
   generateOutput();
   drawOSD();

   document.getElementById(targetid).innerHTML = makePrettyParam(param);
   if(sourceid){
       document.getElementById(sourceid).innerHTML="";
   }
}


   var osd_element_width={
       ALTITUDE: 5,
       ASPEED: 6,
       ASPD1: 6,
       ASPD2: 6,
       ASPD_DEM: 6,
       AVGCELLV: 5,
       BATUSED: 5,
       COMPASS: -5,
       HORIZON: -5,
       FLTMODE: 4,
       GSPEED: 6,
       HOMEDIST: 7,
       MESSAGE: 26,
       PITCH: 5,
       ROLL: 6,
       RSSI: 3,
       SATS: 4,
       VSPEED: 5,
       WIND: 6,
       GNDTRVL: 6,
       AVG_EFFA: 5,
       EFFG: 5,
       ESCTEMP: 4,
       HOME: 7,
       THR_OUT: 5,
       RC_THR: 5,
       POWER: 5,
       NRG_CONS: 5,
       BAT_VOLT:5,
       CURRENT:4,
       AVG_EFFG: 5,
       FLTIME: 7,
       GPSLAT: 12,
       GPSLONG: 12,
       CALLSIGN: 6,
       LINK_Q: 7,
       CRSFANT: 4,
       CRSFPWR: 4,
       CRSFRSSI: 6,
       CRSFSNR: 5,
       TUNED_PV: 5,
   };

   var osd_coordinates={};
   var osd_update={};          // the dropped and altered configuration
   var osd_config={};          // the pasted configuration
   var osd_config_type='';     // might be parachute or missionplanner
   var gridSpec={ x:60, y:22 } // default grid size

   function genereateOSDObject(){
       osd_update={};
       osd_config={}; // fixme; do we need this?

       var txt = document.getElementById("config").value
       var json_converted_config = {}; 

       document.getElementById("availableparameters").innerHTML="<div ondragover='allowDrop(event)' ondrop='remove(event)' style='margin:5px'><b>DROP HERE TO REMOVE</b></div>";

       try {
           try {
               console.log("trying parachute");
               json_converted_config = JSON5.parse(txt)['parameters']; // this is for parachute input
               osd_config_type='parachute';
           } catch (e){
               console.log("trying mission planner");
               var lines=txt.split("\n");
               for(var i=0;i<lines.length;i++){
                   if(lines[i].match(",")){
                       var param=lines[i].split(",")[0].trim();
                       var value=lines[i].split(",")[1].trim();

                       if(param && value) {
                           console.log("saved "+ param);
                           json_converted_config[param] = {"value": parseInt(value)};  //{"value": value};
                       }else{
                           console.log("failed "+ param);
                       }
                   }
               }
               osd_config_type='missionplanner';
           }
           console.log(json_converted_config);
       } catch (e) {
           document.getElementById('error').style.display="block";
           document.getElementById('error').innerHTML="no valid config";
           return;
       }

       const active_osd_object   = Object.fromEntries(Object.entries(json_converted_config).filter(([key]) => key.includes('OSD1_')  &&  key.match('_EN$') && json_converted_config[key].value == 1 ));
       const disabled_osd_object = Object.fromEntries(Object.entries(json_converted_config).filter(([key]) => key.includes('OSD1_')  &&  key.match('_EN$') && json_converted_config[key].value == 0 ));

       // make  OSD drop list
       for (const [param, paramAttr] of Object.entries(disabled_osd_object)) {
           var div = document.createElement("div");
           div.setAttribute('ondrop',"drop(event)");
           div.setAttribute('ondragover',"allowDrop(event)");
           div.setAttribute('draggable',"true");
           div.setAttribute('ondragstart',"drag(event)");
           div.setAttribute('class', 'param');
           
           div.innerHTML = param; // param is OSD1_ALTITUDE_EN

           document.getElementById("availableparameters").appendChild(div);
       }

       console.log(active_osd_object);
       console.log("active elements: "+Object.entries(active_osd_object).length);
       
       document.getElementById('error').innerHTML="";
       document.getElementById('error').style.display="none";

           for (const [param, paramAttr] of Object.entries(active_osd_object)) {

               console.log('param: '+param);   //fixme  -> getname -> get param
               var elmX = json_converted_config[param.replace('_EN','_X')]['value'];   //fixme -> getX
               var elmY = json_converted_config[param.replace('_EN','_Y')]['value'];   //fixme -> getY

               // osd_update[param]=parseInt(1);
               // osd_update[param.replace('_EN','_X')]=parseInt(elmX);
               // osd_update[param.replace('_EN','_Y')]=parseInt(elmY);

               osd_config[param]=parseInt(1);
               osd_config[param.replace('_EN','_X')]=parseInt(elmX);
               osd_config[param.replace('_EN','_Y')]=parseInt(elmY);

               console.log('['+elmY+']['+elmX+']='+param);
       }
       generateCoordinates();
   }

   function generateCoordinates(){
       osd_coordinates={};
       for ([param, paramValue] of Object.entries(osd_config).filter(([key]) => key.includes('OSD1_')  &&  key.match('_EN$') )){
       
           var elmX = osd_config[param.replace('_EN','_X')];
           var elmY = osd_config[param.replace('_EN','_Y')];
           
           console.log("generateCoordinates "+ param+" at "+elmX+"x"+elmY);

           if(typeof osd_coordinates[elmY] == 'undefined'){
                   osd_coordinates[elmY]={};
               } 

           if (typeof osd_element_width[makePrettyParam(param)] !== 'undefined') {
               var elmStart = parseInt(elmX + 1 );
               var elmW = parseInt(osd_element_width[makePrettyParam(param)] + elmX);
               console.log("extending "+param+" to "+osd_element_width[makePrettyParam(param)]+" from X "+elmStart+" to "+elmW);

               if( osd_element_width[makePrettyParam(param)] < 0 ){ // handling centered elements like COMPASS or HORIZON
                   elmStart=parseInt(osd_element_width[makePrettyParam(param)] + elmX +1);
                   elmW = parseInt(osd_element_width[makePrettyParam(param)] + elmX + (osd_element_width[makePrettyParam(param)] * -1)+ (osd_element_width[makePrettyParam(param)] * -1));
               }

               for (var elmWidth = elmStart; elmWidth < elmW; elmWidth++ ){
                   console.log(param+" . "+elmWidth+"x"+elmY);
                   osd_coordinates[elmY][elmWidth]='.';
               }
           }

           if( typeof osd_coordinates[elmY][elmX] != 'undefined' ){
               console.error(elmX+"x"+elmY+" already used by "+osd_coordinates[elmY][elmX]);
               delete osd_coordinates[osd_coordinates[elmY][elmX]];
               delete osd_update[osd_coordinates[elmY][elmX]];
           }
           osd_coordinates[elmY][elmX]=param;

       }
   }

   function generateOutput(){
       var output='';

       if(osd_config_type=='parachute'){
           output="parachute set ";
       }
       for ( [param, value] of Object.entries(osd_update)) {
           if(param){
               if(osd_config_type=='parachute'){
                   output += param + "=" + value + " ";
               }else if(osd_config_type == 'missionplanner'){
                   output += param + "," + value + "<br> ";
               }
           }
       }
       document.getElementById('parachute_command').innerHTML = output;
   }


   function drawOSD(){
       document.getElementById("grid").innerHTML="";

       for (var y = 0; y < gridSpec['y'] ; y++) {   //18 for DJI // 20 for WS
           for (var x = 0; x < gridSpec['x'] ; x++) { //50 for DJI // 53 for WS

               var div = document.createElement("div");
               if(document.getElementById("showCoords").checked == true){
                   div.innerHTML = x+"<br>&nbsp;"+y;
               }
               
               div.setAttribute('id',x+"x"+y);
               div.setAttribute('ondrop',"drop(event)");
               div.setAttribute('ondragover',"allowDrop(event)");
               div.setAttribute('draggable',"true");
               div.setAttribute('ondragstart',"drag(event)");

               var divClasses=[];
               divClasses.push('box');
               divClasses.push('box_'+gridSpec['x']+'x'+gridSpec['y']);

               if (typeof osd_coordinates[y] !== 'undefined') { 
                   if (typeof osd_coordinates[y][x] !== 'undefined') { 
                       divClasses.push('used');
                       if (osd_coordinates[y][x] != '.'){
                           var elemName = osd_coordinates[y][x];
                           // div.innerHTML = elemName; // draw the name OSD1_ALTITUDE_EN
                           div.innerHTML = makePrettyParam(elemName); // draw the name OSD1_ALTITUDE_EN
                       }else{
                           div.innerHTML = "";
                           divClasses.push('occupied');
                       }
                   }
               }

               if (x == 0){
                   divClasses.push('start');
               }

               if( x == 49){
                   divClasses.push('end');
               }

               div.setAttribute('class', divClasses.join(" "));
               document.getElementById("grid").appendChild(div);
           }
       }
   }
   
   function makePrettyParam(OSD1_param_EN){
       return OSD1_param_EN.replace('OSD1_','').replace('_EN','');
   }

   function makeParamName(param){
       if(param == ""){
           return;
       }else if(param.match('^OSD1_')){
           return param;
       }else{
           return 'OSD1_'+param+'_EN';
       }
   }

   function getMatches(string, regex, index) {
       index || (index = 1); // default to the first capturing group
       var matches = [];
       var match;
       while (match = regex.exec(string)) {
           matches.push(match[index]);
       }
       return matches;
   }

   function compute(){
       genereateOSDObject();
       drawOSD();
       generateOutput();
       hideNavBars(); //for stavros page only
   }

   function hideNavBars(){
       Array.from(document.getElementsByClassName('nav-wide-wrapper')).forEach(function(navbar) {
           navbar.setAttribute('style', 'display: none');
       });
   }

   compute();
</script>

_(Many thanks to mfoos for writing this note.)_

* * *

<p style="font-size:80%; font-style: italic">
Last updated on March 13, 2023. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
