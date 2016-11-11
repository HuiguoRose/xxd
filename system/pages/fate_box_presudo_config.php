<?php

$pconfig = array(
	'title'   => '命锁宝箱伪随即',
	'table'   => 'chest',
	'links'   => array(),
	
	'columns' => array(
		array('name' => 'fix_award_count', 'text' => '抽奖次数', 'width' => '80px'),
	),
	
	'opera' => array(
		array('type' => 'link', 'text' => '设置物品', 'render' => 'itemtable'),
	),

	'where' 		=> 'sql_where',
	'insert'  		=> 'sql_insert',
);

function sql_where($params) {
	if(!isset($params['m'])) {
		die('缺少宝箱类型参数');
	}
	return " where `type` = {$params['m']}";
}

function sql_insert($params) {
	if(!isset($params['m'])) {
		die('缺少宝箱类型参数');
	}
	return " `type` = {$params['m']}";
}

function itemtable($row) {
	return html_get_link("设置物品", "?p=chest_item&m=".$row['id'], false);
}

?>
