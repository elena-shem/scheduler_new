<?php

namespace Fuel\Migrations;

// Имя класса должно в точности совпадать с именем файла (без 025_)
class Add_uploaderid_to_uploads 
{
    public function up()
    {
        \DBUtil::add_fields('uploads', array(
            'uploaderid' => array(
                'constraint' => 11, 
                'type'       => 'int',
                'null'       => false,
                'default'    => 0 
            ),
        ));
    }

    public function down()
    {
        \DBUtil::drop_fields('uploads', array(
            'uploaderid'
        ));
    }
}