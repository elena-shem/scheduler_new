<?php

namespace Fuel\Migrations;

class Add_emailpriority_to_globalsettings
{
    public function up()
    {
        \DBUtil::add_fields('globalsettings', array(
            'emailpriority' => array(
                'type'       => 'varchar', 
                'constraint' => 50,           
                'null'       => false, 
                'default'    => '3 (Normal)' 
            ),
        ));
    }

    public function down()
    {
        \DBUtil::drop_fields('globalsettings', array(
            'emailpriority'
        ));
    }
}