define tablename = &1
define filename = &2
SET LOAD SCAN_ROWS 5000
SET LOAD ERRORS 100
drop table &tablename;

load &tablename Fullpath\&filename NEW
exit;

