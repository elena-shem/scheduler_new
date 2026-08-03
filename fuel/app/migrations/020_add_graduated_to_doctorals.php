<?php

namespace Fuel\Migrations;

class Add_graduated_to_doctorals
{
    public function up()
    {
        \DBUtil::add_fields('doctorals', array(
            'graduated' => array(
                'type'    => 'tinyint',
                'null'    => false,
                'default' => 0 
            ),
        ));
    }

    public function down()
    {
        \DBUtil::drop_fields('doctorals', array(
            'graduated'
        ));
    }
}