<?
//Відкриття доступу до БД
define("HOST","127.0.0.1");
define("USER","host2467");
define("PASSWORD","6IaOSBDr");
define("DB","itelit_host2467");
$db=mysql_connect(HOST,USER,PASSWORD);
if (!$db){
exit("Немає доступу до бази даних,помилка - ".mysql_error());
}
if (!mysql_select_db(DB,$db)){
exit("Неможливо вибрати базу даних ".mysql_error());	
}
mysql_query("SET NAMES 'utf8'");
?>