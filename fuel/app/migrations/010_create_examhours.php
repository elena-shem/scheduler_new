<?php

namespace Fuel\Migrations;

class Create_examhours
{
	public function up()
	{
		\DBUtil::create_table('examhours', array(
			'id' => array('type' => 'INTEGER PRIMARY KEY AUTOINCREMENT'),
			'period_id' => array('constraint' => 11, 'type' => 'int'),
			'start' => array('type' => 'time'),
			'end' => array('type' => 'time'),
			'created_at' => array('constraint' => 11, 'type' => 'int', 'null' => true),
			'updated_at' => array('constraint' => 11, 'type' => 'int', 'null' => true),

		), array());
	}

	public function down()
	{
		\DBUtil::drop_table('examhours');
	}
}