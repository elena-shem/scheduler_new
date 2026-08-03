<?php

namespace Fuel\Migrations;

class Rename_table_welcomes_to_welcomeposts
{
	public function up()
	{
		\DB::query('ALTER TABLE welcomes RENAME TO welcomeposts;')->execute();
	}

	public function down()
	{
		\DBUtil::rename_table('welcomeposts', 'welcomes');
	}
}