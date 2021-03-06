 <?php 
 	  $conditions = array(
      '1' => '生命低于',
      '2' => '回合数等于',
    );


    require_once 'lib/config.php';
    require_once 'lib/mysql.php';

    $db = db_connect();

    $allEnemySkill = array();
    $sql = "select `id`,`name` from skill where `type` = 5;";
    $allEnemySkills = db_query($db, $sql);

    foreach ($allEnemySkills as $value){
      $allEnemySkill[$value['id']] = $value['name'];
    }

 ?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>jQuery UI Dialog - Default functionality</title>
  <link rel="stylesheet" href="../jquery-ui.css">
  <script src="../jquery.min.js"></script>
  <script src="../jquery-ui.min.js"></script>
  <style type="text/css">
 	.editor {width: 70px;}
  	
    .ui-dialog .ui-dialog-buttonpane { 
    text-align: center;
}
.ui-dialog .ui-dialog-buttonpane .ui-dialog-buttonset { 
    float: none;
}
  </style>
</head>
<script>
 
 

</script>

<body>
<div id="dialog" title="BOSS脚本配置">
  <table>
  	<tr>
  		<table id="config">
  		
  		</table>
  	</tr>
  </table>
</div>
</body>
  </html>
  <script>
  var skills_list = [
  <?php
  $allEnemySkill[0] = '无'; 
  foreach ($allEnemySkill as $key => $value) {
    echo "{value:'{$value}', id:'{$key}'},".PHP_EOL;
  }
  ?>
  ];
  var select_c_html = '<?=html_get_select("conditions", $conditions, 1)?>';
  var input_v_html = '<?=html_get_input("value", 0)?>';
  var select_s_html = "<?php echo html_get_auto_completed_input('boss_skill##id', 'skills', $allEnemySkill, 0, 120); ?>";
  //var select_s_html = '<?=html_get_select("skills", $allEnemySkill, 0)?>';
  var input_p_html = '<?=html_get_input("power", 0)?>';
  var ind = 1;

  function delRow(node) {
    $(node).parent().parent().remove();
  }

  function newConfig() {
    $('#config').append('<tr><th>当'+select_c_html+'</th><th>'+input_v_html+'</th><th>触发技能'+select_s_html.replace(/##id/g,ind)+' </th><th>威力'+input_p_html+'</th><th><a href="#" onclick="delRow(this)">&nbsp;&nbsp;删除</a></th></tr>');
    ind++;
    $('.skills').autocomplete({
        lookup: skills_list, 
        minChars: 0,
        onSelect: function(s){
          $('#' + this.id + '_hidden')[0].setAttribute('value', s.id);
        }
      });
  }

  function commit(boss_id) {
      var config = [];

      $("select[name='conditions[]']").each(function() {
        config.push({"condition":$(this).val(), "val":0, "skill_id":0, "power":0});
      });

      var i = 0;
      $("input[name='value[]']").each(function(){
        config[i++]['val'] = $(this).val();
      });
      
      i = 0;
      $("input[name='skills[]']").each(function(){
        config[i++]['skill_id'] = $(this).val();
      });


      i = 0;
      $("input[name='power[]']").each(function(){
        config[i++]['power'] = $(this).val();
      });

      var postConfig = [];
      i = 0;
      for (; i < config.length; i++) {
          if (config[i].val > 0 && config[i].skill_id > 0) {
             postConfig.push(config[i]);
          }
      }
      
      if (postConfig.length == 0) {
        return
      }

      $.post("pages/enemy_boss_script_ajax.php",
      {
        boss_id:boss_id,
        config:JSON.stringify(postConfig),
      },
      function(data, status){
        console.log(data, status);
        if (status != 'success') {
          alert("保存失败");
        }
      });
  }

  function open_editor(boss_id) {
    $('#config tr').remove();
    ind = 1;
    $.get("pages/enemy_boss_script_ajax.php?boss_id=" + boss_id,function(data, status){
      if (status != 'success') {
        alert("无法获取配置数据");
        return
      }
      
      var config = JSON.parse(data);
      if (config.length == 0){
        newConfig();
        return
      }

      var i=0;
      for (;i<config.length; i++){
        $('#config').append(newConfig());
      }

      i = 0;
      $("select[name='conditions[]']").each(function() {
        $(this).val(config[i++]['condition']);
      });

      i = 0;
      $("input[name='value[]']").each(function(){
        $(this).val(config[i++]['val']);
      });
      
      i = 0;
      for(i=1;i<=config.length;i++){
        items = $.grep(skills_list, function(n){
          return n.id == parseInt(config[i-1]['skill_id']);
        });
        item = items[0];
        $("#boss_skill"+i).val(item.value);
        $("#boss_skill"+i+"_hidden").val(item.id);
      }

      i = 0;
      $("input[name='power[]']").each(function(){
        $(this).val(config[i++]['power']);
      });
    });

     $( "#dialog" ).dialog(
      {width:550, height:400},
      { buttons:[
         { text: "添加", click: function() { newConfig(); }},
         { text: "保存", click: function() { commit(boss_id);$( this ).dialog( "close" ); }},
      ]}
     );
   }
  </script>
