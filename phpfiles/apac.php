<?php
$servername = "localhost";
$username = "root";
$password = "Burger02";
$dbname = "Adroll";
$date = date('Y-m-d');
$weekendDay = false;
$day = date("D", strtotime("$date"));
if($day == 'Sat' || $day == 'Sun'){
    $weekendDay = 'Weekend';
}
else { $weekendDay = 'Weekday'; }
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO `posts_post` (`id`, `weekno`, `dete`, `stime`, `rtime`, `wtime`, `itype`, `descrp`, `env`, `hostype`, `hostname`, `mode`, `engineer`, `remediation`, `escalated`, `escreason`, `status`,`escalatedto`, `resolvedteam`, `resolvedby`, `resolution`, `source`, `others`, `respteam`, `falsealarm`, `yeer`, `dayofweek`, `menth`, `shyft`,`alertname`, `ghcname`, `taskname`, `comments`,`priority`) VALUES(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+05:30'))), date(convert_tz(now(), '+00:00', '+05:30')), '07:00', '07:00', '01:00', 'GHC', 'BI Pipeline Monitoring', 'Production', 'Jenkins', 'Jenkins BI', 'Email', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+05:30')),'APAC','NA','Pipeline monitoring','NA','No issues observed','None'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+05:30'))), date(convert_tz(now(), '+00:00', '+05:30')), '07:00', '07:00', '01:00', 'GHC', 'Omnom Pipeline Monitoring', 'Production', 'Batchie Patchie', 'app.adroll.com/batchiepatchie', 'Manual Check', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+05:30')),'APAC','NA','Pipeline monitoring','NA','No issues observed','None'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+05:30'))), date(convert_tz(now(), '+00:00', '+05:30')), '07:00', '07:00', '01:00', 'GHC', 'Data Pipeline Monitoring', 'Production', 'AWS EMR', 'aws.amazon.com', 'Manual Check', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+05:30')),'APAC','NA','Pipeline monitoring','NA','No issues observed','None'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+05:30'))), date(convert_tz(now(), '+00:00', '+05:30')), '07:00', '07:00', '01:00', 'GHC', 'Intent Segment Pipeline Monitoring', 'Production', 'AWS EMR', 'aws.amazon.com', 'Manual Check', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+05:30')),'APAC','NA','Pipeline monitoring','NA','No issues observed','None'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+05:30'))), date(convert_tz(now(), '+00:00', '+05:30')), '07:00', '07:00', '01:00', 'Task', 'Checked for EMR failures', 'Production', 'AWS EMR', 'aws.amazon.com', 'Manual Check', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+05:30')),'APAC','NA','NA','EMR Job Check','No issues observed','P1'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+05:30'))), date(convert_tz(now(), '+00:00', '+05:30')), '07:00', '07:00', '01:00', 'Task', 'Checked for EMRs running for more than 12 hours', 'Production', 'AWS EMR', 'aws.amazon.com', 'Manual Check', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+05:30')),'APAC','NA','NA','Long Running EMR Check','No issues observed','P2'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+05:30'))), date(convert_tz(now(), '+00:00', '+05:30')), '07:00', '07:00', '01:00', 'GHC', 'Monitored the Storm Topologies', 'Production', 'Storm cluster', 'app.datadoghq.com', 'Manual Check', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+05:30')),'APAC','NA','Storm Monitoring','NA','No issues observed','P2'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+05:30'))), date(convert_tz(now(), '+00:00', '+05:30')), '07:00', '07:00', '01:00', 'GHC', 'Checked the Celery dashboard for failures', 'Production', 'Celery Worker', 'app.adroll.com/backstage/celerytasks/hud', 'Manual Check', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+05:30')),'APAC','NA','Celery Dashboard check','NA','No issues observed','P2')";

if ($conn->query($sql) === TRUE) {
    echo $date . " APAC Tickets created successfully\n";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
